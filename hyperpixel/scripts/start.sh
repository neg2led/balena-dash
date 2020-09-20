#!/bin/bash

# run hyperpixel4-init
/usr/bin/hyperpixel4-init

# Start pigpiod
pigpiod

# start python script
/usr/bin/env python3 /usr/src/hyperpixel-backlight.py