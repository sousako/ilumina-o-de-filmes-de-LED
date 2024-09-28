
##script
import RPi.GPIO as GPIO
import time
import csv
from PIL import Image, ImageDraw

# Configuração do GPIO
LED_PIN = 18
SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Função para controlar a iluminação
def control_led(state):
    GPIO.output(LED_PIN, state)

# Função para ajustar brilho
def adjust_brightness():
    light_level = GPIO.input(SENSOR_PIN)
    if light_level < threshold:
        control_led(True)
    else:
        control_led(False)

# Função para gerar padrões
def create_pattern():
    img = Image.new('RGB', (100, 100), color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 80, 80], fill='blue')
    img.save('pattern.png')

# Função para registrar uso dos LEDs
def log_usage():
    with open('led_usage.csv', mode='a') as file:
        writer = csv.writer(file)
        state = 'ON' if GPIO.input(LED_PIN) else 'OFF'
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), state])

# Loop principal
try:
    while True:
        control_led(True)  # Exemplo: Liga os LEDs por padrão
        adjust_brightness()
        log_usage()
        time.sleep(60)  # Espera um minuto antes da próxima iteração

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
