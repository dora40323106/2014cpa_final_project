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



#@+node:lee.20141224110313.61: * @file example2.py
#@@language python
#@@tabwidth -4
import cherrypy
import random
from std.asciisymbol import asciiImage

#@+others
#@+node:lee.20141223114246.41: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141223114246.42: *3* def init
    def __init__(self):
    	#你的名子
        self.name = '林祐生'
        # 你的學號
        self.number = '40323123'
        # 你的班級
        self.classes = 'nfu'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/smpss91341/cerrtpy.git'
        # 你的 bitbucket repository url
        self.bitbucket_repo_url = 'https://bitbucket.org/smpss91341/cerrtpy'
        # 你的 openshift app
        self.openshift_url = 'http://cheerpy-40323123.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 80), ('Project 8', 90), ('Project 9', 100)]
        # 你的照片 url
        self.photo_url = 'https://copy.com/RZo6bJEDWAsbHUbh'
        # 這裡是心得
        self.my_remark = """
       在 經 過 這 些 訓 練 ， 已 經 對 基 本 的 網 路 架 構 有 些 了 解 ， 雖 然 在 細 節 的 部 份 ， 還 是 有 些 問 題 存 在 ， 也 希 望 自 己 可 以 在 一 下 時 ， 自 己 建 立 一 個 網 站 使 用 ， 不
			     但 可 以 用 來 管 理 自 己 的 網 站 也 可 以 放 一 些 自 己 在 上 課 時 學 習 的 心 得 ， 說 不 定 到 畢 業 時 ， 這 個 網 站 變 成 我 的 學 習 歷 程 ， 也 從 完 全 不 會 到 ， 完 全 的 理 解 、 分 析 ，
		             期 末 了 ， 在 這 麼 短 的 學 期 中 ， 把 一 些 網 路 的 架 構 利 用 p y t h o n 建 立 出 來 ， 除 了 自 己 很 有 心 得 以 外 ， 也 看 到 了 會 不 一 定 = 會 教 人 , 也 是 因 為 這 樣 ， 漸 漸 我 想 成 為 可 以 
 			     指 導 人 的 小 老 師 ， 也 希 望 自 己 可 以 為 未 來 放 上 一 點 希 望 ， 把 自 己 成 長 茁 壯 ， 變 成 屹 立 不 搖 的 大 樹 ， 成 樹 蔭 給 後 面 的 人 乘 涼 。
        """

    #@+node:lee.20141223114246.43: *3* def use_template
    def use_template(self, content):
        above = """
        <!DOCTYPE html>
    <html lang="en">
    <head>

      <!-- Basic Page Needs
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <meta charset="utf-8">
      <title>title</title>
      <meta name="description" content="">
      <meta name="author" content="">

      <!-- Mobile Specific Metas
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- FONT
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <style>
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 300;
      src: local('Raleway Light'), local('Raleway-Light'), url(/static/font/Raleway300.woff) format('woff');
    }
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 400;
      src: local('Raleway'), url(/static/font/Raleway400.woff) format('woff');
    }
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 600;
      src: local('Raleway SemiBold'), local('Raleway-SemiBold'), url(/static/font/Raleway600.woff) format('woff');
    }
    </style>

      <!-- CSS
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <link rel="stylesheet" href="/static/css/normalize.css">
      <link rel="stylesheet" href="/static/css/skeleton.css">
      <link rel="stylesheet" href="/static/css/custom.css">
      <!-- Favicon
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <link rel="icon" type="image/png" href="/static/images/favicon.png" />

    </head>
    <body>

      <!-- Primary Page Layout
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <!-- .container is main centered wrapper -->
    <div class="container">
    """
        below = """
    </div>
    <footer class="center">
      2014 Computer Programming
    </footer>

    <!-- Note: columns can be nested, but it's not recommended since Skeleton's grid has %-based gutters, meaning a nested grid results in variable with gutters (which can end up being *really* small on certain browser/device sizes) -->

    <!-- End Document
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    </body>
    </html>
    """
        return above + self.generate_nav(self.link()) + content + below
    #@+node:lee.20141223114246.44: *3* def generate_nav
    def generate_nav(self, anchors):
        above_side = """
        <div class="row">
            <div class="nav twelve columns">
                <input type="checkbox" id="toggle" />
                <div>
                    <label for="toggle" class="toggle" data-open="Main Menu" data-close="Close Menu" onclick></label>
                    <ul class="menu">
        """

        content = ''
        for link, name in anchors:
            content += '<li><a href="' + link + '">' + name + '</a></li>'

        below_side = """
                    </ul>
                </div>
            </div>
        </div>
        """
        return above_side + content + below_side
    #@+node:lee.20141223114246.45: *3* def generate_form_page
    def generate_form_page(self, form='', output=''):
        content = """
            <div class="content">
            <div class="row">
              <div class="one-half column">
                %s
              </div>
              <div class="one-half column">
                <div class="output u-full-width">
                  <p>Output:</p>
                  <p>
                    %s
                  </p>
                </div>
              </div>
            </div>
          </div>
        """%(form, output)
        return self.use_template(content)
    #@+node:lee.20141223114246.55: *3* def generate_headline_page
    def generate_headline_page(self, headline, output):
        content = """
      <div class="content">
        <div class="row">
          <div class="headline center">%s</div>
          <div class="twelve columns">
            <p>%s</p>
          </div>
        </div>
      </div>
        """ % (headline, output)
        return self.use_template(content)
    #@+node:lee.20141223114246.46: *3* def generate_personal_page
    def generate_personal_page(self, data=None):
        if data is None:
            return ''

        # check data have all we need, if the key not exist, use empty string
        must_have_key = ('photo_url', 'name', 'ID', 'class', 'evaluation')
        for key in must_have_key:
            data[key] = data.get(key, '')


        if 'evaluation' in data:
            table_content = ''
            for projectName, score in data['evaluation']:
                table_content += """<tr><td>%s</td><td>%s</td>"""%(projectName, score)
            data['evaluation'] = table_content
        content = """
    <div class="content">
    <div class="row">
      <div class="one-half column">
        <div class="headline">
          About Me
        </div>
        <div class="photo">
          <img src="{photo_url:s}" alt="photo">
        </div>
        <div class="meta">
          <ul>
            <li>Name: {name:s}</li>
            <li>ID NO. : {ID:s}</li>
            <li>Class: {class:s}</li>
          </ul>
        </div>
      </div>
      <div class="one-half column">
        <div class="headline">
          Self Evaluation
        </div>
        <div>
          <table class="u-full-width">
            <thead>
              <tr>
                <th>Project Name</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
                {evaluation:s}
            </tbody>
          </table>

        </div>
      </div>
    </div>
    </div>
        """.format(**data)
        return self.use_template(content)
    #@+node:lee.20141223114246.47: *3* def link
    def link(self):
        aviable_link = [("index", "HOME"), ("remark", "心得"), (self.openshift_url, "個人 openshift app"),(self.github_repo_url, "個人 github repo"), (self.bitbucket_repo_url, "個人 bitbucket repo"), ('/', 'back to list')]
        return aviable_link
    #@+node:lee.20141223114246.54: *3* def remark
    @cherrypy.expose
    def remark(self):
        # 這裡是心得
        # generate_headline_page(你的標題, 你的內容)
        return self.generate_headline_page("REMARK", self.my_remark)
    #@+node:lee.20141223114246.48: *3* def index
    @cherrypy.expose
    def index(self):
        # 這裡是首頁
        data = {
            'name':self.name,
            'ID':self.number,
            'class':self.classes,
            'evaluation': self.evaluation,
            'photo_url':self.photo_url,
        }
        return self.generate_personal_page(data)

    #@-others
#@-others
#@-leo
