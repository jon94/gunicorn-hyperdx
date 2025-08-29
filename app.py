from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from HyperDX instrumented app!'

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'gunicorn-hyperdx'}

if __name__ == '__main__':
    app.run()