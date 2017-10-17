#!/usr/bin/python3

from docker import Client


class DockerModule:
    def __init__(self):
        try:
            self.client = Client("tcp://10.100.0.165:2376", version="auto")
        except Exception as e:
            print ('Falhou ao conectar no docker: ', e)

    def list_containers(self):
        containers = self.client.containers(all=True)
        return containers

    def start_container(self, id):
        res = self.client.start(container=id)
        return res

    def stop_container(self, id):
        res = self.client.stop(container=id)
        return res

    def delete_container(self, container):
        self.stop_container(container)
        self.client.remove_container(container=container)
        return "Container removido com sucesso"

    def create_container(self, **kwargs):
        self.client.pull(kwargs.get("image"))
        res = self.client.create_container(name=kwargs.get("name"),
                                           image=kwargs.get("image"),
                                           command=kwargs.get("command"),
                                           stdin_open=True,
                                           detach=True,
                                           tty=True)
        return res


if __name__ == '__main__':
    c = DockerModule()
    c.create_container(name="mari", image="ubuntu", command="echo 'teste'")
    print ('ok')
