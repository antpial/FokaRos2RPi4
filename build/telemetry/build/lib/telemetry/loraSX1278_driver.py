import json
import os
import sys
module_path = os.path.join(os.path.dirname(__file__), 'LoRa_RaspberryPi')
sys.path.append(module_path)

import loralib 


class loraSX1278_driver:
    def __init__(self):
        loralib.init(0, 434000000, 7)

    def send_data_example(self,message):
        print(f"Sending example telemetry data: {message}", flush=True)

    def send_data(self,message):
        try:
            loralib.send(message.encode())
        except Exception as e:
            raise RuntimeError(f"Failed to send data via LoRa: {e}")

