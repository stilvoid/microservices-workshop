#!/bin/bash

while true; do
    inotifywait -r -e modify ./
    ./make.sh
done
