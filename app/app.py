from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def healthz():
    # return jsonify({'status': '200 OK'}), 200
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
