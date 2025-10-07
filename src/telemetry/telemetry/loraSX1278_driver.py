import json
import os
import sys
from time import sleep
import telemetry.loralib as loralib




class loraSX1278_driver:
    def __init__(self, logger=None):
        self.logger = logger
        try:
            loralib.init(0, 434000000, 7)
        except Exception as e:
                self.logger.error(f"LoRa init failed: {e}")

    def send_data_example(self,message):
        print(f"Sending example telemetry data: {message}", flush=True)

    def send_data(self,message):
        try:
            loralib.send(message.encode())
            self.logger.info(f"\n\nWysylam dane: {message}\n\n")
            # loralib.send("Hello\n".encode())  # Send an acknowledgment
        except Exception as e:
            raise RuntimeError(f"Failed to send data via LoRa: {e}")

if __name__ == "__main__":
    driver = loraSX1278_driver()
    while True:
        try:
            driver.send_data("Hello World")
            print("Data sent successfully.")
            sleep(2)  # Sleep for 2 seconds to avoid flooding the channel
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            break