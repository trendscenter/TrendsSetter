# TReNDs-Setter Base Template

This base template includes an example application written in python for validating and performing simple queries on directories made to follow the [BIDS](https://bids-specification.readthedocs.io/en/stable/) standard. The purpose of this template is not for production use, but is a basic example for creating Dockerfiles for NeuroImaging, which follows the [SPEC](../trendssetter_spec_current.pdf). 

The [Dockerfile](./Dockerfile) for this application includes basic dependencies, a miniconda installation, and an example of providing an entrypoint for running an application in docker. For more details on the design of the template please read the [SPEC](../trendssetter_spec_current.pdf).


# What is in the BASE Template

See the [SPEC](../trendssetter_spec_current.pdf) for what dependencies are included in the base image.

## Build Scripts

A few handy tools are included in the `docker_build` folder. The file [build.sh](./docker_build/build.sh) builds the BASE template image on your local machine, and tags it according to the requirements for naming docker-hub repos in the [SPEC](../trendssetter_spec_current.pdf). The file [push.sh](./docker_build/push.sh) pushes the image to the associated docker hub repo (access rights to the repo, and a call to `docker login` will be required to push the image.)

Additionally the script [singularity_build.sh](./docker_build/singularity_build.sh) shows how the image can be built in singularity (by default using today's tag).

## BIDS Validation

The included example application is a simple script in python which wraps BIDS validation a few common queries using the [bids_validator](https://github.com/bids-standard/bids-validator) and [pybids](https://github.com/bids-standard/pybids) python libraries. The application takes an input and output directory as arguments, in addition to some parameters which control the creation of the BIDSLayout pybids objects. You can find documentation on those parameters in the PyBids [here](https://bids-standard.github.io/pybids/generated/bids.layout.BIDSLayout.html#bids.layout.BIDSLayout).

#### Running the Script

The script is run from the command line with:
```python bids_validation.py <input_dir> <output_dir> --verbose --parameters <parameter_file.json>```

This usage has been included in the run-script for the image: [run.sh](./run.sh), which is the entrypoint for the docker image. 

#### Python Design Principles

This application is written to also demonstrate some (but not all) good practices for writing dockerized applications in python, including: 

* inclusion of a [requirements.txt](./requirements.txt) file (even though all dependencies are included in the base template already)
* adherence to [PEP8](https://peps.python.org/pep-0008/) style standards, such as inclusion of docstrings in all functions, and use of underscores in variable and function names
* the use of the `__main__` namespace for command-line execution in python
* using [.dockerignore](./.dockerignore) to avoid inclusion of *.pyc files in the image

For more details on good design practices in python, please consult the [PEP8](https://peps.python.org/pep-0008/) documentation, and the [python docs](https://docs.python.org/3/).
