from flask import Flask

app = Flask(__name__)
#check
#newcomme
#nopushkkakakksccs
#onrenderrrraaaarrrrrrr
#pushreqaaaaeegyjhjhj
# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
