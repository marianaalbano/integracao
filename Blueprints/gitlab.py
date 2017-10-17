from flask import Blueprint, render_template, request
import datetime

from Modules.GitlabModule import GitlabModule

gitlab = Blueprint('gitlab', __name__)


@gitlab.route("/gitlab/new_project/", methods=["GET", "POST"])
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


@gitlab.route("/gitlab/new_user/", methods=["GET", "POST"])
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


@gitlab.route("/gitlab/")
def gitlab_ger():
    gm = GitlabModule()
    lista = gm.list_project()
    projects = [{'name': l.get('name'), 'created_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ"),
                 'last_activity_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ")} for l in lista]
    users = gm.list_user()
    return render_template("gitlab.html", projects=projects, users=users)