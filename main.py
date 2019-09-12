from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
          <!-- create your form here -->
        
            <form action = "/add" method = "post">
                <label for ="rotate-by">
                    <strong>Rotate by: </strong>
                    <input type = "text" id="rotate-by" name = "rot" value = "0"/>
                </label>
                <textarea name = "text"> </textarea>
                <input type = "submit" value = "Submit Query" />
            </form>
        </body>
    </html>    
    """



@app.route("/") #This should be giving a 405 method not allowed but instead gives 404 when submitted
#@app.route("/add", methods=['POST'])
def index():
    return form #"Hello World"

app.run()