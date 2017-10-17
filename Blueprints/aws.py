from flask import Blueprint, render_template, request
from Modules.AWSModule import AWSModule

aws = Blueprint('aws', __name__)

@aws.route("/aws/")
def aws_ger():
    am = AWSModule()
    instances = am.list_instances()
    security_groups = am.list_security_groups()
    return render_template('aws.html', instances=instances, security_groups=security_groups)

@aws.route('/aws/new_sg/', methods=['GET','POST'])
def create_sg():
    try:
        if request.method == 'POST':
            nome = request.form['nome']
            descricao = request.form['descricao']
            am = AWSModule()
            am.create_security_group(nome, descricao)
            return render_template("aws_newsg.html", message="SG criado com sucesso")
        else:
            return render_template("aws_newsg.html")
    except Exception as e:
        return render_template("aws_newsg.html", message="Erro: %s" % e)



@aws.route('/aws/new_ec2/', methods=['GET','POST'])
def create_ec2():
    try:
        if request.method == 'POST':
            imagem = request.form['imagem']
            sg = request.form['sg']
            am = AWSModule()
            am.create_instance(imagem, sg)
            return render_template("aws_newec2.html", message="EC2 criado com sucesso")
        else:
            return render_template("aws_newec2.html")
    except Exception as e:
        return render_template("aws_newec2.html", message="Erro: %s" % e)