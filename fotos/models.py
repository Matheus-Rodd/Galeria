from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='fotos/images/', null=True, blank=True)
    data_viagem = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_viagem', '-created_at']

    def __str__(self):
        return f"{self.titulo} — {self.local}"
