from datetime import datetime

from django.db import models



class Fotografia (models.Model):
    
    OPÇÕES_CATEGORIA = [
        ('NEBULOSA', 'nebulo'),
        ('ESTRELA' , 'estrela'),
        ('GALAXIA', 'galaxia'),
        ('PLANETA', 'planeta')
        
    ]
    nome = models.CharField(max_length=100, null=False,blank=False)
    legenda = models.CharField(max_length=100, null=False,blank=False)
    categoria = models.CharField(max_length=100,choices=OPÇÕES_CATEGORIA,default='')
    descricao = models.TextField(null=False, blank= True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publica = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now,blank=False)

    def __str__(self):
        return f"Fotografia [nome = {self.nome}]"