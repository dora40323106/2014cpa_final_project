#@+leo-ver=5-thin
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
        self.name = '雷英祺'
        # 你的學號
        self.number = '40323151'
        # 你的班級
        self.classes = 'nfu'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/dora40323106/2014cpa_final_project'
        # 你的 bitbucket repository url
        self.bitbucket_repo_url = ''
        # 你的 openshift app
        self.openshift_url = 'http://asdasd-40323119.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 60), ('Project 8', 70), ('Project 9', 65)]
        # 你的照片 url
        self.photo_url = 'data:image/jpeg;base64,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'
        # 這裡是心得
        self.my_remark = """
        這門課真的是各種障礙,希望未來可以更加學習，及向上學習的新永不熄滅。
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
