#!/bin/bash

git fetch
git pull
docker compose down
docker compose up -d --build
