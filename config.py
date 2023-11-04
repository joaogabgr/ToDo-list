SECRET_KEY = 'TodoList'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '2412',
        servidor = 'localhost',
        database = 'ToDo'
    )