
##script

import RPi.GPIO as GPIO # type: ignore
import time

# Configuração do GPIO
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Função para ligar/desligar LEDs em horários específicos
def control_led(state):
    GPIO.output(LED_PIN, state)

# Lógica para controle baseado em horário
while True:
    current_hour = time.localtime().tm_hour
    if current_hour == 18:  # Exemplo: Liga às 18h
        control_led(True)
    elif current_hour == 23:  # Exemplo: Desliga às 23h
        control_led(False)
    time.sleep(3600)  # Espera uma hora antes de verificar novamente