import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Set Trigger ke HIGH selama 10µs
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Tunggu Echo berubah ke HIGH
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Tunggu Echo kembali ke LOW
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Hitung durasi gelombang suara
    duration = end_time - start_time

    # Hitung jarak (34300 cm/s adalah kecepatan suara)
    distance = (duration * 34300) / 2
    return distance

try:
    while True:
        dist = measure_distance()
        print("Jarak: {:.2f} cm".format(dist))
        time.sleep(1)
except KeyboardInterrupt:
    print("Pengukuran dihentikan")
finally:
    GPIO.cleanup()
