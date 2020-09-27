#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "neg2led@github"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os
import time
import argparse
import pigpio

NUM_GPIO=19
PWM_FREQ=1000

pi = pigpio.pi()

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def main(args):
    """ entrypoint """
    print("hello world")
    print(args)
    print(os.environ)

    if not pi.connected:
        exit()

    PWM_DUTY=scale(args.brightness, (0, 255), (0, 1000000))

    pi.hardware_PWM(NUM_GPIO, PWM_FREQ, PWM_DUTY)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument(
        "brightness",
        default=255,
        help="Desired brightness (0-255)"
        )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)