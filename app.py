from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_content():
    url = request.args.get('url')
    result = subprocess.check_output(['phantomjs', 'fetchContent.js', url])
    return jsonify({'content': result.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)
