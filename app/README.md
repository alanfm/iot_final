# Instalação do Laravel

## Usando Docker

Fazer os comando no terminal e ter o docker instalado na máquina

1. Fazer o clone no repositório

```shell
git clone git@github.com:alanfm/iot_final.git
```

2. Entrar no diretório do aplicativo

```shell
cd iot_final/app
```

4. Fazer a cópia do arquivo de configuração do Laravel

```shell
cp .env.example .env
```

5. Fazer a instalação dos pacotes do Laravel

```shell
docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$(pwd):/var/www/html" \
    -w /var/www/html \
    laravelsail/php83-composer:latest \
    composer install --ignore-platform-reqs
```


5. Subir os containers do Docker para o Laravel (PHP e Banco de dados)

```shell
./vendor/bin/sail up -d
```

* Se preferir, crie um alias para o comando ``sail``.
  * Edit o arquivo de configuração do bash
    ```shell
    nano .bashrc
    ```
  * Adicione a seguinte linha nos alias do bash
    ```shell
    alias sail='sh $([ -f sail ] && echo sail || echo vendor/bin/sail)'
    ```
  * Salve as alterações e execute o seguinte comando no terminal
    ```shell
    source ~/.bashrc
    ```
  * Agora você pode usar o comando ``sail`` no terminal
    ```shell
    # Exemplo
    sail up -d
    ```

1. Gerar a chave de segurança do Laravel

```shell
./vendor/bin/sail artisan key:generate
```

7. Fazer a migração do banco de dados e povoar com dados fake

```shell
./vendor/bin/sail artisan migrate:fresh --seed
```

8. Instalar os pacotes do javascript

```shell
./vendor/bin/sail npm install
```

9. Fazer a compilação dos arquivos do javascript

```shell
./vendor/bin/sail npm run build
```

* No desenvolvimento da interface usar o comando
    ```shell
    ./vendor/bin/sail npm run dev
    ```

1.   Acessar o app pelo seguinte link: http://localhost/
     * Quando tiver o usando o ``ngrok`` mudar o valor de ``APP_URL`` no arquivo de configuração do Laravel (``.env``), para o endereço gerado e refazer o comando do item 9.
