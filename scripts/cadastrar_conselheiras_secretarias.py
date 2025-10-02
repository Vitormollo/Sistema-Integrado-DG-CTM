from django.contrib.auth.models import User
from usuario.models import Conselheira, Secretaria

# Conselheiras fictícias
conselheiras_info = [
    ("conselheira1", "Conselheira Fictícia 1"),
    ("conselheira2", "Conselheira Fictícia 2"),
    ("conselheira3", "Conselheira Fictícia 3"),
    ("conselheira4", "Conselheira Fictícia 4"),
]
for username, nome in conselheiras_info:
    user = User.objects.get(username=username)
    Conselheira.objects.get_or_create(id_user=user, nome_conselheira=nome)

# Secretarias reais
secretarias_info = [
    ("vitor", "Vitor Mollo Cunha"),
    ("ana", "Ana Carolina Carnelos Masquetti"),
]
for username, nome in secretarias_info:
    user = User.objects.get(username=username)
    Secretaria.objects.get_or_create(id_user=user, nome_secretaria=nome)

print("Cadastro realizado com sucesso!")
