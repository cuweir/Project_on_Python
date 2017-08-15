import sys, re
from util import *

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):#sys.stdin什麽意思
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)#re.sub()啥玩意
    if title:
        print ('<h1>')
        print (block)
        print ('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
    print('</body></html>')
