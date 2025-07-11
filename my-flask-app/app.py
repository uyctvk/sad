import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask on Render!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # PORT環境変数を使う
    app.run(host='0.0.0.0', port=port)