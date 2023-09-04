
## Criar repositorio virtual

```
python -m venv venv
```

## Ativar repositorio virtual

```
venv\Scripts\activate
```

## Desativar repositorio virtual

```
deactivate
```

## Instalar Django

```
pip install django
```

## Verificar versão Django

```
django -admin --version
```

## Criar coração do projeto

```
django-admin startproject app .
```

## Executa servidor\localhost

```
python manage.py runserver

http://localhost:8000/
```

## Trazer comandos para gerenciar o projeto

```
django-admin --help
```

## Importa as configurações do projeto

```
python manage.py test >> comando
```

## Criar app vazia

```
python manage.py startapp cars >> nome da app
```

## Criar migrations

```
python manage.py makemigrations
```

## Executar migration

```
python manage.py migrate
```

## Criar super usuario

```
python manage.py createsuperuser
```
## Gerar dependências do projeto \ Instalar dependências do projeto

```
pip freeze > requirements.txt
pip freeze -r .\requirements.txt
```
