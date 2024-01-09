import os
import sys
from converter import convertFile

sys.path.append('sys')

op, iFile, toLang = sys.argv[1:4]
match op:
    case 'convert':
        toCode = convertFile(iFile, toLang)
        print(toCode)
    # case 'run':
        # toCode = convertFile(iFile, toLang)
        # eval(toCode)
        # run(oFile, toLang)


print('finished!')

"""
def run(lang):
    if to
    os.system(iFile)
"""


