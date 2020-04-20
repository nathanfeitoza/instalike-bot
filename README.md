# Instalike Bot

Bot para conseguir seguidores do instalike

## Configurações

#### Requisitos

* Python3
* Selenium
    ```
    pip install -U selenium
    ```
* dotenv
    ```
     pip install -U python-dotenv
    ```

#### Configurar .env

Criar o arquivo .env com as seguintes configurações:

```
INSTAGRAM_LOGIN=login do instagram
INSTAGRAM_PASS=senha do instagram
INSTALIKE_EMAIL=email do instalike
INSTALIKE_PASS=senha do instalike
```

### Como iniciar

Após realizada as configurações acima, basta somente rodar o comando abaixo:

```
python3 init.py
```