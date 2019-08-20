from app import app
from flask import render_template
from flask import request
import minesweeper
game=str()

@app.route('/game', methods=['POST'])
def index():
    global game
     
    game=minesweeper.minesweeper(int(request.form.get('len')),float(request.form.get('lvl')))
    game.setupMines()
    return render_template('index.html', title='Home', fmatrix=game.frontmatrix, bmatrix=game.backmatrix)

@app.route('/')
def init():
    return render_template('init.html')

@app.route('/field', methods=['POST'])
def checkfield():
    global game
    rlist=list()
    rlist.append(int(request.form.get('X')))
    rlist.append(int(request.form.get('Y')))
    print(rlist)
    if not game.checkField(rlist):
        return render_template('end.html')     
    
    return render_template('index.html', title='Home', fmatrix=game.frontmatrix, bmatrix=game.backmatrix)
