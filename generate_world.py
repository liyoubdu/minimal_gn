#!/usr/bin/env python3

import os
import sys
import random
import time

out_dir = sys.argv[1]
cc_file = sys.argv[2]
h_file = sys.argv[3]

random.seed(time.time())
randNum = random.randint(0, 54321)

def write_if_changed(path, contents):
  with open(path, 'w') as fp:
    fp.write(contents)
  return


write_if_changed(f'{out_dir}/{h_file}', f'''\
const char *world() {{
    return "world-{randNum}";
}}
''')

