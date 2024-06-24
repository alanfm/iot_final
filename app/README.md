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

10.   Acessar o app pelo seguinte link: http://localhost/
     * Quando tiver o usando o ``ngrok`` mudar o valor de ``APP_URL`` no arquivo de configuração do Laravel (``.env``), para o endereço gerado e refazer o comando do item 9.

## Instalação do Nginx e PHP 8.3 no Ubuntu

1. Instalando o Nginx

```shell
sudo apt install nginx
```

  * Adicionar o domínio do meu site
```shell
sudo nano /etc/nginx/sites-available/mysite
```

  * Adicionar essas configurações no arquivo e fazer as modificações necessárias
```nginx
server {
        listen 80;
        listen [::]:80;
        # SSL configuration
        # listen 443 ssl default_server;
        # listen [::]:443 ssl default_server;
        # Set root directive with your /public Laravel directory
        root /var/www/app/public;
        # Set index directive with index.php
        index index.php;
        # Set server_name directive with the hostname
        server_name mysite.dev;
        location / {
                try_files $uri $uri/ /index.php?$query_string;
        }
        # pass PHP scripts to FastCGI server
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
        }
        location ~ /\.ht {
                deny all;
        }
}
```

* Crie um link simbólico para o arquivo de configuração

```shell
ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/
```


1. Adicionado o repositório

```shell
sudo add-apt-repository ppa:ondrej/php && \
sudo apt update
```

2. Atualizado os pacotes

```shell
sudo apt-get update && sudo apt-get upgrade -y
```

3. Instala do PHP e seus módulos

```shell
sudo apt-get install -y zip unzip php8.3-cli php8.3-dev \
       php8.3-pgsql php8.3-sqlite3 php8.3-gd \
       php8.3-curl \
       php8.3-imap php8.3-mysql php8.3-mbstring \
       php8.3-xml php8.3-zip php8.3-bcmath php8.3-soap \
       php8.3-intl php8.3-readline \
       php8.3-ldap \
       php8.3-msgpack php8.3-igbinary php8.3-redis php8.3-swoole \
       php8.3-memcached php8.3-pcov php8.3-imagick php8.3-xdebug
```

4. Instalando o Composer

```shell
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
```

```shell
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```

```shell
php composer-setup.php
```

```shell
php -r "unlink('composer-setup.php');"
```

```shell
sudo mv composer.phar /usr/local/bin/composer
```

5. Reiniciar o nginx e acessar o site

```shell
sudo service nginx restart
```
