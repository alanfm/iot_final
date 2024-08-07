# Carrega as bibliotecas
# Load libraries
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import serial
import requests
import pickle

# Define o tipo de sensor
# Define the sensor type
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BOARD)
# Define a GPIO conectada ao pino de dados do sensor
# Define the GPIO connected to the sensor data pin
pino_sensor = 25

# Url do ngrok com ip público
# ngrok URL with public IP
URL = "https://e067-200-129-37-2.ngrok-free.app/"
post = URL+'sensor/all'
get = URL+"env/all"

# Configuração da porta serial
# Serial port configuration
ser = serial.Serial(
    port='/dev/serial0',  # Porta serial 
    # Serial port
    baudrate=115200,      
    timeout=1            
)

def getData(get, lux, hum, temp):
  # realizando requisição GET
  # making GET request
    r = requests.get(get) 	# executa o get para coleta de dados
    				# executes the GET to collect data
    print(r)
        
    time.sleep(1)
    # verifica conexão e salva em variáveis os dados coletados via API
    # checks connection and saves collected data via API in variables
    if r.status_code == 200:
        # Analisar a resposta JSON
        # Analyzing the JSON response
        data = r.json()
        env_lux = data['env_lux']
        env_temp = data['env_temp']
        stat_lux = data['lux']['status']
        stat_hum = data['hum']['status']
        stat_temp = data['temp']['status']
        door = data['door']['status']
        light = data['light']['status']
        air = data['air']['status']
        lux_s = lux
        hum_s = hum
        temp_s = temp
        name = data.get('name')
        idd = data.get('id')
        
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
        print("getData: "+str(features))
        return features, name, idd

def postData(post, data):
  print("JSON post: "+str(data))
  try:
      # Enviar POST request
      # Send POST request
      response = requests.post(post, json=data)

      # Verificar a resposta
      # Check the response
      if response.status_code == 201:
          print(f"POST realizado com sucesso para {post}")
          # POST successfully made for {post}
      else:
          print(f"Falha ao enviar POST. Código de status: {response.status_code}")
          # Failed to send POST. Status code: {response.status_code}
  except requests.exceptions.RequestException as e:
      print(f"Erro durante o POST request: {e}")
      # Error during POST request: {e}

# função para realizar as previsoes
# function to make predictions
# def predictions(get,lux,hum,temp):
#   # Carregando o modelo 
#   # Loading the model
#   modelo = joblib.load('/home/mosquitto/mlp_smart_enviroument.joblib')
#   # Fazendo a previsão
#   # Making the prediction
#   features, name, idd = getData(get, lux, hum, temp)
#   features_array = np.array([features]) # transforma a lista em um array
#   					  # transforms the list into an array
#   prediction = modelo.predict(features_array)
  
#   # Mostrando o resultado
#   # Showing the result
#   print("\nFeatures via http e medições: "+str(features))
#   print("\nPredição: "+str(prediction))
#   return prediction

while(1):

  #  # Efetua a leitura do sensor
  #  # Reads the sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
   # Caso leitura esteja ok, mostra os valores na tela
   # If reading is ok, display the values on the screen
   if umid is not None and temp is not None:
     lux_s = 0
     if ser.in_waiting > 0:
        # Lê a linha da serial
        # Reads the serial line
        lux_s = ser.readline().decode('utf-8').rstrip() # faz a leitura do luximetro pela serial
        						# reads the luxmeter via serial
        print(f"\nIluminância: {lux_s}"+" lux")
     print ("\nTemperatura: "+str(temp))
     print ("\nUmidade: "+str(umid))
     features, name, idd = getData(get, lux_s, umid, temp)
     if features[3] == False:
       lux_s = 0
     if features[7] == False:
       lux_s = 0
     if features[4] == False:
       umid = 0
     if features[5] == False:
       temp = 0
       
     data_post = {
          'lux_value': lux_s,
          'hum_value': umid,
          'temp_value': temp
          }
     time.sleep(1)
   else:
     # Mensagem de erro de comunicacao com o sensor
     # Error message for sensor communication failure
     print("Falha ao ler dados do DHT11 !!!") #Failed to read data from DHT11 !!!
    
   time.sleep(3)
   print("Data post: "+str(data_post))
   postData(post, data_post)
