import re
from docassemble.base.util import *

def check_nric (string):
  string = string.upper()
  if not re.match(r'[S][0-9]{7}[A-J]', string):    
    validation_error ('Invalid NRIC format.')
  else:
    x = (2 * int(string[1]) + 7 * int(string[2]) + 6 * int(string[3]) + 5 * int(string[4]) + 4 * int(string[5]) + 3 * int(string[6]) + 2 * int(string[7])) % 11 
    if x == 0 and string[8] == ('J') or x == 1 and string[8] == ('Z') or x == 2 and string[8] == ('I') or x == 3 and string[8] == ('H') or x == 4 and string[8] == ('G') or x == 5 and string[8] == ('F') or x == 6 and string[8] == ('E') or x == 7 and string[8] == ('D') or x == 8 and string[8] == ('C') or x == 9 and string[8] == ('B') or x == 10 and string[8] ==('A'): 
      return True
    else:
      validation_error ('Invalid NRIC format.')