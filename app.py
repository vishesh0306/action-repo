from flask import Flask

app = Flask(__name__)
#check
#newcomment
#nopushk
#onrender
#pushreq
# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
