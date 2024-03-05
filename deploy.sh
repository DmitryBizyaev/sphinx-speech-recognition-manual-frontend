#!/bin/bash

echo $"\napt-get update"
sudo apt-get update &> /dev/null

echo $"\ncheck python version"
sudo python3 --version 2> /dev/null

echo $"\npip install"
sudo apt-get install python3-pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo $"\npip update"
sudo pip3 install --upgrade pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo $"\nflask install"
sudo pip3 install Flask &> /dev/null
sudo pip3 show Flask 2> /dev/null

echo $"\nserver start"
sudo flask run --port=5555
