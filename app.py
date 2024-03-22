from flask import Flask, render_template

app = Flask(__name__,
            static_folder= 'src/static',
            template_folder = 'src/template')

@app.route('/')
@app.route('/index')
def principal():
    return render_template('index.html', titulo="Teste")

# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/flask')
def minha_funcao():
    return '<h1>Está é uma outra rota</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
