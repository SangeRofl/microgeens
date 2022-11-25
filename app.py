from flask import Flask, render_template, url_for, request, flash
from application.ui import SystemInterface, EntranceScreen, Registration
from application.system import System
from application.goods import Item

currUser=False

app = Flask("microgreens")
app.config['SECRET_KEY'] = 'gf789sdg4p3ogdrsg0fsdgdfs0g'
prods = ['1']

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    return es.showEntranceScreen()\

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    return si.showGoods(0)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return r.showRegistrationScreen('register.html')

@app.route('/main', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    global currUser
    if (request.method=='POST'):
        currUser = True  
    if(not currUser):
        return r.showRegistrationScreen('register.html')
    
    return si.showMainPage()


if __name__ == "__main__":
    si = SystemInterface()
    s = System()
    es = EntranceScreen('\\auth')
    r = Registration()
    app.run(debug = True)