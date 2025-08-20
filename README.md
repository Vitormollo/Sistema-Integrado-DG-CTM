# Sistema Integrado DG-CTM

## Como rodar o projeto localmente

1. **Ative o ambiente virtual**

No terminal, navegue até a pasta do projeto e execute:

```
venv\Scripts\activate
```

2. **Instale as dependências**

Se ainda não instalou, rode:

```
pip install -r requirements.txt
```

3. **Inicie o servidor Django**

```
python manage.py runserver
```

4. **Acesse no navegador**

Abra: http://127.0.0.1:8000/

5. **Criar um superusuário (admin)**

No terminal, execute:

```
python manage.py createsuperuser
```

Siga as instruções para definir usuário, email e senha. Depois, acesse http://127.0.0.1:8000/admin/ para entrar no painel administrativo.

---

Se precisar criar o ambiente virtual (caso não exista a pasta `venv`):

```
python -m venv venv
```

Depois, repita o passo 1.
