from django.contrib import admin
from django.utils.html import format_html
from .models import Foto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "local", "data_viagem", "preview", "created_at")
    search_fields = ("titulo", "descricao", "local")
    list_filter = ("local", "data_viagem")

    fieldsets = (
        ("Informações Principais", {"fields": ("titulo", "local", "descricao")}),
        ("Imagem", {"fields": ("imagem",)}),
        ("Datas", {"fields": ("data_viagem",)}),
    )

    def preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:6px;"/>',
                obj.imagem.url
            )
        return "—"
    preview.short_description = "Prévia"
