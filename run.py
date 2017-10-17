#!/usr/bin/python3

from datetime import datetime

from flask import Flask, render_template, redirect, request, jsonify

from Modules.DockerModule import DockerModule
from Modules.GitlabModule import GitlabModule
from Modules.SSHModule import SSHModule

from Blueprints.servidores import servidores
from Blueprints.docker import container
from Blueprints.gitlab import gitlab
from Blueprints.aws import aws


app = Flask(__name__)
app.register_blueprint(servidores)
app.register_blueprint(container)
app.register_blueprint(gitlab)
app.register_blueprint(aws)

@app.route("/")
def index():
    return redirect("/index/")


@app.route("/index/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
