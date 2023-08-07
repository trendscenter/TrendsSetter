#!/bin/bash
# This script is used for building a singularity image 
# from the current version.
# The tag will default to the current date. 
version_tag=$(cat docker_build/version.txt)
printf -v date_tag '%(%m%d%Y)T' -1
cmd="singularity build BASE.img docker://trendscenter/TrendsSetter-BASE:v${version_tag}_${date_tag}"
echo cmd