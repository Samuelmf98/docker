#!/bin/bash

# Determine script directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo $SCRIPT_DIR
# Change directory to project directory
cd $SCRIPT_DIR

# docker compose -f ../pokedex/docker-compose.yaml up $*
docker compose -f pokedex/docker-compose.yaml up $* 