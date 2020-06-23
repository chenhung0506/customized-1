#!/bin/bash
# REPO=docker-reg.emotibot.com.cn:55688
WORK_PATH=$(dirname "$0")
source ${WORK_PATH}/build.sh 
REPO=hub.docker.com
CONTAINER=transmit-tags

export TAG=$(git rev-parse --short HEAD)
set -o allexport
source dev.env
set +o allexport

echo "[ -------- 1.   build and run        -------- ]"
echo "[ -------- 2.   pull image and run   -------- ]"
echo "[ -------- 3.   run module           -------- ]"
echo "[ -------- 4.   run module -d        -------- ]"
echo "[ -------- 5.   stop module          -------- ]"

if [ $# -eq 1 ]; then
    mode=$1
else
    read mode
fi

echo "mode:"$mode
CMD=""


if [ $mode == "1" ]; then
    echo "[ -------- 1.   build and run        -------- ]"
    build
#    imagePull
    dockerComposeUp
elif [ $mode == "2" ]; then
    echo "[ -------- 2.   pull image and run   -------- ]"
    CMD=("imagePull" "dockerComposeUp")
elif [ $mode == "3" ]; then
	echo "[ -------- 3.   run module           -------- ]"
    read -p "Enter TAG: " INPUT_TAG
    echo "input TAG: $INPUT_TAG"
    export TAG=$INPUT_TAG
    CMD=("docker-compose up")
elif [ $mode == "4" ]; then
	echo "[ -------- 3.   run module           -------- ]"
    read -p "Enter TAG: " INPUT_TAG
    echo "input TAG: $INPUT_TAG"
    export TAG=$INPUT_TAG
    CMD=("docker-compose up -d")
else
	echo "[ -------- 5.   stop module          -------- ]"
    CMD=("docker-compose down")
fi

if [[ ${#CMD} > 0 ]]; then
    for val in "${CMD[@]}"; do
      echo $val && eval $val
    done
fi
