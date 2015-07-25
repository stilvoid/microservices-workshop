#!/bin/bash

circo -Tpng functions.dot > functions.png
dot -Tpng components.dot > components.png
landslide -l no -t ./theme slides.md
