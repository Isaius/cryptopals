## To test functions
from codecrypto import *

## MAIN PROGRAM
input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'

result = fixed_XOR(input1, input2)
print(result)