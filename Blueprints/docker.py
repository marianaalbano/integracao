from flask import Blueprint, request, render_template, jsonify

from Modules.DockerModule import DockerModule

container = Blueprint('container', __name__)

@container.route("/container/")
def docker_ger():
    dm = DockerModule()
    containers = dm.list_containers()
    return render_template("docker.html", containers=containers)


@container.route("/container/stop/", methods=["POST"])
def stop():
    container_id = request.form["id"]
    dm = DockerModule()
    dm.stop_container(container_id)
    return jsonify({"message": "Container parado com sucesso!"})


@container.route("/container/start/", methods=["POST"])
def start():
    container_id = request.form["id"]
    dm = DockerModule()
    dm.start_container(container_id)
    return jsonify({"message": "Container iniciado com sucesso!"})


@container.route("/container/remove/", methods=["DELETE"])
def delete_container():
    container_id = request.form["id"]
    dm = DockerModule()
    res = dm.delete_container(container_id)
    return jsonify({"message": res})


@container.route("/container/new/", methods=["GET", "POST"])
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