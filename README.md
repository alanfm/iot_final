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

## Descritivo da Documentação do Projeto

A documentação, scripts e informações importantes estão organizadas da seguinte forma no repositório:

- SCRIPTS: Estão os scripts usados no firmware do arduino nano para o luxímetro, scripts do raspberry para leitura dos sensores e análise de dados no dispostivo para tomada de decisão da IA já treinada;
- SCHEMATICS: Esquemático do circuito montado com sensor LDR com divisor de tensão para leitura do dados posteriormente convertidos em lux e o circuito para entrada do raspberry pi que opera com 3,3V;
- app: Repositório com scripts do backend e frontend da aplicação WEB;
- figures: Todas as figuras utilizadas para apresentar o sistema;
- dataset: Respositório com scripts para geração dos dados artificiais, treinamento dos algoritmos de AI e arquivo com AI treinada para embarcar no raspberry pi.

## Observações Importantes

- Todas as informações detalhadas do que diz respeito a detalhamento das aplicações (Ex: hiperparÂmetros da rede neural que obteve melhores resultados) são apresentadas nos scripts com os devidos comentários.
- O firmware utilizado nos atuadores são opensource disponibilizados pela TASMOTA, tanto para os atuadores a relé como para o atuador infravermelho.