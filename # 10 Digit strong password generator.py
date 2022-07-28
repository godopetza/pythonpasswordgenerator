# 10 Digit strong password generator
# Code by Godopetza

import numbers
import random
from symtable import Symbol

lower_cases = "abcdefghijklmnopqrstvwxyz"
upper_cases = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
number = "012456789"
symbols = "+!@#$%*/\?&"

use_as = lower_cases + upper_cases + symbols
# change length here if needed
passwordlength = 10

password = "".join(random.sample(use_as, passwordlength))

print("Generated Password : "+ password)