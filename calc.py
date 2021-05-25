#!/usr/bin/env python3
import logging
import os
import re
import readline
import types

import numbers
import math
import cmath
import decimal as decimals
import fractions
import random
import statistics

from numbers import *
from math import *
from cmath import *
from decimal import *
from fractions import *
from random import *
from statistics import *

false=False
true=True
none=None
null=None
j=1j
i=j
infi=infj
nani=nanj

for k, v in list(globals().items()):
    if not "__" in k and not k.isupper() and not k.islower():
        globals()[k.lower()] = v

for n in dir(math):
    if "__" in n:
        continue
    elif n in dir(cmath) and isinstance(getattr(math, n), types.BuiltinFunctionType):
        globals()[n] = lambda *x, n=n: (lambda r=getattr(cmath, n)(*x): r.real if r.imag == 0 else r)()

try:
    while True:
        calc = input("\033[95m> \033[39m").strip()
        if calc == "" or calc[0] == "#":
            continue
        elif (calc == "exit()"
            or calc == "exit"
            or calc == "quit()"
            or calc == "quit"
            or calc == "q"):
            exit()
        try:
            calc = re.sub(r'([0-9]+)i', r'\1j', calc)
            try:
                res = eval(calc)
            except Exception:
                res = eval(calc.lower())

            if res == "exit":
                exit()
            else:
                if isinstance(res, complex):
                    if res.imag != 0:
                        print("complex: {0} + {1}i".format(res.real, res.imag))
                        continue
                    else:
                        res = res.real 

                if isinstance(res, bool):
                    print("bool: {0}\thex: 0x{0:X}".format(res).lower())
                    continue

                if isinstance(res, float):
                    if isnan(res) or isinf(res) or res != floor(res):
                        print("float: {0:f}".format(res))
                        continue
                    else:
                        res = floor(res)

                if isinstance(res, int):
                    print("dec: {0:d}\thex: 0x{0:X}".format(floor(res)))
                    continue

                if isinstance(res, types.BuiltinFunctionType):
                    print("python built-in function: {0}".format(res.__name__))
                    continue

                if res == None:
                    print("null")
                    continue

                print("{0}: {1}".format(res.__class__.__name__, res))
                continue

        except Exception as err:
            func_r = r"^[a-zA-Z_][a-zA-Z0-9_]*"
            if re.match(func_r + r"$", calc) or re.match(func_r + r" ", calc):
                ret = os.system(calc)
                if ret != 0:
                    print("ret: {0:d}\thex: 0x{0:X}".format(ret))
            else:
                print("error: {0}".format(err))

except KeyboardInterrupt:
    print('\033[3m\b keyboard interrupt\033[0m')

except EOFError:
    print('\033[3m\b eof\033[0m')
    exit()
