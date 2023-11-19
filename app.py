from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def webhook_callback():
    print("hi")
    return "hi"

if __name__ == '__main__':
    app.run(debug=True)
