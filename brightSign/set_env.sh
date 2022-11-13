#!/bin/bash
unamestr=$(uname)

if [ $unamestr = 'Darwin' ] 
then
    echo "Installing dependencies for:" $unamestr
    brew update
    brew install jq

else
    echo "Installing dependencies for Linux"
    apt update
    apt install -y git
    apt install  -y curl
    apt install -y jq
    git clone https://github.com/muzamilabbasi/DemoProjects.git
    cd /DemoProjects/brightSign/
    chmod +x .
fi
