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
    #@+node:lee.20141221203113.62: *37* def __init__
    def __init__(self):
        self.name = '許兆毅'
        self.number = '40323136'

        self.classes = '四機械設計一甲'
        self.github_repo_url = 'https://github.com/mdeta/2014cp'

        self.evaluation = [('Project1 ', 75), ('Project2 ', 70), ('Project3 ', 75)]
        self.photo_url = 'https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-xap1/v/t1.0-9/1912386_1587965194767590_2203672651142298479_n.jpg?oh=eb1cdbcbda6efdff847bc90db4d758bc&oe=54F97881&__gda__=1429298525_e3bec1862b305e36ed08d4b455c7f5aa'
    def get_nav(self):
        """
        取得 nav link
        """
        #(URL 路徑, anchor name)
        anchors = [('index', 'home'), ('guessForm', '猜數字'), ('multipliedTable', '乘法表'), ('asciiForm', '使用圖案印出字'), (self.github_repo_url, 'github repository'), ('/', 'back to list')]
        return anchors
    #@+node:lee.20141215164031.98: *37* def index
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
          <label for="guessNumber">Guess Number(1~99)</label>
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
            "welcome": "guess a number from 1 to 99",
            "error": "must input a number, your input is %s" % str(guessNumber),
            "successful": "correct! your input is %s answer is %d total count %d" % (str(guessNumber), answer, count),
            "smaller": "smaller than %s and total count %d" % (str(guessNumber), count),
            "bigger": "bigger than %s and total count %d" % (str(guessNumber), count),
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
                extra_content['output'] = message["successful"]+'<a href="guessForm">play again</a>'
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
            'error': 'you must input correct type data.',
            'welcome': 'Welcome to multiplied table page.',
        }
        # set up form
        # two variable
        # first, second
        form = """
        <form action="" method="post">
          <label for="first">first number(an integer)</label>
          <input name="first" type="text">
          <label for="first">second number(an integer)</label>
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
            'welcome': 'welcome to ascii form',
        }
        # set up form
        # variable text
        form = """
        <form method="get" action="">
            <label for="text">Say....</label>
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
