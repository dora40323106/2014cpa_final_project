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
        self.name = 'Ling you-sheng'
        self.number = '40323123'
        self.classes = 'NFU-MDE-A'
        self.github_repo_url = 'http://cheerpy-40323123.rhcloud.com/'
        self.evaluation = [('Project 7', 90), ('Project 8', 90), ('Project 9', 100)]
        self.photo_url = 'https://copy.com/RZo6bJEDWAsbHUbh'
        self.experience = """在 經 過 這 些 訓 練 ， 已 經 對 基 本 的 網 路 架 構 有 些 了 解 ， 雖 然 在 細 節 的 部 份 ， 還 是 有 些 問 題 存 在 ， 也 希 望 自 己 可 以 在 一 下 時 ， 自 己 建 立 一 個 網 站 使 用 ， 不
			     但 可 以 用 來 管 理 自 己 的 網 站 也 可 以 放 一 些 自 己 在 上 課 時 學 習 的 心 得 ， 說 不 定 到 畢 業 時 ， 這 個 網 站 變 成 我 的 學 習 歷 程 ， 也 從 完 全 不 會 到 ， 完 全 的 理 解 、 分 析 ，
		             期 末 了 ， 在 這 麼 短 的 學 期 中 ， 把 一 些 網 路 的 架 構 利 用 p y t h o n 建 立 出 來 ， 除 了 自 己 很 有 心 得 以 外 ， 也 看 到 了 會 不 一 定 = 會 教 人 , 也 是 因 為 這 樣 ， 漸 漸 我 想 成 為 可 以 
 			     指 導 人 的 小 老 師 ， 也 希 望 自 己 可 以 為 未 來 放 上 一 點 希 望 ， 把 自 己 成 長 茁 壯 ， 變 成 屹 立 不 搖 的 大 樹 ， 成 樹 蔭 給 後 面 的 人 乘 涼   !。"""
    #@+node:lee.20141215164031.97: *3* def get_nav
    def get_nav(self):
        """
        取得 nav link
        """
        #(URL 路徑, anchor name)
        anchors = [('index', 'home'), ('guessForm', '猜數字'), ('multipliedTable', '乘法表'), ('asciiForm', '使用圖案印出字'), (self.github_repo_url, 'github repository'), ('/', 'back to list')]
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

#@+node:lee.20141224110313.61: * @file example2.py
#@@language python
#@@tabwidth -4
import cherrypy
import random
from std.asciisymbol import asciiImage

#@+others
#@+node:lee.20141223114246.41: ** class Application

