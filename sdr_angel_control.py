import requests
import logging
import time

class SdrAngelControl:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.port = 8091
        logging.basicConfig(level=logging.DEBUG)

    def __post_request(self, url, params = {}, json = ""):
        HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        URL = f'http://{self.ip_address}:{self.port}{url}'
        return requests.post(URL, headers = HEADERS, params = params, json = json)
        
    def __put_request(self, url, params = {}, json = ""):
        HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        URL = f'http://{self.ip_address}:{self.port}{url}'
        return requests.put(URL, headers = HEADERS, params = params, json = json)
        
    def __log_call_results(self, response):
        if response.status_code < 300:
            print('ok')
        else:
            print(response.text)

    def add_sink_device(self):
        params = {'direction': '1'}
        url = '/sdrangel/deviceset'
        response = self.__post_request(url, params)
        self.__log_call_results(response)

    def set_output_device_to_lime(self):
        url = '/sdrangel/deviceset/1/device'
        data = {"direction": 1,
                "hwType": "LimeSDR"
            }
        response = self.__put_request(url, {}, data)
        self.__log_call_results(response)

    def set_lime_parameters(self):
        url = '/sdrangel/deviceset/1/device/settings'
        data = {"deviceHwType": "LimeSDR",
                "direction": 1,
                "limeSdrOutputSettings": {
                "antennaPath": 2,
                "centerFrequency": 435000000,
                "devSampleRate": 1000000,
                "extClock": 0,
                "extClockFreq": 10000000,
                "gain": 4,
                "gpioDir": 0,
                "gpioPins": 0,
                "log2HardInterp": 3,
                "log2SoftInterp": 0,
                "lpfBW": 5500000,
                "lpfFIRBW": 2500000,
                "lpfFIREnable": 0,
                "ncoEnable": 0,
                "ncoFrequency": 0,
                "reverseAPIAddress": "127.0.0.1",
                "reverseAPIDeviceIndex": 0,
                "reverseAPIPort": 8888,
                "transverterDeltaFrequency": 0,
                "transverterMode": 0,
                "useReverseAPI": 0
              }
        }
        response = self.__put_request(url, {}, data)
        self.__log_call_results(response)

    def init_sdr_angel(self):
        self.add_sink_device()
        self.set_output_device_to_lime()
        time.sleep(0.1)
        self.set_lime_parameters()

def main():
    ac = SdrAngelControl("192.168.86.28")
    ac.init_sdr_angel()

if __name__ == "__main__":
    main()