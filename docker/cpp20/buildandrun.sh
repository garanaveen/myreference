#!/bin/bash

#Build this docker,
docker build . -t cpp_test:1

#Run the docker,
docker run --rm -it  cpp_test:1

