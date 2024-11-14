# raspberryPi

Untuk merangkai dan menggunakan sensor jarak (seperti sensor ultrasonik HC-SR04) di Raspberry Pi, kamu bisa mengikuti langkah-langkah berikut:

### Alat yang Diperlukan
1. Sensor ultrasonik HC-SR04.
2. Kabel jumper.
3. Resistor (330 ohm dan 470 ohm) untuk menurunkan tegangan dari 5V ke 3.3V pada pin Echo.
4. Raspberry Pi dengan microSD yang sudah terpasang OS.

### Rangkaian Hardware
1. **Koneksi Sensor HC-SR04 ke Raspberry Pi:**
   - **VCC** dari sensor ke pin 5V Raspberry Pi.
   - **GND** dari sensor ke pin GND Raspberry Pi.
   - **Trig** dari sensor ke pin GPIO 23 (kamu bisa pilih pin GPIO lain jika perlu).
   - **Echo** dari sensor ke pin GPIO 24 (perlu dibuat voltage divider):
     - Pasang resistor 330 ohm di antara Echo dan GPIO 24.
     - Pasang resistor 470 ohm dari GPIO 24 ke GND untuk membentuk voltage divider, sehingga tegangan Echo turun dari 5V menjadi sekitar 3.3V, yang aman untuk GPIO Raspberry Pi.

### Koding Python untuk Menggunakan Sensor Jarak
Setelah merangkai sensor, buat script Python untuk mengukur jarak. Simpan file ini dengan nama `distance_sensor.py`.

```python
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
```

### Menjalankan Program
Jalankan program ini dengan perintah:

```bash
python3 distance_sensor.py
```

### Penjelasan Cara Kerja
1. Program mengirimkan sinyal trigger pada pin TRIG selama 10 mikrodetik.
2. Sensor HC-SR04 kemudian memancarkan gelombang ultrasonik, dan ketika gelombang memantul kembali, sensor mengirimkan sinyal ke pin ECHO.
3. Program mengukur waktu antara pengiriman dan penerimaan sinyal, lalu menghitung jarak berdasarkan waktu tersebut.

Dengan kode ini, Raspberry Pi akan mencetak jarak yang terukur dalam cm setiap detik.
