from Modules.SSHModule import SSHModule
from flask import Blueprint, render_template

servidores = Blueprint('servidores', __name__)

@servidores.route("/servidores/")
def ssh_load():
    try:
        sm = SSHModule()
        load = sm.load()
        memoria = sm.memoria()
        disco = sm.disco()
        return render_template("servidores.html", load=load, memoria=memoria, disco=disco)
    except Exception as e:
        return render_template("servidores.html", message="Falhou ao gerar informações: %s" % e)