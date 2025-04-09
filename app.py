from flask import Flask, render_template, request
import psycopg2
from datetime import datetime
import os

app = Flask(__name__)

# Dados do banco (pegos do Render)
DB_HOST = os.getenv('DB_HOST', 'dpg-cvrbvmbuibrs73doueng-a.render.com')
DB_NAME = os.getenv('DB_NAME', 'rafael_maia_da_silva')
DB_USER = os.getenv('DB_USER', 'rafael_maia_da_silva_user')
DB_PASS = os.getenv('DB_PASS', 'ObmtxVsbbMHKgyDUcZWiAUGQOOtzfrc9')
DB_PORT = os.getenv('DB_PORT', '5432')

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

# Cria a tabela se não existir
def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS denuncias (
            id SERIAL PRIMARY KEY,
            nome TEXT,
            texto TEXT NOT NULL,
            data_hora TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/denuncia', methods=['POST'])
def denuncia():
    nome = request.form.get('nome')
    texto = request.form.get('denuncia')
    data_hora = datetime.now()

    if texto:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO denuncias (nome, texto, data_hora) VALUES (%s, %s, %s)",
            (nome, texto, data_hora)
        )
        conn.commit()
        conn.close()

    return render_template('index.html', mensagem="Denúncia enviada com sucesso!")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
