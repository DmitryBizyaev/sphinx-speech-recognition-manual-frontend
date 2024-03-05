#!/bin/bash

echo "apt-get update"
sudo apt-get update &> /dev/null

echo "check python version"
sudo python3 --version 2> /dev/null

echo "pip install"
sudo apt-get install python3-pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo "pip update"
sudo pip3 install --upgrade pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo "flask install"
sudo pip3 install Flask &> /dev/null
sudo pip3 show Flask 2> /dev/null

echo "server start"
sudo flask run --host=0.0.0.0 --port=5555
