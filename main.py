from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Custom Redirect URI"

@app.route("/callback", methods=['GET', 'POST'])
def callback():
    code = request.url.split('&')
    for param in code:
        if param.startswith("code"):
            code = param.split("code=")[-1]
            break
            
    if request.args.get('format') == "json":
        return jsonify({"code": code})
    elif request.args.get('format') == "plain":
        return f"<h1>{code}</h1>"
    elif request.args.get('format') == "html":
        return f"""<h1> Authorized code </h1>
                    <h3>{code}</h3>
                """
    else:
        return "Got an empty request..."
                

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
