from django.db import models

# Create your models here.
SIGLAS = ((1, 'AC'),(2, 'AL'),(3, 'AP'),(4, 'AM'),(5, 'BA'),(6, 'CE'),(7, 'DF'),
(8, 'ES'),(9, 'GO'),(10, 'MA'),(11, 'MT'),(12, 'MS'),(13, 'MG'),(14, 'PA'),(15, 'PB'),
(16, 'PR'),(17, 'PE'),(18, 'PI'),(19, 'RJ'),(20, 'RN'),(21, 'RS'),(22, 'RO'),(23, 'RR'),
(24, 'SC'),(25, 'SP'),(26, 'SE'),(27, 'TO'))

class Base(models.Model):
    criacao = models.DateField('Criado', auto_now_add=True)
    alteracao = models.DateTimeField('Alterado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True

class CadastroCliente(Base):
    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=20)
    cpf = models.DecimalField('CPF', max_digits=11, decimal_places=0)
    email = models.EmailField('Email', max_length=100)
    cep = models.DecimalField('CEP', max_digits=8, decimal_places=0)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.IntegerField('Número da casa')
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=30)
    uf = models.CharField(max_length=1, choices=SIGLAS)
    telefone = models.DecimalField('Telefone', max_digits=11, decimal_places=0)
