
const int analogInPin = A0;  
const int analogOutPin = 9;  
/*
  Para realizar a calibração do luxímetro, realizamos a medida com um luxímetro calibrado ou alternativamente com 
  algum aplicativo de celular, usando o luxímetro d celular como base. Após isso, encontramos o valor de calibração
  através da divisão entre o valor medido no celular/luxímetro e o valor apresentado na serial/medido pelo sensor LDR.
  Após isso inserimos essa constante na variável calibration, conform script.

  Importante ressaltar que o arduino nano tem uma resolução de 10bits no canal analógico. Contudo, caso utilizem a proposta
  em outro microcontrolador com resolução maior ou inferior deve-se ajustar o valor da resolução do mesmo para que realize
  as medidas de forma correta.
*/
const float calibration = 0.46875; // variável para calibrar o luxímetro
int sensorValue = 0;  // value read from the pot
int outputValue = 0;  // value output to the PWM (analog out)
float tensao=0, res=0, lum=0;
void setup() {
  // initialize serial communications at 115200 bps:
  Serial.begin(115200);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  tensao = ((float)sensorValue / 1023.0) * 5.0;  // Corrigido para evitar divisão inteira
  res = (tensao * 10000) / (5.0 - tensao);
  lum = (pow(10, 6.5 - 1.25 * log10(res))) / calibration;
  // map it to the range of the analog out:
  outputValue = map(lum, 0, 1023, 0, 255);
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);

  // Imprime o valor de lux na serial
  Serial.println(lum);
  delay(2000);
}
