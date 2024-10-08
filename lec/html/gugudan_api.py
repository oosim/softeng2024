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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
 </head>
 <body>
    <h2>구구단을 외우자 !</h2>
    <form id="form_id" action="javascript:post_query()">
        <input type="text" name="dan" value="7">
        <button type="submit">Go</button>
    </form>
    <div id="results"></div>

 <script>
     function post_query() {
     $.ajax({
         type: "GET",
         url: "/dan/",
         data: $("#form_id").serialize(),
         success: update_result,
         dataType: "html"
         });
     }
     
     function update_result(data) {
        $("#results").html(data);
     }
 </script>

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