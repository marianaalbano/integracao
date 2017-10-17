#!/usr/bin/python
from datetime import datetime

from flask import Flask, render_template, redirect, request, jsonify

from Modules.DockerModule import DockerModule
from Modules.GitlabModule import GitlabModule

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/index/")


@app.route("/index/")
def home():
    return render_template("base.html")


@app.route("/container/")
def docker_ger():
    dm = DockerModule()
    containers = dm.list_containers()
    return render_template("container.html", containers=containers)


@app.route("/container/stop/", methods=["POST"])
def stop():
    container_id = request.form["id"]
    dm = DockerModule()
    dm.stop_container(container_id)
    return jsonify({"message": "Container parado com sucesso!"})


@app.route("/container/start/", methods=["POST"])
def start():
    container_id = request.form["id"]
    dm = DockerModule()
    dm.start_container(container_id)
    return jsonify({"message": "Container iniciado com sucesso!"})


@app.route("/container/remove/", methods=["DELETE"])
def delete_container():
    container_id = request.form["id"]
    dm = DockerModule()
    res = dm.delete_container(container_id)
    return jsonify({"message": res})


@app.route("/container/new/", methods=["GET", "POST"])
def container_new():
    try:
        if request.method == "POST":
            name = request.form["container-name"]
            image = request.form["container-image"]
            command = request.form["container-command"]
            dm = DockerModule()
            dm.create_container(name=name,
                                image=image,
                                command=command)
            return render_template("docker_new.html", message="Container criado com sucesso")
        else:
            return render_template("docker_new.html")
    except Exception as e:
        return render_template("docker_new.html", message="Erro: %s" % e)


@app.route("/gitlab/new_project/", methods=["GET", "POST"])
def gitlab_newproject():
    try:
        if request.method == "POST":
            name = request.form['project-name']
            gm = GitlabModule()
            res = gm.createprojects(name=name)
            return render_template("gitlab_newproject.html", message="Projeto criado com sucesso")
        else:
            return render_template("gitlab_newproject.html")
    except Exception as e:
        return render_template("gitlab_newproject.html", message="Erro: %s" % e)


@app.route("/gitlab/new_user/", methods=["GET", "POST"])
def gitlab_newuser():
    try:
        if request.method == "POST":
            name = request.form['name']
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            gm = GitlabModule()
            res = gm.createprojects(name=name, username=username, password=password, email=email)
            return render_template("gitlab_newuser.html", message="Usuario criado com sucesso")
        else:
            return render_template("gitlab_newuser.html")
    except Exception as e:
        return render_template("gitlab_newuser.html", message="Erro: %s" % e)


@app.route("/gitlab/")
def gitlab_ger():
    gm = GitlabModule()
    lista = gm.list_project()
    projects = [{'name': l.get('name'), 'created_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ"),
                 'last_activity_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ")} for l in lista]
    users = gm.list_user()
    return render_template("gitlab.html", projects=projects, users=users)


if __name__ == '__main__':
    app.run(debug=True)
