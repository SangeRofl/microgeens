from flask import Flask, render_template, url_for, request, flash
from application.ui import SystemInterface, EntranceScreen
from application.system import System
from application.goods import Item

app = Flask("microgreens")
app.config['SECRET_KEY'] = 'gf789sdg4p3ogdrsg0fsdgdfs0g'

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if(request.method == 'POST'):
        flash('Вход выполнен', category='success')
        return si.showMainPage()
    return es.showEntranceScreen()



@app.route('/main', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', products = prods)


if __name__ == "__main__":
    si = SystemInterface()
    s = System()
    es = EntranceScreen('\auth')
    app.run(debug = True)