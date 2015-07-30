# Building the slides

The slide deck is build using [Landslide](https://github.com/adamzap/landslide) and [Graphviz](http://graphviz.org/).

You may build the slide deck by installing both tools and then running:

    ./make.sh

Alternatively, you can use the provided [docker-compose](https://docs.docker.com/compose/) setup:

    docker-compose run build

Both of these methods will output the presentation in the file `presentation.html`.
