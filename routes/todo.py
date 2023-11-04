from app import db, app, get_user
from models import Tarefas
from flask import request, redirect, url_for, session, flash, render_template

@app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    
    if titulo == '' or descricao == '':
        flash('Preencha todos os campos!')
        return redirect(url_for('index'))
    
    tarefa = Tarefas(tar_titulo=titulo, tar_descricao=descricao, tar_user_id=session['user'], tar_status='Pendente')
    
    db.session.add(tarefa)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/editar/<id>', methods=['GET'])
def editar_form(id):
    tarefa = Tarefas.query.filter_by(tar_id=id).first()
    
    return render_template('editar.html', tarefa=tarefa, user=get_user())

@app.route('/editar/<id>', methods=['POST'])
def editar(id):
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    status = request.form['status']
    
    if titulo == '' or descricao == '' or status == '':
        flash('Preencha todos os campos!')
        return redirect(url_for('index'))
    
    tarefa = Tarefas.query.filter_by(tar_id=id).first()
    tarefa.tar_titulo = titulo
    tarefa.tar_descricao = descricao
    tarefa.tar_status = status
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/excluir/<id>', methods=['GET'])
def excluir(id):
    tarefa = Tarefas.query.filter_by(tar_id=id).first()
    
    db.session.delete(tarefa)
    db.session.commit()
    
    return redirect(url_for('index'))