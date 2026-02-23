#!/usr/bin/env python3
"""Simple script that prints numbers from 1 to 20, aligned right with multiplication."""

for i in range(1, 21):
    print(str(i * i).rjust(20))
