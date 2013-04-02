# Overview

Search for data that hashes to the correct goal output hash. This script will randomly Skein1024 hash data and check the digest output to determine how many bits are different from the goal output. Whenever a "best" guess is found, it is submitted to the xkcd site, assuming your network connection is working.


# Quickstart 

## Ubuntu

	sudo ./quickstart.sh
	source venv/bin/activate

    python3 xkcd-hashing.py

    Note: Quickstart script uses apt-get.

## Windows/OS X

	Be sure you have Python 3 and pyskein. This version does not use gmpy so it may be easier for non-Linux users to setup. Note that its performance is not as great though.

	python3 otheros.py


Wait and hope you find a guess with a small diff (i.e. closer to the goal hash).

# Speed Test

	python3 xkcd-hashing.py time   # Outputs # hash/s






