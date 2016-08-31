#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pokemon GO Device Database
Copyright (c) 2016 vosk <https://github.com/vosk>
"""

import json
import sys

filename="devices.json"
try:
    with open(filename, 'rb') as data:
        t=json.load(data)
        print(t)
except ValueError as e:
    print('Error with configuration file')
    print(e)
    sys.exit(-1)
finally:
    print("Its not THAT broken")
