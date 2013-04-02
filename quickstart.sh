#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

apt-get install build-essential
apt-get install python3
apt-get install python3-dev
apt-get install python-virtualenv
apt-get install libgmp3-dev

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
