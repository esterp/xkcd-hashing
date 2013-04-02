# Overview

Search for data that hashes to the correct goal output hash. This script will randomly Skein1024 hash data and check the digest output to determine how many bits are different from the goal output. Whenever a "best" guess is found, it is submitted to the xkcd site, assuming your network connection is working.

Wait and hope you find a guess with a small diff (i.e. closer to the goal hash).


# Quickstart 

## Ubuntu/OS X (With Homebrew)

	sudo ./quickstart.sh
	source venv/bin/activate

    python3 main.py

## Windows/OS X (Without Homebrew)

Be sure you have Python 3.0+ and [PySkein](http://pythonhosted.org/pyskein/).

	python3 main.py

# Speed Test

	python3 main.py time   // Outputs # hash/s






