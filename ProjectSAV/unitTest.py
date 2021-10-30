# -*- coding: utf-8 -*-
"""
This is the Sebastian Aponte Vivas sample project.

Unit test
"""

import subprocess

# Types of possible user inputs
inputs = [139, 'aws', '1E', '@', '', '139', [139,170], {139,170}, 139.5, 1.39, '1.39', '139.5', 17000]

# For each input in list print the function result
for inpt in inputs:
    process = subprocess.Popen("python palyersAddInpt.py %s " % inpt, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("\nInput: {}".format(inpt))
    for outLine in process.stdout.readlines():
        print(outLine)
    retval = process.wait()


