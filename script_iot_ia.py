# import Adafruit_DHT
import time
import requests
import serial
import joblib
import numpy as np
import telepot
import generate_dataset as gd
"""
Script configurado para rodar em máquina virtual do python
source /home/mosquitto/sklearn-env/bin/activate

OBS.: Todas as bibliotecas para rodar o script estão instalados nesta máquina.
"""
"""
Informações para o Thinkspeak
Link para instalação do pacote: https://www.makerhero.com/blog/raspberry-pi-e-thingspeak/
ID Chanel: 2580016
WRite API: WD8CEEVP3R51MSXM
Read API: NIXUZIPO28NMV61B

O dataset tem dois campos:
- field1: label;
- field2: id_amb.
"""

""" 
Instalação do telepot - comandos.
$ pip3 install telepot
$ pip3 install telepot --upgrade  # UPGRADE
"""

"""
Informações de versão das bibliotecas usadas no treinamento do modelo .joblib
NumPy version: 1.25.2
scikit-learn version: 1.5.0
joblib version: 1.4.2
"""

# criando insancia do telepot para envio de msg via telegram
bot = telepot.Bot('7221900994:AAGfe6-AIACarNB9XisZH553VGn31xaSrj8')
chat_id = 5597495193

# URL para API GET e POST
URL = 'https://0c74-191-7-192-77.ngrok-free.app/'
POST = URL+'/sensor/all' #url para get via http dos dados
GET = URL+'/env/all' #url para get via http dos dados


# Configurações do sensor
# sensor = Adafruit_DHT.DHT11
pino_sensor = 25  # Número do pino GPIO onde o sensor está conectado

# Configuração da porta serial
# ser = serial.Serial(
#     port='/dev/serial0',  # Porta serial 
#     baudrate=115200,      
#     timeout=1            
# )

def generateDataSensorRandom(lux,temp):
  # variáveis para coletar os dados dos sensores
  # sensores = gd.generateData(l)
  lux_s = gd.getLuxSensor(lux)
  temp_s = gd.getTempSensor(temp)
  hum_s = gd.getHumiditySensor()
  # dados dos sensores para post
  data_post = {
          'lux_value': lux_s,
          'hum_value': hum_s,
          'temp_value': temp_s
          }
  return lux_s,temp_s,hum_s,data_post

def postData(post, data):
  try:
      # Enviar POST request
      response = requests.post(post, json=data)

      # Verificar a resposta
      if response.status_code == 201:
          print(f"POST realizado com sucesso para {post}")
      else:
          print(f"Falha ao enviar POST. Código de status: {response.status_code}")
  except requests.exceptions.RequestException as e:
      print(f"Erro durante o POST request: {e}")
      
# função get para coletar os dados do banco de dados
def getData(get, lux, hum, temp):
  # realizando requisição GET
    r = requests.get(get) # executa o get para coleta de dados
    print(r)
        
    time.sleep(1)
    # verifica conexão e salva em variáveis os dados coletados via API
    if r.status_code == 200:
        # Analisar a resposta JSON
        data = r.json()
        env_lux = data.get('env_lux')
        env_temp = data.get('env_temp')
        stat_lux = data.get('lux')
        stat_hum = data.get('hum')
        stat_temp = data.get('temp')
        door = data.get('door')
        light = data.get('light')
        air = data.get('air')
        lux_s = lux
        hum_s = hum
        temp_s = temp
        name = data.get('name')
        id = data.get('id')
        
        if light == False:
          lux_s = 0
        if stat_lux == False:
          lux_s = 0
        if stat_hum == False:
          hum_s = 0
        if stat_temp == False:
          temp_s = 0
        
        # inserimos todas as variáveis em uma lista para implementar no modelo de IA treinado
        features = [lux_s, hum_s, temp_s, stat_lux, stat_hum, stat_temp, door, light, air, env_temp, env_lux]
        print(features)
        return features, name, id
      
# função para realizar as previsoes
def predictions(get,lux,hum,temp):
  # Carregando o modelo 
  modelo = joblib.load('/home/geraldo/Documentos/python_projects/iot-ia/mlp_smart_enviroument.joblib')
  # modelo = joblib.load('/home/mosquitto/modelo_treinado_mlp.joblib')
  # Fazendo a previsão
  features, name, id = getData(get, lux, hum, temp)
  features_array = np.array([features]) # transforma a lista em um array
  prediction = modelo.predict(features_array)
  
  # Mostrando o resultado
  print("\nFeatures via http e medições: "+str(features))
  print("\nPredição: "+str(prediction))
  return prediction
    
# função para tomada de decisões da IA
def decisionAI(prediction,name,id):
  # Tomada de decisões
    if prediction[0] == 0:
      print("Operação Normal")
    elif prediction[0] == 1:
      print("Falha climatização no ambiente "+str(name)+".")  # Enviar a tomada de decisões e o dataframe da falha para nuvem
      bot.sendMessage(chat_id=chat_id, text="Falha na climatização no ambiente "+str(name)+" (id: "+str(id)+").")
      thinksPeak(prediction[0],id)
    elif prediction[0] == 2:
      print("Falha na iluminação")  # Enviar a tomada de decisões e o dataframe da falha para nuvem
      bot.sendMessage(chat_id=chat_id, text="Falha na iluminação no ambiente "+str(name)+" (id: "+str(id)+").")
      thinksPeak(prediction[0],id)
    elif prediction[0] == 3:
      print("Falha iluminação e ar condicionado.")
      bot.sendMessage(chat_id=chat_id, text="Falha na iluminação e climatização do ambiente "+str(name)+" (id: "+str(id)+").")
      thinksPeak(prediction[0],id)
    else:
      print("Mensagem de teste..")

def thinksPeak(label,id_amb):
  # Defina a API key e os dados
  api_key = 'WD8CEEVP3R51MSXM'
  post = {
      'field1': id_amb,
      'field2': label,
  }
  
  url = f"https://api.thingspeak.com/update?api_key={api_key}"
  for field, value in post.items():
      url += f"&{field}={value}"
  # Fazer a requisição GET
  response = requests.get(url)

  if response.status_code == 200:
      return f"POST realizado com sucesso para {post}"
  else:
      return f"Falha ao enviar POST. Código de status: {response.status_code}"



# função para ler sensores via serial
def serialData():
  lux, hum, temp = 0
  data_post = {
          'lux_value': lux,
          'hum_value': hum,
          'temp_value': temp
          }
  # umid_s, temp_s = Adafruit_DHT.read_retry(sensor, pino_sensor) # faz a leitura do sensor DHT11
  #   if umid_s is not None and temp_s is not None:
  #       lux_s = 0
  #       if ser.in_waiting > 0:
  #           # Lê a linha da serial
  #           lux_s = ser.readline().decode('utf-8').rstrip() # faz a leitura do luximetro pela serial
  #           print(f"Iluminância: {lux_s}")
    
  #         print('Umidade: {0:0.1f}%'.format(umid_s))
  #         print('Temperatura: {0:0.1f}°C'.format(temp_s)
  # Efetua a leitura do sensor
  # umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
  #  # Caso leitura esteja ok, mostra os valores na tela
  # if umid is not None and temp is not None:
  #   lux_s = 0
  #   if ser.in_waiting > 0:
  #       # Lê a linha da serial
  #     lux_s = ser.readline().decode('utf-8').rstrip() # faz a leitura do luximetro pela serial
  #     print(f"\nIluminância: {lux_s}"+" lux")
  #   print ("\nTemperatura: "+str(temp));
  #   print ("\nUmidade: "+str(umid))
  #   print ("Aguarda 5 segundos para efetuar nova leitura...n");
  #   time.sleep(1)
  # else:
  #    # Mensagem de erro de comunicacao com o sensor
  #    print("Falha ao ler dados do DHT11 !!!")
  # print("Retorna dados da serial.")
  return lux,hum,temp,data_post

#bot telegram
def handle(msg):
  chat_id = msg['chat']['id']
  command = msg['text']
  print('got command: %s' % command)
  
# time.sleep(2)

while True:
    """ 
    Sequência das features para realização de testes:
    lux | humidity | temperature | ligthing_switch | climate_switch | door_actuator | lux_status | 
    humidity_status | temperature_status | enviroment_temperature | enviroment_lux
    """
    # gerando dados randomicos para teste
    l,h,t,data_post = generateDataSensorRandom(350,26)
    # coletando os dados dos sensores
    features, name, id = getData(GET,l,h,t)
    # enviado informações via request POST para banco de dados
    postData(POST, data_post)
    # realizando previsoes
    prediction = predictions(GET,l,h,t)
    # tomada de decisão da IA
    decisionAI(prediction, name, id)
    # bot.getUpdates()
    #delay de 1s
    time.sleep(1)