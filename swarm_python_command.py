import subprocess
from subprocess import Popen, PIPE

@app.route('/swarm_start')
def swarm_start():
    output = subprocess.check_output('docker swarm init', shell=True)
    v = str(output.decode(encoding="utf-8"))
    x = v.split("command:")
    r = x[1]
    k = r.split("To add")
    j = k[0]
    return j

@app.route('/swarm_stop')
def swarm_stop():
    output = subprocess.check_output('docker swarm  leave --force', shell=True)
    return output

@app.route('/jupyter_start')
#@token_required
def jupyter_start():
    run_command('jupyter notebook')
    return "Start Service"

@app.route('/jupyter_stop')
def jupyter_stop():
    run_command('jupyter notebook stop')
    return "Stop Service"
    
    
