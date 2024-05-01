import machine
import random
import network
import time
import sys
import gc
import dht  # Import the DHT library if you're using a DHT sensor
try:
    import usocket as socket
except:
    import socket

# Create a DHT object for temperature and humidity sensor
dht_sensor = dht.DHT22(machine.Pin(4))  # Replace Pin(4) with the appropriate GPIO pin

gc.collect()

# Configure ESP32 in AP mode
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="HAri", password="Thankyoubhaii@1234")
print("Network Configure ",ap.ifconfig())
# Web page
def web_page(temp, humidity):
    
    temp = random.randint(10,401)
    humidity = random.randint(30,100)
    html_page = """
    <html>
    <head>
    <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
    </head>
    <body>
    <center><h2>ESP32 Temperature and Humidity Monitoring</h2></center>
    <center>
    <p>Temperature: <strong>{0} °C</strong></p>
    <p>Humidity: <strong>{1} %</strong></p>
    </center>
    </body>
    </html>""".format(temp, humidity)
    return html_page

# Create server socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print('Socket created')
except Exception as e:
    print('Error:', str(e))
    sys.exit()

while True:
    conn, addr = s.accept()
    print('Client connected from', addr)
    request = conn.recv(1024)
    request = str(request)
    print('Request content:', request)

    # Read temperature and humidity data from the sensor
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    response = web_page(temperature, humidity)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
