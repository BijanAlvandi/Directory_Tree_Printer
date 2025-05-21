import os
import sys
import argparse
from pathlib import Path
import logging

DEFAULT_FOLLOW_SYMLINKS = False
DEFAULT_MAX_DEPTH = None
DEFUALT_SHOW_HIDDEN = False

parser = argparse.ArgumentParser(description='Directory Tree Printer')
parser.add_argument('--all', action='store_true', help='Limit recursion depth')
parser.add_argument('--max-depth', type=int, default=DEFAULT_MAX_DEPTH, help='Limit recursion depth')
parser.add_argument('--follow-symlinks', action='store_true', default=DEFAULT_FOLLOW_SYMLINKS)

args = parser.parse_args()





