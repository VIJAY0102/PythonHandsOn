#!/usr/bin/env python

import os

os.system('touch file.txt ; env > file.txt ; chmod 777 file.txt ')
print("File Created")
