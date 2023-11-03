from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/set_cookie')
def index():
  cookie_value = request.cookies.get('sessionid', None)
  print(cookie_value)
  if cookie_value:
      # 如果cookie存在，执行相关操作
      pass
  return render_template('index.html', cookie_value=cookie_value)
app.run(port=5542)