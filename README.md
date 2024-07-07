# Smart Environment
>Sistema de monitoramento de iluminação e climatização de ambientes

O projeto desenvolvido consiste na implementação de um _Smart Enviroment_ utilizando conceitos de IoT e IA. Neste ambiente, podemos realizar o controle de acesso, iluminação e climatização por meio de uma aplicação Web, para _Smartphones_ (Android e iOS) e computadores. Além disso, a solução conta com um sistema de monitoramento de dados de sensores de luminosidade, umidade e temperatura de um ambiente. A coleta dos dados é realizada pelos sensores presentes no ambiente, que são enviadas para um servidor dispositivo de borda. Esses dados são utilizados e aplicados na IA desenvolvida para gestão dos alertas e envio das tomadas de decisão. Desta forma, podemos monitorar a iluminância média do local, temperatura e umidade com o objetivo de detectar possíveis falhas para acionar o setor de manutenção de forma automatizada, otimizando serviços de manutenção dos ambientes. 

## Arquitetura do Projeto
<div align="center"><img src="/figures/arquitetura_iot.png" alt="image" width="400" height="auto"></div>

## Aplicação
A aplicação Web usada para gerenciar os atuadores e sensores utilizados no ambiente é ilustrada abaixo. Através da interface do aplicativo o usuário pode controlar os status do sensores e atuadores. Para o controle de cada ambiente cadastrado o usuário também pode determinar e editar os valores de luminosidade e temperatura padrão. Por fim, a aplicação também apresenta os dados de leituras dos sensores através de gráficos atualizados com o banco de dados que coleta esses valores. 
<div align="center"><img src="/figures/app.png" alt="image" width="600" height="auto"></div>

## Alertas
Os dados coletadores e os status dos atuadores e sensores são enviados para o banco
de dados. Desta forma a IA, já treinada, analisa essas informações e de acordo com os dados
setados como padrão do ambiente a mesma realiza a tomata de decisão para disparar os alertas.
Os alertas são enviados para um bot no Telegram com os dados do ambiente e o problema
encontrado. 
<div align="center"><img src="/figures/bot.png" alt="image" width="400" height="auto"></div>

## Observações Importantes

Todas as informações detalhadas do que diz respeito a detalhamento das aplicações (Ex: hiperparÂmetros da rede neural que obteve melhores resultados) são apresentadas nos scripts com os devidos comentários.


## Descritivo dos Scripts do Projeto

- Script para gerara dataset: generate_dataset.py;
- Scripts do dispositivo de borda (IA e sensores): script_ia_ok.py and script_raspberry_sensores.py;
- Script do arduino nano: luximetro_arduinoNano.ino; 
- Script de treinamento da IA: projeto_final_iot_mlp.ipynb; 
- Dataset com dados artificiais: database_iot_pf.csv;  
- Esquemático do luxímetro: Esquematico_luximetro.pdf; 
- Arquivo com IA treinada: mlp_smart_enviroument.joblib.