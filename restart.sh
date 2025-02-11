#!/bin/bash

# git
git fetch
git pull

# docker
docker compose down
docker compose up  --build
