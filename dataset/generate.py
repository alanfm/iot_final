import random

luxVal = 0 # Valor de luminosidade
tempVal = 0 # Valor de temperatura
humVal = 0 # Valor de umidade
environmentLuxAverage = 200 # Média de luminosidade
environmentTempAverage = 24  # Média de temperatura
lightingSwitch = 0 # 0 = desligado, 1 = ligado
climateSwitch = 0 # 0 = desligado, 1 = ligado
doorActuator = 0 # 0 = fechada, 1 = aberta
luxStatus = 0 # 0 = desligado, 1 = ligado
tempStatus = 0 # 0 = desligado, 1 = ligado
humStatus = 0 # 0 = desligado, 1 = ligado
label = 0 # 0 = normal, 1 = notificar iluminação, 2 = notificar ar condicionado

# Criar uma função que gera dados aleatórios para os sensores
# e determina o rótulo baseado nas condições dos sensores
# Para valores com rotulo normal, os dados dos sensores devem está dentro dos seguintes intervalos:
# lux_values de 200 a 1000
# humidity_values de 30 a 70
# temperature_values de 15 a 30
# Para valores com rótulo notificar iluminação:
# lux_values menor que 200
# Para valores com rótulo notificar ar condicionado:
# temperature_values maior que 30

def generateLabel():
    return random.randint(0, 2)

def generateLux(label):
    variation = environmentLuxAverage * 0.1
    luxStatus = 1 if label == 1 else 0

    if label != 1:
        return random.uniform(environmentLuxAverage - variation, environmentLuxAverage + variation), luxStatus
    
    return random.uniform(0, environmentLuxAverage - variation - 1), luxStatus

def generateHum(label):
    humStatus = 1 if label == 2 else 0
    if label != 2:
        return random.uniform(30, 49), humStatus
    
    return random.uniform(50, 80), humStatus

def generateTemp(label):
    variation = environmentTempAverage * 0.25
    tempStatus = 1 if label == 2 else 0

    if label != 2:
        return random.uniform(environmentTempAverage - variation, environmentTempAverage + variation), tempStatus
    
    return random.uniform(environmentTempAverage + variation + 1, 40), tempStatus

def generateData():
    label = generateLabel()
    luxVal, luxStatus = generateLux(label)
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

data = generateDataset(1000000)
saveDataset(data)
print("Algoritmo de geração de dados finalizado.")