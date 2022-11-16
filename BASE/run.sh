#!/bin/bash
# An example run script in bash, which serves as an entrypoint for the dockerized application
# This script should NEVER INSTALL DEPENDENCIES. All dependencies should exist already in the Dockerfile
# This script should not do extensive work in terms of parsing user input, scanning filesystems etc.
#   but should instead provide a single pipeline for running each stage of the application

# Inputs:
#   The run script should really only take a few standardized inputs on the command line
#       1) the input directory (BIDS-compliant, and in /input)
#       2) the output directory (Mounted to the image in /output)
#       3) a parameter file (JSON)
input_directory=$1
output_directory=$2
parameter_file=$3

# The application:
#   In this instance, the application is just a single python call
python /app/bids_validation/main.py $input_directory $output_directory --parameters $parameter_file
