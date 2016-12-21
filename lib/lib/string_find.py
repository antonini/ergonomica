#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint's name standards are insane
# pylint: disable=invalid-name

"""
[lib/lib/string_find.py]

Defines the "string_find" command.
"""

import os
import fnmatch

verbs = {}

def string_find(env, args, kwargs):
    """[DIR=.] {name:PATTERN=*}@Finds all lines in files in DIR (recursively) that match PATTERN."""
    try:
        pattern = kwargs["name"]
    except KeyError:
        pattern = "*"
    try:
        path = args[0]
    except IndexError:
        path = env.directory
    result = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if fnmatch.fnmatch(os.path.join(root, dir), pattern):
                result.append(os.path.join(root, dir))
        for name in files:
            opened_file = open(os.path.join(root, name), "r").readlines()
            for x in range(len(opened_file)):
                if pattern in opened_file[x]:
                    result.append(os.path.join(root, name) + ", line %s \n" % x + opened_file[x])
    return list(set(result))

verbs["string_find"] = string_find
verbs["sfind"] = string_find
