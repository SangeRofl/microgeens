from flask import Flask, render_template, url_for, request, flash
from application.ui import SystemInterface, EntranceScreen, Registration, Enrtance
from application.system import System
from application.goods import Item

flag=False

app = Flask("microgreens")
app.config['SECRET_KEY'] = 'gf789sdg4p3ogdrsg0fsdgdfs0g'
prods = ['1']

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if (request.method=='POST'):
        r.writeUserData([request.form['username'], request.form['pwd']])
    return es.showEntranceScreen()

@app.route('/product', methods=['GET', 'POST'])
def product():
    return render_template('product.html')

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    return si.showGoods(0)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return r.showRegistrationScreen('register.html')

@app.route('/main', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    global flag
    if(not flag):
        if (request.method=='POST'):
            currUser = [request.form['username'], request.form['pwd']]  
            if(e.checkLogin(currUser[0])):
                if(e.checkPassword(currUser[1])):
                    flag = True
                    return si.showMainPage()
            return es.showEntranceScreen()
    return r.showRegistrationScreen('register.html')
    


if __name__ == "__main__":
    si = SystemInterface()
    es = EntranceScreen('\\auth')
    e = Enrtance()
    r = Registration()
    s = System()
    s.runSystemInterface()
    app.run(debug = True)