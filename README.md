# Projeto Final de IoT

Aplicação para o projeto final da disciplina de IoT.
Dentro da branch generate_v2 temos alguns scripts e arquivos como segue descrição abaixo:

- dataset_iot_pf.csv: arquivo com a base de dados geradas artificialmente para treinamento da IA;
- generate_dataset.py: Arquivo com script para gerar os dados artificialmente;
- luximetro_arduinoNamo.ino: Script no arduino nano para leitura do sensor LDR, conversão para lux e envio dos dados via serial;
- mlp_smart_environment.joblib: Arquivo gerado no colab por meio da biblioteca .joblib com IA treinada;
- projeto_final_iot_mlp.ipynb: Arquivo com script para treinamento da IA com colab usando MLP;
- script_ia_ok: Arquivo com script de tomada de decisões da IA;
- script_raspberry_sensores: Arquivo com script para leitura dos sensores e envio dos dados para banco de dados em nuvem.
