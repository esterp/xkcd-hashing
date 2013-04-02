#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
	apt-get install build-essential
	apt-get install python3
	apt-get install python3-dev
	apt-get install python-virtualenv
	apt-get install libgmp3-dev
elif [[ "$unamestr" == 'Darwin' ]]; then
   brew install python3
   brew intall gmp
fi

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
