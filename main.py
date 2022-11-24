from flask import Flask

app = Flask("microgreens")

if __name__ == "__main__":
    app.run(Debug=True)