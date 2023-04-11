#!/usr/bin/env python3

import os
import sys
import random

out_dir = sys.argv[1]
cc_file = sys.argv[2]
h_file = sys.argv[3]
randNum = random.randint(0, 54321)

def write_if_changed(path, contents):
    if not os.path.exists(path):
        with open(path, 'w') as fp:
            fp.write(contents)
        return

    with open(path) as old_fp:
        old_contents = old_fp.read()

    if contents != old_contents:
        with open(path, 'w') as fp:
            fp.write(contents)


write_if_changed(f'{out_dir}/{cc_file}', f'''\
#include "{h_file}"

const char *world() {{
    return "world-{randNum}";
}}
''')

write_if_changed(f'{out_dir}/{h_file}', '''\
const char *world();
''')
