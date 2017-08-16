import sys, re
from handlers import *
from util import *
from rules import *

class Parser(object):
    '''
    語法分析器讀取文本文件、應用規則并且控制處理程序
    '''
    def __init__(self, handler):
        self.handler = handler
        self.rules = []#規則列表
        self.filters = []#過濾器列表

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')

class BasicTextParser(Parser):
    '''
    在構造函數中增加規則和過濾起的具體語法分析器
    '''
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRender()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
















