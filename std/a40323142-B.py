#@+leo-ver=5-thin
#@+node:lee.20141215164031.94: * @file example.py
#@@language python
#@@tabwidth -4
#@+<<decorations>>
#@+node:lee.20141215164031.95: ** <<decorations>>
import cherrypy
import random
from std.asciisymbol import asciiImage
from wsgi import env
#@-<<decorations>>

#@+others
#@+node:lee.20141215164031.96: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141221203113.62: *3* def __init__
    def __init__(self):
        self.name = '陳柏曄'
        self.number = '40323142'
        self.classes = '機械設計一年甲班'

        self.github_repo_url = 'https://github.com/mdeta/2014-cp-ab'

        self.evaluation = [('專案 7', 75), ('專案 8', 70), ('專案t 9', 65)]
        self.photo_url = 'https://copy.com/U44kSdtBp2yziELR'
    #@+node:lee.20141215164031.97: *3* def get_nav
    def get_nav(self):
        """
        取得 nav link
        """
        #(URL 路徑, anchor name)
        anchors = [('index', '首頁'), ('guessForm', '猜數字'), ('multipliedTable', '乘法表'), ('asciiForm', '使用圖案印出字'), (self.github_repo_url, 'github倉儲'), ('/', '回到目錄')]
        return anchors
    #@+node:lee.20141215164031.98: *3* def index
    @cherrypy.expose
    def index(self):
        """
        個人首頁
        """
        # 取得模板
        tmpl = env.get_template('personal_page.html')
        # 設定額外變數
        extra_content = {
            'title': 'personal page -' + self.name,
            'photo_url': self.photo_url,
            'std_name': self.name,
            'ID':self.number,
            # class 在 mako 底下是關鍵字
            'classes':self.classes,
            'anchors':self.get_nav(),
            'self_evaluations':self.evaluation
        }
        # 宣染
        return tmpl.render(**extra_content)

    #@+node:lee.20141215164031.99: *3* def guessForm
    @cherrypy.expose
    def guessForm(self, guessNumber=None):
        
        # get template
        tmpl = env.get_template('form.html')
        
        form = """
        <form action="" method="get">
          <label for="guessNumber">猜數字(1~99)</label>
          <input name="guessNumber" type="text">
          <input type="submit" value="Send" class="button button-primary">
        </form>
        """
        
        # set common content
        extra_content = {'title':'guessform', 'form':form, 'anchors':self.get_nav()}
        
        # get count from session
        count = cherrypy.session.get("count", None)
        # if is None, it mean it does not exist
        if not count:
            # create one
            count = cherrypy.session["count"] = 0

        # get answer from session
        answer = cherrypy.session.get("answer", None)
        # if is None, it mean it does not exist
        if not answer:
            # create one
            answer = cherrypy.session["answer"] = random.randint(1, 100)


        # 設定在哪種情況下該回傳哪種訊息
        message = {
            "welcome": "從1到99猜一個數字吧!!",
            "error": "必須要輸入數字, 你的輸入是 %s" % str(guessNumber),
            "successful": "答對了!答案是 %d , 總共猜了 %d" % (answer, count),
            "smaller": "比 %s 小,猜了 %d 次" % (str(guessNumber), count),
            "bigger": "比 %s 大,猜了 %d 次" % (str(guessNumber), count),
        }

        #假如 guessNumber is None, 表示是第一次進來, 或是未傳值
        if guessNumber is None:
            extra_content['output'] = message['welcome']
            return tmpl.render(**extra_content)
        # 其他, 表示要開始處理 guessNumber
        else:
            # convert guessNumber to int
            try:
                guessNumber = int(guessNumber)
            except:
                # if fail
                # throw error
                extra_content['output'] = message['error']
                return tmpl.render(**extra_content)

            # convert ok, make count plus one, everytime
            cherrypy.session["count"] += 1

            if guessNumber == answer:
                # clear session count and answer
                del cherrypy.session["count"]
                del cherrypy.session["answer"]
                # throw successful
                extra_content['form'] = ''
                extra_content['output'] = message["successful"]+'<a href="guessForm">在玩一次</a>'
            elif guessNumber > answer:
                # throw small than guessNumber
                extra_content['output'] = message["smaller"]
            else:
                # throw bigger than guessNumber
                extra_content['output'] = message["bigger"]
            return tmpl.render(**extra_content)
    #@+node:lee.20141215164031.100: *3* def multipliedTable
    @cherrypy.expose
    def multipliedTable(self, first=None, second=None):
        # get template
        tmpl = env.get_template('form.html')
        # set up messages
        message = {
            'error': '你必須輸入正確的數值',
            'welcome': '輸入你想要的99乘法表',
        }
        # set up form
        # two variable
        # first, second
        form = """
        <form action="" method="post">
          <label for="first">第一個數字(整數)</label>
          <input name="first" type="text">
          <label for="first">第二個數字(整數)</label>
          <input name="second" type="text">
          <input type="submit" value="Send" class="button button-primary">
        </form>
        """

        # set extra content variable
        extra_content = {
            'title': 'multipliedTable', 'form': form, 'anchors': self.get_nav()}

        # if first and second parameter is None
        # set output to welcome
        if first is None and second is None:
            extra_content['output'] = message.get('welcome')
            return tmpl.render(**extra_content)
        # try convert to integer
        try:
            first = int(first)
            second = int(second)
        except:
            #raise error
            extra_content['output'] = message.get('error')
            return tmpl.render(extra_content)
        # start process
        output = ''
        for f in range(1, first + 1):
            for s in range(1, second + 1):
                output += str(f) + '*' + str(s) + '=' + str(f * s) + '<br/>'
        # update extra content
        extra_content['output'] = '<p>' + output + '</p>'
        # render
        return tmpl.render(**extra_content)
    #@+node:lee.20141215164031.101: *3* def asciiForm
    @cherrypy.expose
    def asciiForm(self, text=None):
        # get template
        tmpl = env.get_template('form.html')
        # set up messages
        messages = {
            'welcome': '輸入你想要印的數字及英文字母吧',
        }
        # set up form
        # variable text
        form = """
        <form method="get" action="">
            <label for="text">要印...</label>
            <input type="text" name="text" />
            <input type="submit" value="Send" class="button button-primary">
        </form>
        """
        # set up extra content
        extra_content = {
            'title': 'asciiForm', 'form': form,
            'anchors': self.get_nav()
        }

        # if text is None, set output to welcome
        if text is None:
            extra_content['output'] = messages.get('welcome')
        # if not None, start process
        else:
            # use module asciisymol's asciiImage function
            # one arg, input type string
            extra_content['output'] = asciiImage(text)
        # render
        return tmpl.render(**extra_content)
    #@-others
#@-others
#@-leo
