import time
import requests
import joblib
import numpy as np
import telepot
import generate_dataset as gd


"""
Script configurado para rodar em ambiente virtual do python
Script configured to run in Python virtual environment
source /home/mosquitto/sklearn-env/bin/activate

OBS.: Todas as bibliotecas para rodar o script estão instalados nesta máquina.
NOTE: All libraries to run the script are installed on this machine.
"""
"""
Informações para o Thinkspeak
Information for Thinkspeak
Link para instalação do pacote: https://www.makerhero.com/blog/raspberry-pi-e-thingspeak/
Link to install the package: https://www.makerhero.com/blog/raspberry-pi-e-thingspeak/
ID Chanel: 2580016
WRite API: WD8CEEVP3R51MSXM
Read API: NIXUZIPO28NMV61B

O dataset tem dois campos:
The dataset has two fields:
- field1: label;
- field2: id_amb.
"""

""" 
Instalação do telepot - comandos.
Telepot installation - commands.
$ pip3 install telepot
$ pip3 install telepot --upgrade  # UPGRADE
"""

"""
Informações de versão das bibliotecas usadas no treinamento do modelo .joblib
Version information of libraries used in training the .joblib model
NumPy version: 1.25.2
scikit-learn version: 1.5.0
joblib version: 1.4.2
"""

# criando insancia do telepot para envio de msg via telegram
# creating telepot instance for sending messages via telegram
bot = telepot.Bot('7221900994:AAGfe6-AIACarNB9XisZH553VGn31xaSrj8')
chat_id = 5597495193

# URL para API GET e POST criada a partir do ngrok; comando ngrok http http://localhost:80
# URL for GET and POST API created using ngrok; command ngrok http http://localhost:80
URL = 'https://e067-200-129-37-2.ngrok-free.app/'
POST = URL+'/sensor/all' 	#url para get via http dos dados
				      # URL for GET via http for the data
GET = URL+'/env/all' 	#url para get via http dos dados
			      # URL for GET via http for the data
      
# função get para coletar os dados do banco de dados
# get function to collect data from the database
def getData(get):
  # realizando requisição GET
  # making GET request
    r = requests.get(get) 	# executa o get para coleta de dados
    				      # performs the GET to collect data
    print(r)
        
    time.sleep(1)
    # verifica conexão e salva em variáveis os dados coletados via API
    # checks connection and saves collected data via API in variables
    if r.status_code == 200:
        # Analisar a resposta JSON
        # Analyzing the JSON response
        data = r.json()
        print("Tipo do r.json: "+str(data))
        env_lux = data['env_lux']
        env_temp = data['env_temp']
        stat_lux = data['lux']['status']
        stat_hum = data['hum']['status']
        stat_temp = data['temp']['status']
        door = data['door']['status']
        light = data['light']['status']
        air = data['air']['status']
        lux_s = data['lux']['value']
        hum_s = data['hum']['value']
        temp_s = data['temp']['value']
        name = data.get('name')
        id = data.get('id')
        
        # Condições para habilitar ou desativar os sensores e coleta de dados
        # Conditions to enable or disable sensors and data collection
        if light == False:
          lux_s = 0
        if stat_lux == False:
          lux_s = 0
        if stat_hum == False:
          hum_s = 0
        if stat_temp == False:
          temp_s = 0
        
        # inserimos todas as variáveis em uma lista para implementar no modelo de IA treinado
        # we insert all variables into a list to implement in the trained AI model
        features = [lux_s, hum_s, temp_s, stat_lux, stat_hum, stat_temp, door, light, air, env_temp, env_lux]
        print(features)
        return features, name, id
      
# função para realizar as previsoes
# function to make predictions
def predictions(get):
  # Carregando o modelo 
  # Loading the model
  modelo = joblib.load('/home/geraldo/Documentos/python_projects/iot-ia/mlp_smart_enviroument.joblib')
  # modelo = joblib.load('/home/mosquitto/modelo_treinado_mlp.joblib')
  # Fazendo a previsão
  # Making the prediction
  features, name, id = getData(get)
  features_array = np.array([features])   # transforma a lista em um array
  					            # transforms the list into an array
  prediction = modelo.predict(features_array) 	# realiza as predições
  						            # makes the predictions
  
  # Mostrando o resultado
  # Showing the result
  print("\nFeatures via http e medições: "+str(features))
  print("\nPredição: "+str(prediction))
  return prediction
    
# função para tomada de decisões da IA
# function for AI decision making
def decisionAI(prediction, name, id):
  # Tomada de decisões
  # Decision making
    if prediction[0] == 0:
      print("Operação Normal")
    elif prediction[0] == 1:
      bot.sendMessage(chat_id=chat_id, text="Falha na climatização no ambiente "+str(name)+" (id: "+str(id)+").")
      print("Falha climatização no ambiente "+str(name)+".")  	# Enviar a tomada de decisões e o dataframe da falha para nuvem
      								# Send the decision making and the failure dataframe to the cloud
      thinksPeak(prediction[0], id)
    elif prediction[0] == 2:
      print("Falha na iluminação")  	# Enviar a tomada de decisões e o dataframe da falha para nuvem
      					# Send the decision making and the failure dataframe to the cloud
      bot.sendMessage(chat_id=chat_id, text="Falha na iluminação no ambiente "+str(name)+" (id: "+str(id)+").")
      thinksPeak(prediction[0], id)
    elif prediction[0] == 3:
      print("Falha iluminação e ar condicionado.")
      bot.sendMessage(chat_id=chat_id, text="Falha na iluminação e climatização do ambiente "+str(name)+" (id: "+str(id)+").")
      thinksPeak(prediction[0], id)
    else:
      print("Mensagem de teste..")
      # Test message

# Função para envio de dados ao thinkspeak
# Function to send data to ThinkSpeak
def thinksPeak(label, id_amb):
  # Defina a API key e os dados
  # Define the API key and data
  api_key = 'WD8CEEVP3R51MSXM'
  post = {
      'field1': id_amb,
      'field2': label,
  }
  # url para realizar post no canal do thinkspeak criado
  # URL to perform POST on the created ThinkSpeak channel
  url = f"https://api.thingspeak.com/update?api_key={api_key}"
  for field, value in post.items():
      url += f"&{field}={value}"
  # Fazer a requisição GET
  # Make the GET request
  response = requests.get(url)

  if response.status_code == 200:
      return f"POST realizado com sucesso para {post}"
      # POST successfully made for {post}
  else:
      return f"Falha ao enviar POST. Código de status: {response.status_code}"
      # Failed to send POST. Status code: {response.status_code}

  return lux, hum, temp, data_post

while True:
    """ 
    Sequência das features para realização de testes:
    Sequence of features for testing:
    lux | humidity | temperature | lighting_switch | climate_switch | door_actuator | lux_status | 
    humidity_status | temperature_status | environment_temperature | environment_lux
    """
    # coletando os dados dos sensores
    # collecting data from sensors
    features, name, id = getData(GET)
    # realizando previsoes
    # making predictions
    prediction = predictions(GET)
    # tomada de decisão da IA
    # AI decision making
    decisionAI(prediction, name, id)
    # delay de 5s
    # 5s delay
    time.sleep(5)
