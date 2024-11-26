# Smart Environment
> System for monitoring lighting and air conditioning in environments

The developed project consists of implementing a Smart Environment using IoT and AI concepts. In this environment, we can control access, lighting, and air conditioning through a Web application for Smartphones (Android and iOS) and computers. In addition, the solution includes a monitoring system for data from luminosity, humidity, and temperature sensors in an environment. Data collection is performed by the sensors in the environment and sent to an edge device server. These data are used and applied to the AI developed for alert management and decision-making. This allows monitoring the average illuminance of the location, temperature, and humidity to detect potential failures and automate maintenance actions, optimizing the maintenance services of the environments.

## Hardware
Below, we briefly present the hardware devices used in the project. All devices were chosen to ensure the best cost-benefit ratio in terms of price and features offered. As an edge device, we chose a Raspberry Pi Model 3 b+ as an MQTT server with the Mosquitto broker, as well as a server with an Edge Computing architecture for other applications. For this purpose, Mosquitto, Python3, and Ngrok (to establish a temporary external connection for online demonstrations) were configured on the device. However, if the institution has infrastructure and a public IP available, it is recommended to use them for implementation. To improve the device's performance during installation and operation, an overclocking of 1,400 MHz was applied.

For the actuators, we used SONOFF and SmartIR hardware, which offer a DIY (Do-It-Yourself) mode and allow the firmware to be replaced with another chosen by the developer. For access control, we have two types of electronic locks: one with a 12V solenoid and mechanical memory (pulse of 10 ms to 100 ms) and another with a 12V electromagnet that remains closed when energized and opens when de-energized.

The average illuminance of the location is measured using an LDR (Light Dependent Resistor) sensor. The LDR is a passive electronic component of the variable resistor type, specifically a resistor whose resistance varies according to the light intensity that falls on it. The data is collected through the LDR sensor with a voltage divider using a logarithmic function, measured by an analog channel of the Arduino Nano, and sent via serial to the Raspberry Pi. The circuit schematic is available in the repositories. The temperature and humidity readings of the environment are performed using the DTH11 sensor. The DHT11 is a low-cost digital sensor used for measuring air humidity and temperature, operating in the range of 0 to 50 °C and 20% to 90% humidity. In this project, the sensor sends data directly to the Raspberry Pi.

## Software
The system used for managing and accessing data in this project was developed as a Web application for Mobile and Desktop access. The front end of the application uses the React JS library \ A JavaScript library for building user interfaces, and the Tailwind CSS framework, a CSS framework aimed at design creation. The backend was developed using the Laravel framework, a PHP framework for backend, and the MariaDB relational database. Additionally, several scripts were developed for the proposed solution to enable communication between the equipment involved in the prototype. A Python script was developed for reading the DHT11 sensors and serial input with luxmeter data. On the Arduino Nano, another script converts these analog data into lux values and sends them to the Raspberry Pi via serial. The implementation of the MQTT protocol with the adopted hardware was done using TASMOTA, an open-source firmware that facilitates quick and efficient implementation of the protocol on SONOFFs and SmartIRs. Finally, a bot was developed to send maintenance alerts via Telegram.

## Project Architecture
<div align="center"><img src="/figures/arquitetura.png" alt="image" width="400" height="auto"></div>

## Application
The Web application used to manage the actuators and sensors in the environment is illustrated below. Through the application interface, the user can control the status of the sensors and actuators. For each registered environment, the user can also determine and edit the default luminosity and temperature values. Finally, the application also displays sensor reading data through graphs updated with the database that collects these values.

<div align="center"><img src="/figures/app.png" alt="image" width="600" height="auto"></div>

## Alerts
The collected data and the status of the actuators and sensors are sent to the database. The trained AI analyzes this information and, based on the predefined data for the environment, makes decisions to trigger alerts. The alerts are sent to a bot on Telegram with information about the environment and the detected problem.

<div align="center"><img src="/figures/bot.png" alt="image" width="400" height="auto"></div>

## Project Documentation Overview
The documentation, scripts, and important information are organized as follows in the repository:

SCRIPTS: Includes the firmware scripts for the Arduino Nano luxmeter, Raspberry Pi sensor reading scripts, and data analysis scripts for decision-making by the trained AI.
SCHEMATICS: Circuit schematic with the LDR sensor and voltage divider for lux data reading and the circuit for the Raspberry Pi input operating at 3.3V.
app: Repository with backend and frontend scripts for the WEB application.
figures: All figures used to present the system.
dataset: Repository with scripts for generating artificial data, training AI algorithms, and the trained AI file to be deployed on the Raspberry Pi.
Important Notes
Detailed information regarding applications (e.g., hyperparameters of the neural network that achieved the best results) is presented in the scripts with proper comments.
The firmware used in the actuators is open-source and provided by TASMOTA, for both relay and infrared actuators.


# Smart Environment
>Sistema de monitoramento de iluminação e climatização de ambientes

O projeto desenvolvido consiste na implementação de um _Smart Enviroment_ utilizando conceitos de IoT e IA. Neste ambiente, podemos realizar o controle de acesso, iluminação e climatização por meio de uma aplicação Web, para _Smartphones_ (Android e iOS) e computadores. Além disso, a solução conta com um sistema de monitoramento de dados de sensores de luminosidade, umidade e temperatura de um ambiente. A coleta dos dados é realizada pelos sensores presentes no ambiente, que são enviadas para um servidor dispositivo de borda. Esses dados são utilizados e aplicados na IA desenvolvida para gestão dos alertas e envio das tomadas de decisão. Desta forma, podemos monitorar a iluminância média do local, temperatura e umidade com o objetivo de detectar possíveis falhas para acionar o setor de manutenção de forma automatizada, otimizando serviços de manutenção dos ambientes. 

## Hardware
A seguir iremos apresentar brevemente os dispositivos de hardware utilizados no projeto, onde todos os dispositivos foram escolhidos visando o melhor custo benefício em termos de valor aquisitivo e recursos oferecidos. Como dispositivo de borda escolhemos um Raspberry Pi Modelo 3 b+ como um servidor MQTT com broker Mosquitto, assim como um servidor com arquitetura de Edge Computing para outras aplicações. Para isso, foram configurados no dispositivo o Mosquitto, Python3 e Ngrok (para estabelecer uma conexão externa temporária para demonstração na internet). No entanto, caso a instituição disponha de infraestrutura e IP público disponível recomenda-se usá-los para implementação. Para melhorar o desempenho do dispositivo na instalação e operação, foi realizado um overclock para 1.400 MHz no dispositivo.

Para os atuadores utilizamos os hardwares SONOFF e SmartIR que oferecem o modo DIY (Do-It-Yourself) e permitem que o firmware seja substituído por outro de escolha do desenvolvedor. No controle de acesso, temos dois tipos de tranca eletrônica, uma com solenóide 12V e memória mecânica (pulso de 10 ms a 100 ms) e outra com eletroimã também com tensão de acionamento de 12V que fica fechada quando energizada e aberta quando desernegizada.

A iluminância média do local é aferida usando um sensor de luminosidade LDR (Light Dependent Resistor). O LDR é um componente eletrônico passivo do tipo resistor variável, mais especificamente, é um resistor cuja resistência varia conforme a intensidade da luz que incide sobre ele. Os dados são coletados através do sensor LDR com divisor de tensão por meio de uma função logarítmica, este é aferido por um canal analógico do Arduino Nano e enviado via serial para o Raspberry Pi. O esquemático do circuito está disponível nos repostórios. Já a leitura dos dados de temperatura e umidade do ambiente foram realizadas através do sensor DTH11. O DHT11 é um sensor digital de baixo custo usado para medição de umidade e temperatura do ar, atua com temperatura na faixa de 0 a 50 °C e umidade de 20\% a 90\%. Neste projeto, tal sensor envia os dados diretamente para o Raspberry PI.

## Software
O sistema usado para o gerenciamento e acesso dos dados deste projeto foi desenvolvido como uma aplicação Web, para acesso via Mobile e Desktop. O front da aplicação utiliza a biblioteca React JS \ Biblioteca JavaScript para criar interfaces de usuário e o framework Tailwind CSS. Um framework CSS voltado para criar design. O backend foi desenvolvido utilizando o framework Laravel. Um framework em PHP para backend e o banco de dados relacional MariaDB. Além disto, para a solução proposta neste projeto foram desenvolvidos alguns scripts para permitir a integração e funcionamento da comunicação entre os equipamentos envolvidos no protótipo. Para leitura dos sensores DHT11 e a entrada serial com os dados do luxímetro foi desenvolvido um script em Python. No Arduino Nano, através de um script esses dados analógicos são convertidos em valores de lux e enviados para o RPI via serial. A implementação do protocolo MQTT com os hardwares adotados foi feita com o TASMOTA, um firmware de código aberto que facilita a implementação do protocolo de forma rápida e eficiente em SONOFF's e SmartIR's. Por fim, também foi desenvolvido um bot para o envio dos alertas de manutenção via Telegram. 


## Arquitetura do Projeto
<div align="center"><img src="/figures/arquitetura.png" alt="image" width="400" height="auto"></div>

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

---
<!-- 
# Smart Environment
> Lighting and Air Conditioning Monitoring System for Environments

The developed project consists of the implementation of a _Smart Environment_ using IoT and AI concepts. In this environment, we can control access, lighting, and air conditioning through a Web application for _Smartphones_ (Android and iOS) and computers. Additionally, the solution includes a system for monitoring data from light, humidity, and temperature sensors in an environment. Data collection is carried out by the sensors present in the environment, which are sent to an edge server device. These data are used and applied to the AI developed for alert management and decision-making. In this way, we can monitor the average illuminance of the place, temperature, and humidity with the aim of detecting possible failures to automatically trigger the maintenance sector, optimizing the maintenance services of the environments.

## Project Architecture
<div align="center"><img src="/figures/arquitetura.png" alt="image" width="400" height="auto"></div>

## Application
The Web application used to manage the actuators and sensors utilized in the environment is illustrated below. Through the application's interface, the user can control the status of sensors and actuators. For the control of each registered environment, the user can also determine and edit the standard values for brightness and temperature. Finally, the application also presents the sensor reading data through updated graphs with the database that collects these values.
<div align="center"><img src="/figures/app.png" alt="image" width="600" height="auto"></div>

## Alerts
The collected data and the status of the actuators and sensors are sent to the database. Thus, the already trained AI analyzes this information, and according to the data set as the environment standard, it makes the decision to trigger alerts. The alerts are sent to a bot on Telegram with the environment data and the identified problem.
<div align="center"><img src="/figures/bot.png" alt="image" width="400" height="auto"></div>

## Project Documentation Description

The documentation, scripts, and important information are organized as follows in the repository:

- SCRIPTS: Contains the scripts used in the Arduino Nano firmware for the luxmeter, Raspberry Pi scripts for sensor reading, and data analysis on the device for AI decision-making;
- SCHEMATICS: Schematic of the circuit assembled with the LDR sensor with a voltage divider for data reading later converted into lux and the circuit for the Raspberry Pi input which operates at 3.3V;
- app: Repository with backend and frontend scripts of the WEB application;
- figures: All figures used to present the system;
- dataset: Repository with scripts for generating artificial data, training AI algorithms, and a file with the trained AI to embed in the Raspberry Pi.

## Important Observations

- All detailed information regarding the application details (e.g., hyperparameters of the neural network that achieved the best results) is presented in the scripts with the appropriate comments.
- The firmware used in the actuators is open-source provided by TASMOTA, both for relay actuators and the infrared actuator. -->
