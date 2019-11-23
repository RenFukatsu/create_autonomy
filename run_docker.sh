#!/bin/bash

xhost +

SCRIPT_DIR=$(cd $(dirname $0); pwd)

IMAGE_NAME="create_autonomy"

echo $IMAGE_NAME

docker run -it --rm \
  --net="host" \
  --volume="$SCRIPT_DIR/:/root/ros2_ws/src/create_autonomy/" \
  --name=create_autonomy \
  $IMAGE_NAME \
  bash
