# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name, S.



#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = []
    spl = s.split(" ")
    for i in spl:
        words.append(i.capitalize())
    done = " ".join(words)
    return done
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
