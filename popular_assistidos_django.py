import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SIGCTM.settings')
django.setup()

from assistido.models import Assistido, Telefone, Conselheira

nomes = ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Rafael", "Juliana"]
responsaveis = ["tio", "tia", "avo", "primo", "outro"]
bairros = ["Centro", "Jardim", "Vila Nova", "Industrial"]
cidades = ["Cidade A", "Cidade B", "Cidade C"]
ruas = ["Rua 1", "Rua 2", "Rua 3"]
escolas = ["Escola Alfa", "Escola Beta", "Escola Gama"]

# Pega uma conselheira existente (ou None)
conselheira = Conselheira.objects.first()

for i in range(1, 71):
    nome = f"{random.choice(nomes)} Fictício {i}"
    numero = str(i).zfill(3)
    dn = date.today() - timedelta(days=random.randint(5000, 20000))
    assistido = Assistido.objects.create(
        nmcompleto_assist=nome,
        numero_assist=numero,
        dn_assist=dn,
        nmgenitor_assist="Genitor Teste",
        nmgenitora_assist="Genitora Teste",
        nmresponsavel_assist=random.choice(responsaveis),
        outro_responsavel="Outro Teste" if random.choice(responsaveis) == "outro" else "",
        escola_assist=random.choice(escolas),
        rua_assist=random.choice(ruas),
        bairro_assist=random.choice(bairros),
        cidade_assist=random.choice(cidades),
        numerocasa_assist=str(random.randint(1, 999)),
        id_conselheira=conselheira,
        gestante_assist=bool(random.getrandbits(1)),
        arquivado_assist=False,
        arquivomorto_assist=False,
    )
    Telefone.objects.create(
        id_assist=assistido,
            numero_telefone=f"(99) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}",
            obs_telefone="Telefone fictício"
    )
print("70 assistidos fictícios criados!")