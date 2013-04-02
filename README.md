# Overview

Search for data that hashes to the correct goal output hash. This script will randomly Skein1024 hash data and check the digest output to determine how many bits are different from the goal output. Whenever a "best" guess is found, it is submitted to the xkcd site, assuming your network connection is working.

# Quickstart

	sudo ./quickstart.sh
	source venv/bin/activate

    python3 xkcd-hashing.py

Wait and hope you find a guess with a small diff (i.e. closer to the goal hash).

TODO list
+ Scrape the current MIT score
+ Automatically POST the data when found
+ Use the random bytes, right now the bit differences calculated for these are not the same as those calculated on the xkcd website for some reason.
+ Autodeployment on Amazon EC2
+ multithreading?

I might do some of these eventually, if psets magically get done...








