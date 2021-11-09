FROM gcc:latest
COPY . /usr/scr/cpp20
WORKDIR /usr/scr/cpp20
RUN g++ --std=c++2a -o hellocpp20 main.cpp
CMD [ "./hellocpp20" ]

