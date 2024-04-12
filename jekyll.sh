#!/bin/bash

IMAGE_NAME="jekyll-runner"

error_exit()
{
	echo "$1" 1>&2
	exit 1
}

docker info >/dev/null 2>&1 || error_exit "Docker daemon is not running. Please start Docker."

if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
  echo "Docker image not found. Building the image..."
  docker build -t $IMAGE_NAME . || error_exit "Failed to build the Docker image."
else
  echo "Docker image $IMAGE_NAME found. No need to build."
fi

if [ $# -eq 0 ]; then
    error_exit "No command provided. Usage: $0 <command> [args...]"
fi

docker run --rm -u $(id -u):$(id -g) -v "${PWD}:/srv/jekyll" $IMAGE_NAME "$@" || error_exit "Failed to run the Jekyll command."
