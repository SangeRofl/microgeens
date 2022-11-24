from flask import Flask, render_template

app = Flask("microgreens")
prods = ["Яблоко", "Апельсин", "Груша"]
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', products = prods)
@app.route('/about', methods=['GET', 'POST'])
def about():
    return 'hello moto-moto'

if __name__ == "__main__":
    app.run(debug = True)