#!/bin/bash
# This script is used for pushing to the base image repo
# You can use a similar style script to push to your own repo
version_tag=$(cat docker_build/version.txt)
printf -v date_tag '%(%m%d%Y)T' -1
docker build . -t trendscenter/trendssetter-base:v${version_tag}_${date_tag}