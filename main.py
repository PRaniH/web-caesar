from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
          <!-- create your form here -->
        
            <form action = "/" method = "post">
                <label for ="rotate-by">
                    <strong>Rotate by: </strong>
                    <input type = "text" id="rotate-by" name = "rot" value = "0"/>
                </label>
                <textarea id = "text" name = "text">{0}</textarea>
                <input type = "submit" value = "Submit Query" />
            </form>
        </body>
    </html>    
    """

@app.route("/", methods=['POST'])
def encrypt():
    text_string = request.form['text']
    rot_amt = request.form['rot']

    rotated_string = rotate_string(str(text_string), int(rot_amt))

    return "<!DOCTYTPE HTML> <HTML> <HEADER></HEADER> <BODY> <H1>" + form.format(rotated_string) + "</H1> </BODY> </HTML>"


@app.route("/")
def index():
    return form.format("") #"Hello World"

app.run()