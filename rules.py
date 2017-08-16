class Rule(object):
    '''
    所有規則的基類
    '''
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    '''
    標題佔一行，最多70字符，不以冒號結尾。
    '''
    type = 'heading'#被繼承自Rule類的action方法使用
    def condition(self, block):#條件函數檢查
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    '''
    題目是文檔的第一個塊，但前提是它是大標題。
    '''
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first:
            return False
        self.first = False#missed in the first execution
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
    '''
    列表是以連字符開始的段落，作爲格式化的一部分，要移除連字符。
    '''
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    '''
    列表從不是列表項的塊和隨後的列表項之間。在最後一個連續列表項之後結束。
    '''
    type = 'list'
    inside = False
    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    '''
    段落衹是其他規則沒有覆蓋到的塊
    '''
    type = 'paragraph'
    def condition(self, block):
        return True





















