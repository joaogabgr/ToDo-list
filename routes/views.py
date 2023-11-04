from app import app, get_user
from flask import render_template, session, request, redirect, url_for
from models import Tarefas

@app.route('/')
def index():
    if get_user() is None:
        return redirect(url_for('autenticar', q='cadastrar'))
    else:
        lista = Tarefas.query.filter_by(tar_user_id=session['user']).order_by(Tarefas.tar_id.desc()).all()
        return render_template('index.html',lista=lista, user=get_user())
    
@app.route('/autenticar', methods=['GET'])
def autenticar():
    print(get_user())
    if get_user() != None:
        return redirect(url_for('index'))
    
    q = request.args.get('q')
    return render_template('autenticar.html', action=q, user=get_user())
