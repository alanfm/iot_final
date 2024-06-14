import joblib
import pandas as pd
# import serial
import time
import numpy as np
import generate_dataset as gd

# Carregar o modelo
modelo = joblib.load('/home/geraldo/Documentos/python_projects/JUPYTER-NOOTEBOOK/IoT_final_project/mlp_smart_enviroument.joblib')

while True:
    
    """ 
    Sequência das features para realização de testes:
    
    lux | humidity | temperature | ligthing_switch | climate_switch | door_actuator | lux_status | 
    humidity_status | temperature_status | enviroument_temperature | enviroument_lux
    
    """
    features = gd.generateData()
    features = features[:11]
    print(features)
    # features = [286, 30, 30, 1, 1, 1, 1, 1, 1, 25, 300]

    # Convertendo para um array
    features_array = np.array([features])

    # Fazendo a previsão
    prediction = modelo.predict(features_array)

    # Mostrando o resultado
    print(prediction)
    
    # Tomada de decisões
    match prediction[0]:
        case 0:
            print("Operação Normal")
        case 1:
            print("Falha climatização.") # Enviar a tomada de decisões e o dataframe da falha para nuvem
        case 2:
            print("Falha na iluminação") # Enviar a tomada de decisões e o dataframe da falha para nuvem
        case 3:  
            print("Falha iluminação e ar condicionado.") # Enviar a tomada de decisões e o dataframe da falha para nuvem
    
    time.sleep(2)