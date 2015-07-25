# Things to do first

## Get on the WiFi

    SSID: `<blahblah>`

    Password: `<blahblah>`

## Install an SSH client

    Windows: PuTTY is good

    OSX and Linux: You've already got one :P

---

# Building micro-services with Docker

---

# About me

Steve Engledow - Head of software delivery for cloud at [Proxama](http://proxama.com)

![It's'a me](http://offend.me.uk/media/images/me.png)

## Links

Email: <steve@offend.me.uk>

Github: <https://github.com/stilvoid>

Twitter: [@stilvoid](https://twitter.com/stilvoid)

# Presenter notes

* Last 12 months migrating away from 3 years of monolith

---

# Agenda

## Part 1: Introduction to micro-services

* What? Why? How?
* Getting set up

## Part 1: Developing with `Docker`

* Introducing `docker-compose`
* Write some code; build some services

## Lunch

* Open to suggestions...

## Part 2: Deploying micro-services

* Options for deployment
* Deploy!

---

# Introduce yourself

---

# Micro-services - what, why, how?

---

# What are micro-services?

> Do one thing and do it well.

## Independent processes

* Based on capabilities

## Small and self-contained

* High maintainability

## Immutable

* Easy to replace

## Decoupled

* Communicate by API

# Presenter notes

UNIX philosophy

---

# Why *not* micro-services?

## Mistrust from the old-school

> Anything invented after you're thirty-five is against the natural order of things.
>
> \- Douglas Adams

## It's not always appropriate

* Tightly-coupled systems
* If it ain't broke...

## New problems to solve

* Network
* Serialisation
* Fault tolerance
* Testing and deployment

## Presenter notes

* Network - load balancing
* Serialisation - overhead, message formats
* Testing - today :D

---

# Why micro-services?

## Automation

* Testing
* Continuous delivery

## Resilience

* Fault tolerance
* Zero-downtime deployment

## Maintainability

* Low barrier to feature development

## Diversity

* Choose the best tool for the job

## Presenter notes

* Diversity - opportunities to learn too ;)

---

# How to design for micro-services

1. Outline functionality

2. Map dependencies

3. Identifier clusters

4. Pick your balance

5. If in doubt, start bigger

---

# Getting set up

---

# AWS Setup


1. Make an account at <http://aws.amazon.com>

    (Or log in to your existing account)

2. Redeem your voucher

3. Create an EC2
    * Ubuntu
    * Be sure to save your ssh key
    * Take a note of the IP address

4. Install software

        !bash
        $ apt-get install docker.io git vim

    (Replace `vim` with your favourite editor)

---

# Docker setup

1. Make an account at <https://hub.docker.com>

    (Or log in to your existing account)

2. Login through your EC2

        !bash
        $ docker login

---

# Brief guide to Docker

---

# Brief Docker guide/refresher

## Pull an image from the registry

    !bash
    $ docker pull mongo

## Run a container

    !bash
    $ docker run -d -P --name db mongo

## List running containers

    !bash
    $ docker ps

## See a container's logs

    !bash
    $ docker logs db

## Stop a container

    !bash
    $ docker stop db

## Remove a container

    !bash
    $ docker rm db

---

# Developing with Docker

---

# Developing with Docker

## The task

Build a persistent, multi-user, web-based chat service.

With a bot!

Prototype: <http://code.offend.me.uk/babble-proto>

## Check out the base project

    !bash
    $ git clone git@github.com:stilvoid/microservices-workshop.git

## Build and run the prototype yourself

    !bash
    $ cd prototype
    $ docker build -t babble-proto ./
    $ docker run -ti --rm -p 80:80 babble-proto

## Visit <http://<your EC2 IP>> to see it

## Presenter notes

* Start with a prototype

---

# Project structure

---

# Functionality

![Functions](functions.png)

# Presenter notes

Draw vertical slices

---

# Components

Conveniently mapping what's in the repository...

## Room service

Handles creation of rooms, listing rooms, registering users, modifying room memberships.

## Message service

Handles storage and retrieval of messages. Allows filtering messages by room.

## UI service

Serves up a web interface that consumes APIs from the other services.

## Bot service

A service that waits for a `!quote` messages and posts a random quote.

## Quote service

Has a database of quotes and an API to retrieve one at random.

---

# Introducing docker-compose

---

# The problem

1. Docker requires you to remember sometimes complex invocations, e.g. ports and volume mounts.

        !bash
        $ docker run -d -p 27017:27017 -v $(pwd):/data mongo

2. Defining relationships between containers requires manual wiring up.

        !bash
        $ docker run -d --name db mongo      # Run a mongo db

        $ docker run -d --link db:db my-app  # Run my app, link it to the db

3. Managing a suite of related containers isn't easy, i.e. you need to remember to mention each container involved.

        !bash
        $ docker stop mongo my-app  # Stop everything

        $ docker rm mongo my-app    # Remove the containers

---

# The solution

Docker-compose is a tool that allows you to easily maintain a collection of services, their configuration, and the links betweem them using a simple YAML format that mirrors docker command line options:

## Example

    !YAML
    db:                    # --name db
        image: mongo
        ports:
            - 27017:27017  # -p 27017:27017
        volumes:
            - .:/data      # -v $(pwd):/data

    app:                   # --name app
        image: my-app
        links:
            - db           # --link db:db

It's easy to start and stop the whole stack:

    !bash
    $ docker-compose up -d  # Run detached (background)

    $ docker-compose stop   # Stop everything

    $ docker-compose rm     # Remove everything

---

# Other uses

Docker-compose is useful for running test suites or build processes.

## Example

Define a service with links to services that come up in known states (e.g. a blank database), and a target for running test suites.

    !YAML
    test:
        build: ./             # Build the image from current dir
        command: run_tests    # Use a custom command
        volumes:
            - .:/usr/src/app  # Mount the current source
        links:
            - db:testdb       # Link the test database

    testdb:                   # No need to mount a data dir
        image: mongo          # as we don't want it to persist

And then you simply run:

    docker-compose run --rm test

---

# Linking containers

Some cases need direct service-to-service linking:

    !yaml
    db:
        image: mongo

    app:
        image: my-app
        links:
            - db:db

In some other cases, passing in configuration is enough.

Enter environment variables:

    !yaml
    web:
        build: ./web
        ports:
            - 8000:80  # Run on port 8000
        environment:
            api_url: http://localhost:8001

    api:
        build: ./api
        ports:
            - 8001:80  # Run on port 8001

# Presenter notes

Explain about linking - hostname internally

---

# Coding time!

---

# Exercise one - full stack

The repository contains code for each service.

Write a `docker-compose.yml` to run them all together on a single machine.

![Components](components.png)

Documentation is at <https://docs.docker.com/compose/yml/>.

.qr: 150|https://docs.docker.com/compose/yml/

Visit <http://<your EC2 IP>> to see if it worked.

---

# Exercise two - the services

---

# Introducing Bottle

Bottle is a python web micro-framework.
