#@+leo-ver=5-thin
<<<<<<< HEAD
#@+node:lee.20141221203113.46: * @file example1.py
=======
#@+node:lee.20141224110313.61: * @file example2.py
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
#@@language python
#@@tabwidth -4
import cherrypy
import random
from std.asciisymbol import asciiImage

#@+others
<<<<<<< HEAD
#@+node:lee.20141221203113.47: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141221203113.61: *3* def init
    def __init__(self):
        self.name = '廖佑珊'
        self.number = '40323107'
        self.classes = 'nfu'
        self.github_repo_url = 'https://github.com/mdeta/2014-cp-ab'
        self.evaluation = [('Project 7', 60), ('Project 8', 60), ('Project 9', 60)]
        self.photo_url = 'http://placekitten.com/g/350/300'
        
    #@+node:lee.20141221203113.53: *3* def use_template
=======
#@+node:lee.20141223114246.41: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141223114246.42: *3* def init
    def __init__(self):
    	#你的名子
        self.name = '廖佑珊'
        # 你的學號
        self.number = '40323107'
        # 你的班級
        self.classes = 'nfu'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/dora40323106/2014cpa_final_project'
        # 你的 bitbucket repository url
        self.bitbucket_repo_url = ''
        # 你的 openshift app
        self.openshift_url = 'http://cpa-nfutaiwan.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 80), ('Project 8', 90), ('Project 9', 100)]
        # 你的照片 url
        self.photo_url = 'http://placekitten.com/g/350/300'
        # 這裡是心得
        self.my_remark = """
        Computer Programming is good course
        """


    #@+node:lee.20141223114246.43: *3* def use_template
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
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
<<<<<<< HEAD
    #@+node:lee.20141221203113.58: *3* def generate_nav
=======
    #@+node:lee.20141223114246.44: *3* def generate_nav
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
    def generate_nav(self, anchors):
        above_side = """
        <div class="row">
            <div class="nav twelve columns">
                <input type="checkbox" id="toggle" />
                <div>
                    <label for="toggle" class="toggle" data-open="Main Menu" data-close="Close Menu" onclick></label>
                    <ul class="menu">
        """
<<<<<<< HEAD
        
        content = ''
        for link, name in anchors:
            content += '<li><a href="' + link + '">' + name + '</a></li>'
        
=======

        content = ''
        for link, name in anchors:
            content += '<li><a href="' + link + '">' + name + '</a></li>'

>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
        below_side = """
                    </ul>
                </div>
            </div>
        </div>
        """
        return above_side + content + below_side
<<<<<<< HEAD
    #@+node:lee.20141221203113.59: *3* def generate_form_page
=======
    #@+node:lee.20141223114246.45: *3* def generate_form_page
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
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
<<<<<<< HEAD
    #@+node:lee.20141221203113.60: *3* def generate_personal_page
    def generate_personal_page(self, data=None):
        if data is None:
            return ''
        
=======
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

>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
        # check data have all we need, if the key not exist, use empty string
        must_have_key = ('photo_url', 'name', 'ID', 'class', 'evaluation')
        for key in must_have_key:
            data[key] = data.get(key, '')
<<<<<<< HEAD
                
                 
=======


>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
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
<<<<<<< HEAD
    #@+node:lee.20141221203113.55: *3* def link
    def link(self):
        aviable_link = [("index", "HOME"),("asciiForm", "使用圖案印出字"), ("guessForm", "猜數字"), (self.github_repo_url, "github repo"), ("weblink", "Creo web/link"), ("/", "back to list")]
        return aviable_link
    #@+node:lee.20141221203113.49: *3* def index
    @cherrypy.expose
    def index(self):
=======
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
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
        data = {
            'name':self.name,
            'ID':self.number,
            'class':self.classes,
            'evaluation': self.evaluation,
            'photo_url':self.photo_url,
        }
        return self.generate_personal_page(data)
<<<<<<< HEAD
    #@+node:lee.20141221203113.51: *3* def asciiForm
    @cherrypy.expose
    def asciiForm(self, text=None):
        # form, action to asciiOutput
        # set up messages
        messages = {
            'welcome': 'welcome to ascii form',
        }
        content = """
        <form method="get" action="">
            <label for="text">Say....</label>
            <input type="text" name="text" />
            <input type="submit" value="Send" class="button button-primary">
        </form>
        """
        output = ''
        # if text is None, set output to welcome
        if text is None:
            output = messages.get('welcome')
        # if not None, start process
        else:
            # use module asciisymol's asciiImage function
            # one arg, input type string
            output = asciiImage(text)
        return self.generate_form_page(content, output)
    #@+node:lee.20141221203113.54: *3* def guessForm
    @cherrypy.expose
    def guessForm(self, guessNumber=None):
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

        form = """
        <form action="" method="get">
          <label for="guessNumber">Guess Number(1~99)</label>
          <input name="guessNumber" type="text">
          <input type="submit" value="Send" class="button button-primary">
        </form>
        """

        message = {
            "welcome": "guess a number from 1 to 99",
            "error": "must input a number, your input is %s" % str(guessNumber),
            "successful": "correct! your input is %s answer is %d total count %d" % (str(guessNumber), answer, count),
            "smaller": "smaller than %s and total count %d" % (str(guessNumber), count),
            "bigger": "bigger than %s and total count %d" % (str(guessNumber), count),
        }

        if guessNumber is None:
            return self.generate_form_page(form, message["welcome"])
        else:
            # convert guessNumber to int
            try:
                guessNumber = int(guessNumber)
            except:
                # if fail
                # throw error
                return self.generate_form_page(form, message["error"])

            # convert ok, make count plus one, everytime
            cherrypy.session["count"] += 1

            if guessNumber == answer:
                # clear session count and answer
                del cherrypy.session["count"]
                del cherrypy.session["answer"]
                # throw successful
                return self.generate_form_page(form,  message["successful"] + '</h1><a href="guessForm">play again</a>')
            elif guessNumber > answer:
                # throw small than guessNumber
                return self.generate_form_page(form, message["smaller"])
            else:
                # throw bigger than guessNumber
                return self.generate_form_page(form, message["bigger"])
    #@+node:lee.20141221203113.56: *3* def weklink
    @cherrypy.expose
    def weblink(self):
        return """
    <script type="text/javascript" src="/static/weblink/pfcUtils.js"></script>
    <script type="text/javascript" src="/static/weblink/wl_header.js">
        document.writeln("Error loading Pro/Web.Link header!");
    </script>
    <script type="text/javascript" language="JavaScript">
        if (!pfcIsWindows()) netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
        // 若第三輸入為 false, 表示僅載入 session, 但是不顯示
        // ret 為 model open return
        var ret = document.pwl.pwlMdlOpen("cube.prt", "v:/tmp", false);
        if (!ret.Status) {
            alert("pwlMdlOpen failed (" + ret.ErrorCode + ")");
        }
        //將 ProE 執行階段設為變數 session
        var session = pfcGetProESession();
        // 在視窗中打開零件檔案, 並且顯示出來
        var window = session.OpenFile(pfcCreate("pfcModelDescriptor").CreateFromFileName("cube.prt"));
        var solid = session.GetModel("cube.prt",pfcCreate("pfcModelType").MDL_PART);
        var length,width,myf,myn,i,j,volume,count,d1Value,d2Value;
        // 將模型檔中的 length 變數設為 javascript 中的 length 變數
        a1 = solid.GetParam("a1");
        // 將模型檔中的 width 變數設為 javascript 中的 width 變數
        //改變零件尺寸
        //myf=20;
        //myn=20;
        volume=0;
        count=0;
        try
        {
            // 以下採用 URL 輸入對應變數
            //createParametersFromArguments ();
            // 以下則直接利用 javascript 程式改變零件參數
            for(i=0;i<=5;i++)
            {
                myf=100.0;
                // 設定變數值, 利用 ModelItem 中的 CreateDoubleParamValue 轉換成 Pro/Web.Link 所需要的浮點數值
                a1_Value = pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myf + i * 10);
                // 將處理好的變數值, 指定給對應的零件變數
                a1.Value = a1_Value;
                //零件尺寸重新設定後, 呼叫 Regenerate 更新模型
                solid.Regenerate(void null);
                //利用 GetMassProperty 取得模型的質量相關物件
                properties = solid.GetMassProperty(void null);
                //volume = volume + properties.Volume;
                volume = properties.Volume;
                count = count + 1;
                alert("執行第"+count+"次,零件總體積:"+volume);
                // 將零件存為新檔案
                var newfile = document.pwl.pwlMdlSaveAs("cube.prt", "v:/tmp", "cube"+count+".prt");
                if (!newfile.Status) {
                    alert("pwlMdlSaveAs failed (" + newfile.ErrorCode + ")");
                }
            }
            //alert("共執行:"+count+"次,零件總體積:"+volume);
            //alert("零件體積:"+properties.Volume);
            //alert("零件體積取整數:"+Math.round(properties.Volume));
        }
        catch(err)
        {
            alert ("Exception occurred: "+pfcGetExceptionType (err));
        }
    </script>
        """
    #@-others
#@-others
#@-leo
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
        self.name = '莊舜婷'
        self.number = '40323105'
        self.classes = 'nfu'
        self.github_repo_url = 'https://github.com/mdeta/2014cp'
        self.evaluation = [('Project ', 70), ('Project ', 70), ('Project ', 70)]
        self.photo_url = 'http://placekitten.com/g/350/300'
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
=======
>>>>>>> 7b6112ca16d684c239b025c7c787374257e99ca4
    #@-others
#@-others
#@-leo
