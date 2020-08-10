from django.db import models

# Create your models here.

class FUNCIONARIO(models.Model):
    NOM_FUNCIO = models.CharField(max_length=100, null=False, verbose_name="Nome")
    DCR_CARGO_FUNCIO = models.CharField(max_length=50, null=False, verbose_name="Cargo")

    def __str__(self):
        return self.NOM_FUNCIO

class OBRA(models.Model):
    NOM_OBRA = models.CharField(max_length=100, null=False, verbose_name="Nome")
    IMG_OBRA = models.ImageField(upload_to='images', null=True, verbose_name="Foto")
    NOM_CLIENT_OBRA = models.CharField(max_length=70, null=False, verbose_name="Cliente")
    DAT_OBRA = models.DateField(null=False, verbose_name="Data de início")
    NOM_FNCRSP_OBRA = models.ForeignKey(FUNCIONARIO, on_delete=models.CASCADE, verbose_name="Responsável")

    def __str__(self):
        return self.NOM_OBRA

class PRODUTO(models.Model):
    TIPO_CHOICES = (
        ("produto", "Produto"),
        ("serviço", "serviço"),
    )
    NOM_PRODUT = models.CharField(max_length=100, null=False, verbose_name="Nome")
    IMG_PRODUT = models.ImageField(upload_to='images', verbose_name="Foto")
    DAT_PRODUT = models.DateField(null=False, verbose_name="Data de Atualização")
    VLR_PRODUT = models.FloatField(null=False, verbose_name="Valor Unit.")
    QTD_PRODUT = models.FloatField(null=False, verbose_name="Qtd. em estoque")
    DCR_MODELO_PRODUT = models.CharField(max_length=50, verbose_name="Modelo")
    DCR_FABRIC_PRODUT = models.CharField(max_length=50, verbose_name="Fabricante")
    MRC_PRDSRV_PRODUT = models.CharField(max_length=20, choices=TIPO_CHOICES, null=False, verbose_name="Classificação")

    def __str__(self):
        return self.NOM_PRODUT

class ITEM_OBRA(models.Model):
    NOMEOBRA = models.ForeignKey(OBRA, on_delete=models.CASCADE, verbose_name="Nome")
    NOMEPRODUTO = models.ForeignKey(PRODUTO, on_delete=models.CASCADE, verbose_name="Produto")
    QTD_ITMOBR = models.FloatField(null=False, verbose_name="Qtd. Aplicada")
    DCR_OBSERV_ITMOBR = models.CharField(max_length=50, verbose_name="Observação")

    def __int__(self):
        return self.id
