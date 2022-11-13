FROM ubuntu:18.04
RUN apt update
RUN apt install -y git
RUN apt install  -y curl
RUN apt install -y jq
RUN git clone https://github.com/muzamilabbasi/DemoProjects.git
WORKDIR /DemoProjects/brightSign/
RUN chmod +x .
ARG API_KEY
ENV API_KEY=$API_KEY
