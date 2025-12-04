#!/usr/bin/env python3

import sys
import os
sys.dont_write_bytecode = True

if len(sys.argv) == 1:
  print('usage: ./main.py [day] [--test]')
  for day in os.listdir(os.getcwd()):
    if os.path.isdir(os.path.join(os.getcwd(), day)):
      print(f'  {day}')
  exit(1)

if len(sys.argv) == 2:
  sys.INPUTFILE = f'{sys.argv[1]}/real.input'

if len(sys.argv) == 3 and sys.argv[2] == '--test':
  sys.INPUTFILE = f'{sys.argv[1]}/mini.input'

__import__(f'{sys.argv[1]}.solution', globals())