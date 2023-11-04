# ToDo list

## Tecnologias Utilizadas

- HTML
- CSS
- JavaScript
- Python (Flask)
- MySQL

## Requisitos minimos

- MySQL Server
- Python
- VirtualEnv

## Funcionalidades Principais

- **Adição de Tarefas:** Os usuários devem poder adicionar novas tarefas à lista.
- **Remoção de Tarefas:** Deve haver uma opção para os usuários removerem tarefas concluídas ou não desejadas.
- **Marcar como Concluído:** Os usuários devem poder marcar tarefas como concluídas.
- **Editar Tarefas:** Permitir que os usuários editem o texto das tarefas existentes.

## Configuração do Ambiente

Para configurar o ambiente e iniciar o projeto, siga os passos abaixo:

1. Clone este repositório:

```bash
git clone https://github.com/joaogabgr/ToDo-list .
```

2. Ative a maquina virtual:

```bash
py -m venv venv
.\venv\Scripts\activate
```

3. Baixar dependencias:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:

```bash
Altere as informações do banco de dados no "config.py" 
```

5. Inicar o banco de dados:

```bash
mysql -u root -p < Banco.sql
```

6. Iniciar programa:

```bash
python app.py
```
