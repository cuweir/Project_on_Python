import sys, re
from util import *

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):#sys.stdin文件流
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)#re.sub():將block中的所有*xxx*匹配項用<em>xxx</em>替換。
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
