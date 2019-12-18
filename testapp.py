from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def hello_server():
    return "Hello world"

if __name__ == "__main__":
    print("Start")
    app.run(port=8000)