from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from HyperDX instrumented Flask app!'

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'flask-hyperdx'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)