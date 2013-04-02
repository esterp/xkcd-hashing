# Overview

Search for data that hashes to the correct goal output hash. This script will randomly Skein1024 hash data and check the digest output to determine how many bits are different from the goal output. Whenever a "best" guess is found, it is submitted to the xkcd site, assuming your network connection is working.

Note: Quickstart script uses apt-get.

# Quickstart

	sudo ./quickstart.sh
	source venv/bin/activate

    python3 xkcd-hashing.py

Wait and hope you find a guess with a small diff (i.e. closer to the goal hash).

# Speed Test

	python3 xkcd-hashing.py time   # Outputs # hash/s






