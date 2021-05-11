from django.db import models

# Create your models here.
SIGLAS = (('ac', 'AC'),('al', 'AL'),('ap', 'AP'),('am', 'AM'),('ba', 'BA'),('ce', 'CE'),('df', 'DF'),
('es', 'ES'),('go', 'GO'),('ma', 'MA'),('mt', 'MT'),('ms', 'MS'),('mg', 'MG'),('pa', 'PA'),('pb', 'PB'),
('pr', 'PR'),('pe', 'PE'),('pi', 'PI'),('rj', 'RJ'),('rn', 'RN'),('rs', 'RS'),('ro', 'RO'),('rr', 'RR'),
('sc', 'SC'),('sp', 'SP'),('se', 'SE'),('to', 'TO'))

class Base(models.Model):
    criacao = models.DateField('Criado', auto_now_add=True)
    alteracao = models.DateTimeField('Alterado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True

class CadastroCliente(Base):
    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=20)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('Email', max_length=100)
    cep = models.DecimalField('CEP', max_digits=8, decimal_places=0)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.IntegerField('Número da casa')
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=30)
    uf = models.CharField(max_length=2, choices=SIGLAS)
    telefone = models.DecimalField('Telefone', max_digits=11, decimal_places=0)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
