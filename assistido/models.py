from django.db import models


class Assistido(models.Model):
    id_assist = models.AutoField(primary_key=True)
    nmcompleto_assist = models.CharField(max_length=255)
    numero_assist = models.CharField(max_length=50, blank=True, null=True)
    dn_assist = models.DateField()  # Data de nascimento
    nmgenitor_assist = models.CharField(max_length=255, blank=True, null=True)
    nmgenitora_assist = models.CharField(max_length=255, blank=True, null=True)

    DTCADASTRO = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')

    # Tipo de responsável (padrão com opções e campo "outro")
    TIPOS_RESPONSAVEL = [
        ("tio", "Tio"),
        ("tia", "Tia"),
        ("avo", "Avô/Avó"),
        ("primo", "Primo/Prima"),
        ("outro", "Outro"),
    ]
    nmresponsavel_assist = models.CharField(
        max_length=50, choices=TIPOS_RESPONSAVEL, default="outro"
    )
    outro_responsavel = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Preencher se o tipo do responsável for 'Outro'."
    )

    escola_assist = models.CharField(max_length=255, blank=True, null=True)
    rua_assist = models.CharField(max_length=255, blank=True, null=True)
    bairro_assist = models.CharField(max_length=100, blank=True, null=True)
    cidade_assist = models.CharField(max_length=100, blank=True, null=True)
    numerocasa_assist = models.CharField(max_length=20, blank=True, null=True)
    nm_conselheiro = models.CharField(max_length=255, blank=True, null=True)

    gestante_assist = models.BooleanField(default=False)
    arquivomorto_assist = models.BooleanField(default=False)
    filaarquivomorto_assist = models.BooleanField(default=False)
    dtarquivomorto_assist = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nmcompleto_assist


class Irmaos(models.Model):
    id_irmaos = models.AutoField(primary_key=True)
    id_assist_1 = models.ForeignKey(
        Assistido,
        on_delete=models.CASCADE,
        related_name="irmao1"
    )
    id_assist_2 = models.ForeignKey(
        Assistido,
        on_delete=models.CASCADE,
        related_name="irmao2"
    )

    def __str__(self):
        return f"Irmãos: {self.id_assist_1} e {self.id_assist_2}"


class Telefone(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    id_assist = models.ForeignKey(
        Assistido,
        on_delete=models.CASCADE,
        related_name="telefones"
    )
    numero_telefone = models.CharField(max_length=20)
    obs_telefone = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_telefone} ({self.id_assist})"
