from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/denuncia', methods=['POST'])
def denuncia():
    texto = request.form.get('denuncia')
    print(f'Denúncia recebida: {texto}')  # Aqui você pode salvar num banco ou arquivo
    return render_template('index.html', mensagem='Denúncia enviada com sucesso!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
