from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/callback', methods=['GET', 'POST'])
def callback():
    code = request.url.split('code=')[-1]
    if request.args.get('format') == 'json':
        return jsonify({"code": code})
    else:
        return f"""<h1> Authorized code </h1>
                    <h3>{code}</h3>
                """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
