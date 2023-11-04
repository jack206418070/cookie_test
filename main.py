from flask import Flask, make_response, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/set_cookie')
def set_cookie():
    resp = make_response(redirect('http://sub.shohumask.shop/'))
    resp.set_cookie('sessionid', 'cookie_value', domain='.shohumask.shop', secure=False)
    return resp


app.run(port=5541)