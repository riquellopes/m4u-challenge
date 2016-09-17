Documentação
============

O app bookmark foi dividido em 2 projetos, o **BookmarkWeb** onde foi criada uma aplicação com [Django](https://www.djangoproject.com/), que serve todo conteúdo web.
O **BookmarkApi** é uma aplicação [Nodejs](https://nodejs.org/en/)+[Expressjs](http://expressjs.com/pt-br/)+[Mongodb](https://www.mongodb.com/)
que vai gerenciar toda a criação de novos bookmarks e usuários.
Para orquestrar todos esses serviços eu utilizei [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/). Estando com tudo configurado corretamente, basta execupar o comando
abaixo.

```bash
    $ docke-compose up

    # No MacOsx a primeira vez
    $ docker-machine start
    $ docker-machine env
    $ eval $(docker-machine env)

    $ docke-compose up or docke-compose stop
```
### Variavéis de Ambiente
- DB_NAME
- DB_USER
- DB_PASS
- DB_HOST
- BOOKMARK_API
- BOOKMARK_DEFAULT_PASS
- MONGO_URI
- TOKEN_SECRET
- PORT

### Comandos do BookmarkWeb
```bash

    $ make setup-local # Cria setup para o ambiente de desenvolvimento.
    $ make create-db # Cria banco.
    $ make migrate # Criar tabelas.
    $ make debug # Executar projeto em modo debug.
    $ make test # Executar test
    $ make test-cov # Executar test com coverage
    $ make createsuperuser-bookmark # Criar admin
    $ make shell # Entra no modo shell django
```

### Executar Teste BookmarkWeb
```bash
    $ make test
```

### Comandos do BookmarkApi.
```bash
    $ npm test or make test
```
