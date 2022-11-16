"""Simple Example Application which runs
BIDS Validator on a provided root directory
and then uses pybids to print some basic queries
"""
# Python Builtins
import os
import json
import argparse
# External Libraries
from bids_validator import BIDSValidator
from bids import BIDSLayout

DEFAULT_PARAMETERS = dict(
    # These are parameters for our application
    do_validate=True,
    get_subjects=True,
    get_sessions=True,
    get_tasks=True,
    # And params for the BIDS layout
    absolute_paths=True,
    derivatives=False,
    config=None,
    sources=None,
    regex_search=False,
    database_path=None,
    reset_database=False,
    indexer=None
)


def create_parser() -> argparse.ArgumentParser:
    """Creates an argument parser for the application
    ARGS:
        N/A
    KWARGS:
        N/A
    """
    parser = argparse.ArgumentParser("BIDS Validation + Queries")
    parser.add_argument("root-dir",
                        help="""The path of the BIDS""" +
                        """directory to validate/parse""",
                        type=str,
                        required=True)
    parser.add_argument("output-dir",
                        help="The path to dump query output to",
                        type=str,
                        required=True)
    parser.add_argument("--output-file",
                        help="The name of the query output file (JSON)",
                        default="bids_validation.json",
                        type=str,
                        required=False
                        )
    parser.add_argument("-p",
                        "--parameters",
                        help="Parameters for validation (JSON file)",
                        default=None,
                        type=str,
                        required=False
                        )
    parser.add_argument("-v",
                        "--verbose",
                        help="Print output to command line?",
                        action="store_true")
    return parser


def validate(root: str) -> bool:
    """Validates a BIDS directory.
        Basically, just wrap the usage example from the documentation
    ARGS:
        NAME    TYPE    DESC
        root    (str)   The Directory to Parse
    KWARGS:
        N/A
    """
    return BIDSValidator().is_bids(root)


def make_queries(root: str,
                 do_validate: bool = True,
                 get_subjects: bool = True,
                 get_sessions: bool = True,
                 get_tasks: bool = True,
                 **kwargs) -> dict:
    """Creates a PyBids object at the root, and does basic queries
    ARGS:
        NAME    TYPE    DESC
        root    (str)   The Directory to Parse
    KWARGS:
        NAME            TYPE    DESC                DEFAULT
        do_validate     (bool)  Do BIDS Validation? True
        get_subjects    (bool)  Do subjects query?  True
        get_sessions    (bool)  Do sessions query?  True
        get_tasks       (bool)  Do tasks query?     True

        ADDITIONAL KWARGS GET PASSED TO BIDSLayout constructor
    """
    layout = BIDSLayout(root, **kwargs)
    results = dict()
    if do_validate:
        results["valid"] = validate(root)
    if get_subjects:
        results["subjects"] = layout.get_subjects()
    if get_sessions:
        results["sessions"] = layout.get_sessions()
    if get_tasks:
        results["tasks"] = layout.get_tasks()
    return results


def main(args):
    """Run the application using the args namespace from ArgumentParser"""
    root_dir = args.root_dir
    output_dir = args.output_dir
    output_file = args.output_file
    full_output_path = os.path.join(output_dir, output_file)
    parameter_file = args.parameters
    parameter_dict = DEFAULT_PARAMETERS
    if parameter_file is not None and os.path.exists(parameter_file):
        with open(parameter_file, "r") as json_input_handle:
            parameter_dict = json.load(json_input_handle)
    query_dict = make_queries(root_dir, **parameter_dict)
    if args.verbose:
        print("***** BIDS QUERIES *****")
        print(query_dict)
    with open(full_output_path, "w") as json_output_handle:
        json.dump(query_dict, json_output_handle)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    main(args)
