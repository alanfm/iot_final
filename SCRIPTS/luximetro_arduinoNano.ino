
const int analogInPin = A0;  
const int analogOutPin = 9;  
/*
  Para realizar a calibração do luxímetro, realizamos a medida com um luxímetro calibrado ou alternativamente com 
  algum aplicativo de celular, usando o luxímetro do celular como base. Após isso, encontramos o valor de calibração
  através da divisão entre o valor medido no celular/luxímetro e o valor apresentado na serial/medido pelo sensor LDR.
  Após isso inserimos essa constante na variável calibration, conforme script.

  Importante ressaltar que o arduino nano tem uma resolução de 10bits no canal analógico. Contudo, caso utilizem a proposta
  em outro microcontrolador com resolução maior ou inferior deve-se ajustar o valor da resolução do mesmo para que realize
  as medidas de forma correta.
  
  To calibrate the luxmeter, we measure with a calibrated luxmeter or alternatively with 
  some cell phone application, using the cell phone luxmeter as a base. After that, we find the calibration value
  by dividing the value measured on the cell phone/luxmeter by the value presented on the serial/measured by the LDR sensor.
  After that, we insert this constant into the calibration variable, as per the script.
    
  It is important to note that the Arduino Nano has a 10-bit resolution on the analog channel. However, if you use this approach
  on another microcontroller with higher or lower resolution, you should adjust the resolution value so that the measurements are correct.
*/

// variável para calibrar o luxímetro
// variable to calibrate the luxmeter
const float calibration = 0.46875;

int sensorValue = 0;  // value read from the pot
int outputValue = 0;  // value output to the PWM (analog out)
float tensao = 0, res = 0, lum = 0;
void setup() {
  // initialize serial communications at 115200 bps:
  Serial.begin(115200);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  // Corrigido para evitar divisão inteira
  // Corrected to avoid integer division
  tensao = ((float)sensorValue / 1023.0) * 5.0; 
  res = (tensao * 10000) / (5.0 - tensao);
  lum = (pow(10, 6.5 - 1.25 * log10(res))) / calibration;
  
  // map it to the range of the analog out:
  // mapeia para o intervalo da saída analógica:
  outputValue = map(lum, 0, 1023, 0, 255);
  
  // change the analog out value:
  // altera o valor de saída analógica:
  analogWrite(analogOutPin, outputValue);

  // Imprime o valor de lux na serial
  // Prints the lux value on the serial
  Serial.println(lum);
  delay(2000);
}
