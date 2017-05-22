# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

pwRegex = re.compile(r'''(
        ^(?=.*[0-9]+)
        (?=.*[a-z]+)
        (?=.*[A-Z]+)
        .{8,}
        $
        )''', re.VERBOSE)

def checkPW():
    p = input('Please enter a password: ')
    mo = pwRegex.search(p)
    if (not mo):
        print ('Password does not meet criteria.')
        return False
    else:
        print ('Got it!')
        return True

checkPW()