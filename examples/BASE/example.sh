#!/bin/bash
echo Running docker image
docker run -v $(pwd)/output:/output -v $(pwd)/ds000122:/input/ds000122 trendscenter/trendssetter-base /app/run.sh /input/ds000122 /output /app/bids_validation/default_parameters.json
echo Finished running docker image
cat output/bids_validation.json
echo 
