from flask import Flask , request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    ip = request.args.get('ip')
    return '''<h1>My ip : {}</h1>'''.format(ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
