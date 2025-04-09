from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Cria a tabela se não existir
def init_db():
    conn = sqlite3.connect('denuncias.db')
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS denuncias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        texto TEXT NOT NULL,
        data_hora TEXT
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
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if texto:
        conn = sqlite3.connect('denuncias.db')
        c = conn.cursor()
        c.execute("INSERT INTO denuncias (nome, texto, data_hora) VALUES (?, ?, ?)", (nome, texto, data_hora))
        conn.commit()
        conn.close()
    return render_template('index.html', mensagem='Denúncia enviada com sucesso!')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
