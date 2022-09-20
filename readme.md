<h1 align="center">
BandKamp
</h1>

## 💻 Projeto

Aplicação de porfolio.

## 🔨 Implementações

- [x] CRUD Artistas
- [x] CR Albums
- [x] CR Músicas
- [x] Filtros
- [x] Paginação
- [x] Postgres

## 🎨 Layout

Para essa aplicação, não foi utilizado figma

## ✨ Tecnologias

- [x] Django
- [x] Django Rest Framework
- [x] Django Filter
- [x] Model Bakery
- [x] CI CD

## 🌐 Deploy

[Link do deploy](https://band-kamp-caio.herokuapp.com/api/schema/swagger-ui/)

# Instruções:
 
### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash
# linux: 

source venv/bin/activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Execute as migrações
```
./manage.py migrate
```
### Rode a aplicação
```
./manage.py runserver
```
