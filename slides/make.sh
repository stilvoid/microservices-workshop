#!/bin/bash

circo -x -Tpng functions.dot > functions.png
neato -x -Tpng coupled.dot > coupled.png
circo -Tpng decoupled.dot > decoupled.png
dot -Tpng components.dot > components.png
landslide -i -l no -t ./theme slides.md
