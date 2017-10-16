import paramiko


class SSHModule():

    def __init__(self):
        try:
            maquinas = ['localhost','localhost','localhost']
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            for maquina in maquinas:
                self.client.connect(maquina, username='root', password='4linux')
            ("Conexão feita com sucesso!")
        except Exception as e:
            return "Erro: %s" %e


    def load(self):
        try:
            stdin,stdout,stderr = self.client.exec_command('uptime')
            if stderr.channel.recv_exit_status() != 0:
                stderr.channel.recv_exit_status()
                return stderr.read().decode('utf-8')
            else:
                return stdout.read().decode('utf-8')
            return "Comando executado com sucesso!"
        except Exception as e:
            return "Comando falhou!"

