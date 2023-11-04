from app import db
from sqlalchemy.sql import func


class Usuario(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_nome = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_senha = db.Column(db.String(255), nullable=False)

class Tarefas(db.Model):
    tar_id = db.Column(db.Integer, primary_key=True)
    tar_user_id = db.Column(db.Integer, nullable=False)
    tar_titulo = db.Column(db.String(255), nullable=False)
    tar_descricao = db.Column(db.String(255), nullable=True)
    tar_status = db.Column(db.String(255), nullable=False)
    tar_data = db.Column(db.DateTime(timezone=True), default=func.now())