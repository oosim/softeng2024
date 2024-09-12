from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():

    return """
 <!DOCTYPE html>
 <html lang="kr">
 <head>
 <meta charset="UTF-8">
 <title>Flask Home Page</title>
 </head>
 <body>
 <form method="GET" action="/dan/">
 <h2>구구단 출력하기</h2>
 <label>단 :
 <input type="text" name="dan">
 </label>
 <button type="submit">출력</button>
 </form>
 </body>
 </html>
    """

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {name} 님."

# 주소창에 /dan/7 입력
@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = <strong>{int(dan) * i}</strong><br>"
    return html_str

# 주소창에 /dan/?dan=5 입력
@app.route("/dan/")
def gugudan_arg_html():
    dan = request.args.get('dan', "1")
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = <strong>{int(dan) * i}</strong><br>"
    return html_str

app.run(debug=True)

#...