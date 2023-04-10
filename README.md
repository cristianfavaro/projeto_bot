# Projeto Bot Telegram

O projeto consiste em criar uma ferramenta para administrar facilmente o telegram no Django. O código foi baseado na estrutura iniciarl da lib python-telegram-bot, que é amplamente utilizada.
O meu desafio era encontrar uma forma de simplificar a estrutura, sobretudo na parte de conversas entre o usuário e o bot - que é bastante complexa na lib original. 


# Docker
O projeto está estrutura em Docker. 
Para rodar, basta instalar o Docker no PC/Mac.
No terminal de comando, escreva: 
- `docker-compose build` (para criar os conteineres)
- `docker-compose up -d` (para iniciar o sistema com a flag d, o que significa que o terminal ficará livre - detached)

## Ngrok

Para testar o Telegram durante o desenvolvimento, é preciso criar um link online. Isso é bem simples de fazer com o Ngrok. Basta instalar o programa e rodar 'ngrok http 8000' no terminal (assim ele deixará online a porta 8000, a mesma que usamos para o Django), pegar o url criado e passar para o webhook.