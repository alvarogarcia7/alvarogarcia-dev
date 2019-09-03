#!/usr/bin/env python
from subprocess import call
import sys

input_path = sys.argv[1]

paths = input_path.split("/")

if (paths[0] != "themes" or paths[1] != "hugo-serif-theme"):
  raise ValueError("Can only be executed for paths starting with 'themes/hugo-serif-theme'")

intermediate_paths = "/".join(paths[2:-1])

call(["mkdir", "-p", intermediate_paths])
call(["cp", input_path, intermediate_paths])

