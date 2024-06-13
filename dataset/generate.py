import random

# Variáveis de controle
luxVal = 0 # Valor de luminosidade (float)
tempVal = 0 # Valor de temperatura (float)
humVal = 0 # Valor de umidade (float)   
environmentTempAverage = 24  # Média de temperatura
lightingSwitch = 0 # 0 = desligado, 1 = ligado
climateSwitch = 0 # 0 = desligado, 1 = ligado
doorActuator = 0 # 0 = fechada, 1 = aberta
luxStatus = 0 # 0 = desligado, 1 = ligado
tempStatus = 0 # 0 = desligado, 1 = ligado
humStatus = 0 # 0 = desligado, 1 = ligado
label = 0 # 0 = normal, 1 = notificar iluminação, 2 = notificar ar condicionado



"""
    Gera um rótulo aleatório para os dados
"""
def generateLabel():
    return random.randint(0, 2)

def getEnvironmentLux():
    # Lista de valores de média de ambientes
    environmentLuxAverageList = [200, 250, 300, 350, 400, 450]
    # Seleção aleatória do valor da luminosidade média do ambiente
    return environmentLuxAverageList[random.randint(0, len(environmentLuxAverageList)-1)]

"""
    Gera um valor de luminosidade aleatório
"""
def generateLux(label):
    environmentLuxAverage = getEnvironmentLux()
    variation = environmentLuxAverage * 0.1
    luxStatus = 1 if label == 1 else 0

    if label != 1:
        return random.uniform(environmentLuxAverage - variation, environmentLuxAverage + variation), luxStatus, environmentLuxAverage
    
    return random.uniform(0, environmentLuxAverage - variation - 1), luxStatus, environmentLuxAverage

"""
    Gera um valor de umidade aleatório
"""
def generateHum(label):
    humStatus = 1 if label == 2 else 0
    if label != 2:
        return random.uniform(30, 49), humStatus
    
    return random.uniform(50, 80), humStatus

"""
    Gera um valor de temperatura aleatório
"""
def generateTemp(label):
    variation = environmentTempAverage * 0.25
    tempStatus = 1 if label == 2 else 0

    if label != 2:
        return random.uniform(environmentTempAverage - variation, environmentTempAverage + variation), tempStatus
    
    return random.uniform(environmentTempAverage + variation + 1, 40), tempStatus

"""
    Gera os dados para os sensores
"""
def generateData():
    label = generateLabel()
    luxVal, luxStatus, environmentLuxAverage  = generateLux(label)
    humVal, humStatus = generateHum(label)
    tempVal, tempStatus = generateTemp(label)

    if label == 1:
        lightingSwitch = 1
        climateSwitch = 1
    else:
        lightingSwitch = 0
        climateSwitch = 0

    doorActuator = random.randint(0, 1)

    return (luxVal, humVal, tempVal, lightingSwitch, climateSwitch, doorActuator, luxStatus, humStatus, tempStatus, environmentTempAverage, environmentLuxAverage, label)


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

data = generateDataset(10)
saveDataset(data)
print("Algoritmo de geração de dados finalizado.")