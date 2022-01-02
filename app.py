import subprocess
from subprocess import Popen, PIPE
import shlex
from IPython.lib import passwd

import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api', methods=['GET', 'POST'])
def api():
    with open("stdout.txt","wb") as out:
         r=subprocess.run(["jupyter", "notebook", "list"], stdout=out)

         output = subprocess.check_output('jupyter notebook list', shell=True)
         v = str(output.decode(encoding="utf-8"))
         v=v.strip().split("\n")[-1]
         x = v.split("=")
         r = x[1]
         #r = r.replace(" :: /home/ubuntu", "")
         r = r.replace("http://0.0.0.0:8888/?token","")
         r = r.replace("/home","")
         r = r.replace(" :: ","")
         return r

    #return {
    #    "user": str(r),
    #}

def run_command(cmd):
    p = Popen(shlex.split(cmd), bufsize=1, universal_newlines=True)
    return p.poll()

if __name__ == "__main__":
    run_command('jupyter notebook')
    app.run(host='0.0.0.0', port=5000 , debug=True)
