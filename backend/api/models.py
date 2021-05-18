from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class Pavilhao(models.Model):
    numero = models.IntegerField()
    capacidade = models.IntegerField(default=116)
    restante = models.IntegerField(default=0)

    def __str__(self):
        return f'Pavilhão Habitacional {self.numero}'

    class Meta:
        verbose_name = 'Pavilhão'
        verbose_name_plural = 'Pavilhões'
        ordering = ['id']


class Sentenciado(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=50)
    pavilhao = models.ForeignKey(
        Pavilhao,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Reeducando.: {self.nome}'
