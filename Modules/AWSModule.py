#!/usr/bin/python3

import boto3

class AWSModule(object):
    def __init__(self):
        self.ec2 = boto3.resource("ec2")

    def list_instances(self):
        return self.ec2.instances.all()

    def list_security_groups(self):
        return self.ec2.security_groups.all()

    def create_instance(self,image,sg=None):
        try:
            self.ec2.create_instances(ImageId=image,
                                      InstanceType="t2.micro",
                                      MinCount=1,
                                      MaxCount=1,
                                      SecurityGroupIds=sg)
            return "EC2 criado com sucesso!"
        except Exception as e:
            return e

    def create_security_group(self, nome, descricao):
        try:
            sg = self.ec2.create_security_group(GroupName=nome, Description=descricao)
            return "Grupo criado com sucesso!"
        except Exception as e:
            return e



if __name__ == '__main__':
    aws = AWSModule()
    for u in aws.list_instances():
        print (u.id)