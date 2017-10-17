import requests
import json
from datetime import datetime

class GitlabModule:


    def createprojects(self,**dados):
        try:
            self.token = "rsSMxQqJy2s1yVyFsmJe"
            self.recurso = "projects"
            self.url = "http://10.100.0.113/api/v4/%s?private_token=%s" %(self.recurso, self.token)
            res = json.loads(requests.post(self.url, data=dados)._content.decode().decode('utf-8'))

            return res

        except Exception as e:
            print (e)

    def list_project(self):
        self.token = "rsSMxQqJy2s1yVyFsmJe"
        self.recurso = "projects"
        self.url = "http://10.100.0.113/api/v4/%s/?private_token=%s" % (self.recurso, self.token)
        print (self.url)

        response = json.loads(requests.get(self.url)._content.decode('utf-8'))
        return response

    def createuser(self, **kwargs):
        try:
            self.token = "rsSMxQqJy2s1yVyFsmJe"
            self.recurso = "users"
            self.url = "http://10.100.0.113/api/v4/%s?private_token=%s" % (self.recurso, self.token)
            res = json.loads(requests.post(self.url, data=kwargs)._content.decode('utf-8'))

            return res

        except Exception as e:
            print (e)

    def list_user(self):
        self.token = "rsSMxQqJy2s1yVyFsmJe"
        self.recurso = "users"
        self.url = "http://10.100.0.113/api/v4/%s/?private_token=%s" % (self.recurso, self.token)

        response = json.loads(requests.get(self.url)._content.decode())

        return response

if __name__ == '__main__':
    project = GitlabModule()
    lista = project.list_user()
    print (lista)

    #print [{'name': l.get('name'), 'created_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ"),
    #        'last_activity_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ")} for l in lista]
    #
    # for f in lista:
    #     print f["name"],type(str(f["created_at"])),type(str(f["last_activity_at"]))
