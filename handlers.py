class Handler(object):
    """
    處理從Parser調用的方法對象。
    該解析器會在每個塊的開始部分調用start()和end()方法，使用合適的塊名作爲參數。
    sub()方法會用正則表達式替換中。當時用了'emphasis'這樣的名字調用時，他會返回合適的替換函數。
    """
    def callback(self, prefix, name, *args):#查找一個正確的方法
        method = getattr(self, prefix+name, None)#
        if callable(method):#可調用
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result   #modified
        return substitution

class HTMLRender(Handler):
    '''
    用於生成HTML的具體處理程序
    HTMLRender内的方法可以通過超類處理程序的start()、end()和sub()方法來訪問。
    實現了用於HTML文檔的基本標簽
    '''
    def start_document(self):
        print('<html><head><title>...</title></head><body>')    #modified

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):#unordered list
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)
