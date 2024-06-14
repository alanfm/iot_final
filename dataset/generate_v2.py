import random

# Variáveis de controle lidas dos sensores
luxVal = 0 # Valor de luminosidade (float)
tempVal = 0 # Valor de temperatura (float)
humVal = 0 # Valor de umidade (float)   

# Status dos atuadores
lightingSwitch = 0 # 0 = desligado, 1 = ligado
climateSwitch = 0 # 0 = desligado, 1 = ligado
doorActuator = 0 # 0 = fechada, 1 = aberta

# Flag de status dos sensores
luxStatus = 0 # 0 = desligado, 1 = ligado
tempStatus = 0 # 0 = desligado, 1 = ligado
humStatus = 0 # 0 = desligado, 1 = ligado

# Rótulo de saída
label = 0 # 0 = normal, 1 = notificar ar condicionado, 2 = notificar iluminação, 3 = Iluminação e ar condicionado

""" 
    Seleciona um valor de iluminância aleatóriamente
"""
def getEnvironmentLux():
    # Lista de valores de média de ambientes
    environmentLuxAverageList = [200, 250, 300, 350, 400, 450, 500]
    # Seleção aleatória do valor da luminosidade média do ambiente
    return environmentLuxAverageList[random.randint(0, len(environmentLuxAverageList)-1)]

""" 
    Seleciona um valor de temperatura aleatóriamente
"""
def getEnvironmentTemperature():
    # Lista de valores de média de ambientes
    environmentTemperatureAverageList = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    # Seleção aleatória do valor da luminosidade média do ambiente
    return environmentTemperatureAverageList[random.randint(0, len(environmentTemperatureAverageList)-1)]

""" 
    Gera o valor de umidade aleatoriamente entre 0 e 100
"""
def getHumiditySensor():
    return random.uniform(0,100)

""" 
    Gera as flags de status aleatoriamente
"""
def getStatsFlags():
    return random.randint(0,1)

""" 
    Gera o valor de lux aleatoriamente <= ao valor setado
"""
def getLuxSensor(setLux):
    return random.uniform(0,setLux)

""" 
    Gera o valor de temperatura aleatoriamente >= ao valor setado
"""
def getTempSensor(setTemp):
    return random.uniform(setTemp,100)


""" 
    Gera os dados artificiais
"""
def generateData(percentLux=0.1, percentTemp=0.2):    
    lux = getEnvironmentLux()
    temp = getEnvironmentTemperature()
    humidity = getHumiditySensor()
    tempSensor = getTempSensor(temp)
    luxSensor = getLuxSensor(lux)
    luxStatus = getStatsFlags()
    humStatus = getStatsFlags()
    tempStatus = getStatsFlags()
    lightingSwitch = getStatsFlags()
    climateSwitch = getStatsFlags()
    doorActuator = getStatsFlags()
    
    # Checa se ou o status do luxímetro ou o status do interruptor estiverem zerados atribui zero para luxSensor
    if luxStatus == 0 or lightingSwitch == 0:
        luxSensor = 0
    
    # Atribui o valor zero quando o status do sensor de temperatura estiver desligado 0
    if tempStatus == 0:
        tempSensor = 0
    
    # Critérios para rotular as falhas e operação normal
    if (luxSensor <= (lux * (1 - percentLux)))  and luxStatus == 1 and lightingSwitch == 1 and tempSensor >= (temp * (1 + percentTemp)) and climateSwitch == 1 and tempStatus == 1 and humidity >= 50:
        label = 3 # falha na iluminação e ar condicionado
    elif (luxSensor <= (lux * (1 - percentLux)))  and luxStatus == 1 and lightingSwitch == 1:
        label = 2 # falha na iluminação
    elif tempSensor >= (temp * (1 + percentTemp)) and climateSwitch == 1 and tempStatus == 1 and humidity >= 50:
        label = 1 # falha no ar condicionado
    else:
        label = 0 # operação normal
    return (luxSensor, humidity, tempSensor, luxStatus, humStatus, tempStatus, lightingSwitch, climateSwitch, doorActuator, temp, lux, label)

""" 
    Gerando o número de amostras desejado
"""
def generateDataset(num_samples): 
    data = []
    for _ in range(num_samples):
        data.append(generateData())
    return data

def saveDataset(data):
    with open('sensor_data.csv', 'w') as file:
        file.write('lux,humidity,temperature,lighting_switch,climate_switch,door_actuator,lux_status,humidity_status,temperature_status,environment_temperature,environment_lux,label\n')
        for d in data:
            file.write(f'{d[0]},{d[1]},{d[2]},{d[3]},{d[4]},{d[5]},{d[6]},{d[7]},{d[8]},{d[9]},{d[10]},{d[11]}\n')

    print("Arquivo CSV gerado com sucesso.")

data = generateDataset(2000000)
saveDataset(data)
print("Algoritmo de geração de dados finalizado.")
