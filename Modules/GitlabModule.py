import requests
import json
from datetime import datetime

class GitlabModule:


    def createprojects(self,**dados):
        try:
            self.token = "y5BAhu9Tdmi84XjSY2yR"
            self.recurso = "projects"
            self.url = "http://10.100.0.62/api/v3/%s/?private_token=%s" %(self.recurso, self.token)
            res = json.loads(requests.post(self.url, data=dados)._content)

            return res

        except Exception as e:
            print e

    def list_project(self):
        self.token = "y5BAhu9Tdmi84XjSY2yR"
        self.recurso = "projects"
        self.url = "http://10.100.0.62/api/v3/%s/?private_token=%s" % (self.recurso, self.token)

        response = json.loads(requests.get(self.url)._content)

        return response

    def createuser(self, **dados):
        try:
            self.token = "y5BAhu9Tdmi84XjSY2yR"
            self.recurso = "users"
            self.url = "http://10.100.0.62/api/v3/%s/?private_token=%s" % (self.recurso, self.token)
            res = json.loads(requests.post(self.url, data=dados)._content)

            return res

        except Exception as e:
            print e

    def list_user(self):
        self.token = "y5BAhu9Tdmi84XjSY2yR"
        self.recurso = "users"
        self.url = "http://10.100.0.62/api/v3/%s/?private_token=%s" % (self.recurso, self.token)

        response = json.loads(requests.get(self.url)._content)

        return response

if __name__ == '__main__':
    project = GitlabModule()
    lista = project.list_user()
    print lista

    #print [{'name': l.get('name'), 'created_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ"),
    #        'last_activity_at': datetime.strptime(l.get('created_at'), "%Y-%m-%dT%H:%M:%S.%fZ")} for l in lista]
    #
    # for f in lista:
    #     print f["name"],type(str(f["created_at"])),type(str(f["last_activity_at"]))
