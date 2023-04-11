# Bot Telegram

Trabalho desenvolvido na disciplina Algoritmos de Automação, ministrada pelo professor 
Álvaro Justen (@turicas), no Master em Jornalismo de Dados do Insper. 

##O projeto
O projeto consiste em criar uma ferramenta para administrar facilmente o telegram no Django. O código foi baseado na estrutura da lib python-telegram-bot.
O meu desafio era encontrar uma forma de simplificar a estrutura, sobretudo na parte de conversas entre o usuário e o bot - que é bastante complexa na lib original. A ideia é criar uma ferramenta simples e facilmente escalável para eu adicionar novas funcionalidades ao bot. 

## Docker
O projeto está estrutura em Docker. 
Para rodar, basta instalar o Docker no PC/Mac. No terminal de comando, escreva na pasta em que você baixou os arquivos do repositório git: 
- `docker-compose build` (para criar os conteineres)
- `docker-compose up -d` (para iniciar o sistema com a flag d, o que significa que o terminal ficará livre - detached)

## Django
O site usa o framework python Django para controlar o bot. A ideia é que seja uma ferramenta para trabalhar com sites e, futuramente, ser compatível também com o Flask. 

## Variáveis de ambiente. 
Antes de rodar o programa, é necessário criar dois arquivos `.env`.

Este é o primeiro, dentro da pasta app, que vai alimentar o django:

```
POSTGRES_USER
POSTGRES_PASSWORD=
POSTGRES_DB=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=


#django
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

#Telegram Token
TOKEN=
```

Este é o segundo arquivo `.env`, responsável por definir as variáveis do Postgres no Docker. 
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

## Ngrok
Para testar o Telegram durante o desenvolvimento, é preciso criar um link online. Isso é bem simples de fazer com o Ngrok. Basta instalar o programa e rodar 'ngrok http 8000' no terminal (assim ele deixará online a porta 8000, a mesma que usamos para o Django), pegar o url criado e passar para o webhook.
