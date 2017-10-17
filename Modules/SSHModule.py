import paramiko
from paramiko import SSHClient


class SSHModule(object):

    def __init__(self):
        try:
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        except Exception as e:
            return "Erro: %s" %e


    def load(self):
        try:
            dados = []
            self.maquinas = ['localhost','localhost','localhost']
            for maquina in self.maquinas:
                self.client.connect(maquina, username='user', password='passwd')
                stdin,stdout,stderr = self.client.exec_command('uptime')
                if stderr.channel.recv_exit_status() != 0:
                    raise Exception(stderr.channel.recv_exit_status())
                    dados.append(stderr.read().decode('utf-8'))
                else:
                    dados.append(stdout.read().decode('utf-8'))
            return dados
        except Exception as e:
            return e

    def memoria(self):
        try:
            dados = []
            self.maquinas = ['localhost','localhost','localhost']
            for maquina in self.maquinas:
                self.client.connect(maquina, username='user', password='passwd')
                stdin,stdout,stderr = self.client.exec_command('free -m')
                if stderr.channel.recv_exit_status() != 0:
                    stderr.channel.recv_exit_status()
                    dados.append(stderr.read().decode('utf-8'))
                else:
                    dados.append(stdout.read().decode('utf-8'))
            return dados
        except Exception as e:
            return e


    def disco(self):
        try:
            dados = []
            self.maquinas = ['localhost','localhost','localhost']
            for maquina in self.maquinas:
                self.client.connect(maquina, username='user', password='passwd')
                stdin,stdout,stderr = self.client.exec_command(" df -h /")
                if stderr.channel.recv_exit_status() != 0:
                    stderr.channel.recv_exit_status()
                    dados.append(stderr.read().decode('utf-8'))
                else:
                    dados.append(stdout.read().decode('utf-8'))
            return dados
        except Exception as e:
            return e

