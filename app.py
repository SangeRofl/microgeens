from flask import Flask, render_template, url_for, request, flash
from application.ui import SystemInterface, EntranceScreen
from application.system import System

app = Flask("microgreens")
app.config['SECRET_KEY'] = 'gf789sdg4p3ogdrsg0fsdgdfs0g'
prods = ["Яблоко", "Апельсин", "Груша"]




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', products = prods)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return 'hello moto-moto'

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if(request.method == 'POST'):
        print(request.form)
        flash('Вход выполнен', category='success')
    return render_template('index.html', products = prods)

@app.route('/lnk')
def lnk():
    return 'Тест ссылок'

@app.errorhandler(404)
def pageNotFound(error):
    return '<h1>Попали не туда</h1>' 

if __name__ == "__main__":
    System()
    app.run(debug = True)