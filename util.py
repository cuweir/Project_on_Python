#文本塊生成器
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():#strip()函數：移除字符串頭尾的指定字符，默認為空格。返回新字符串。
            block.append(line)
        elif block:
            yield ''.join(block).strip()#join()函數：將括號内的字符串block用''連接起來。返回新字符串。
            block = []
