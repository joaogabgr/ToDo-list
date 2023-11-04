from app import app, db
from flask import request, redirect, url_for, session, flash
from models import Usuario

@app.route('/autenticar', methods=['POST'])
def autentica():
    if 'q' in request.args:
        action = request.args.get('q')

    if action == 'login':
        email = request.form['email']
        senha = request.form['senha']

        if email == '' or senha == '':
            flash('Preencha todos os campos!')
            return redirect(url_for('index'))
        
        if not Usuario.query.filter_by(user_email=email).first():
            flash('Email não cadastrado!')
            return redirect(url_for('index'))
        
        if not Usuario.query.filter_by(user_email=email, user_senha=senha).first():
            flash('Senha incorreta!')
            return redirect(url_for('index'))
        
        session['user'] = Usuario.query.filter_by(user_email=email, user_senha=senha).first().user_id
        return redirect(url_for('index'))

    if action == 'cadastrar':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senhaConf = request.form['senhaConf']

        if nome == '' or email == '' or senha == '' or senhaConf == '':
            flash('Preencha todos os campos!')
            return redirect(url_for('index'))
        
        if Usuario.query.filter_by(user_email=email).first():
            flash('Email já cadastrado!')
            return redirect(url_for('index'))
        
        if senha != senhaConf:
            flash('Senhas não conferem!')
            return redirect(url_for('index'))
        
        user = Usuario(user_nome=nome, user_email=email, user_senha=senha)

        db.session.add(user)
        db.session.commit()

        session['user'] = user.user_id
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('index'))
