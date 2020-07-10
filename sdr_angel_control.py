import requests
import logging
import time

REQUEST_TIMEOUT = 8
SDR_ANGEL_SETTLE_TIME = 0.4

class SdrAngelControl:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.port = 8091
        logging.basicConfig(level=logging.WARN)

    def __post_request(self, url, params = {}, json = "", timeout = REQUEST_TIMEOUT):
        time.sleep(SDR_ANGEL_SETTLE_TIME)
        HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        URL = f'http://{self.ip_address}:{self.port}{url}'
        return requests.post(URL, headers = HEADERS, params = params, json = json, timeout = timeout)
        
    def __put_request(self, url, params = {}, json = "", timeout = REQUEST_TIMEOUT):
        time.sleep(SDR_ANGEL_SETTLE_TIME)
        HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        URL = f'http://{self.ip_address}:{self.port}{url}'
        return requests.put(URL, headers = HEADERS, params = params, json = json, timeout = timeout)
        
    def __delete_request(self, url, params = {}, json = "", timeout = REQUEST_TIMEOUT):
        time.sleep(SDR_ANGEL_SETTLE_TIME)
        HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        URL = f'http://{self.ip_address}:{self.port}{url}'
        return requests.delete(URL, headers = HEADERS, params = params, json = json, timeout = timeout)
        
    def __log_call_results(self, response):
        if response.status_code < 300:
            print('ok')
        else:
            print(response.text)

    def delete_device_sets(self):
        while True:
            response = self.__delete_request('/sdrangel/deviceset')
            if response.status_code > 300:
                break

    def delete_input_channels(self):
        channel_index = 0
        while True:
            response = self.__delete_request(f'/sdrangel/deviceset/0/channel/{channel_index}')
            # channel_index += 1
            print(response.text)
            if response.status_code > 300:
                break

    def add_sink_device(self):
        params = {'direction': '1'}
        url = '/sdrangel/deviceset'
        response = self.__post_request(url=url, params=params)
        self.__log_call_results(response)

    def set_output_device_to_lime(self):
        url = '/sdrangel/deviceset/1/device'
        data = {"direction": 1,
                "hwType": "LimeSDR"
            }
        response = self.__put_request(url=url, json=data)
        self.__log_call_results(response)

    def set_input_device_to_lime(self):
        url = '/sdrangel/deviceset/0/device'
        data = {"direction": 0,
                "hwType": "LimeSDR"
            }
        response = self.__put_request(url=url, json=data)
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

    def add_nfm_tx_channel(self):
        data = {
                "NFMModSettings": {
                    "afBandwidth": 3000,
                    "audioDeviceName": "System default device",
                    "channelMute": 0,
                    "ctcssIndex": 0,
                    "ctcssOn": 1,
                    "cwKeyer": {
                    "dashKey": 45,
                    "dashKeyModifiers": 0,
                    "dotKey": 46,
                    "dotKeyModifiers": 0,
                    "keyboardIambic": 1,
                    "loop": 1,
                    "mode": 1,
                    "sampleRate": 11025,
                    "text": "w1ant test test test ",
                    "wpm": 11
                    },
                    "fmDeviation": 1000,
                    "inputFrequencyOffset": 0,
                    "modAFInput": 4,
                    "playLoop": 0,
                    "reverseAPIAddress": "127.0.0.1",
                    "reverseAPIChannelIndex": 0,
                    "reverseAPIDeviceIndex": 0,
                    "reverseAPIPort": 8888,
                    "rfBandwidth": 12500,
                    "rgbColor": -65536,
                    "title": "NFM Modulator",
                    "toneFrequency": 1060,
                    "useReverseAPI": 0,
                    "volumeFactor": 1
                },
                "channelType": "NFMMod",
                "direction": 1
            }
        # Creates the channel
        response = self.__post_request('/sdrangel/deviceset/1/channel', {}, data)
        self.__log_call_results(response)
        # Sets the channel properties
        response = self.__put_request('/sdrangel/deviceset/1/channel/0/settings', {}, data)
        self.__log_call_results(response)

    def add_nfm_rx_channel(self):
        data = {
                "NFMDemodSettings": {
                    "afBandwidth": 3000,
                    "audioDeviceName": "System default device",
                    "audioMute": 0,
                    "ctcssIndex": 1,
                    "ctcssOn": 1,
                    "deltaSquelch": 0,
                    "fmDeviation": 5000,
                    "highPass": 1,
                    "inputFrequencyOffset": 0,
                    "reverseAPIAddress": "127.0.0.1",
                    "reverseAPIChannelIndex": 0,
                    "reverseAPIDeviceIndex": 0,
                    "reverseAPIPort": 8888,
                    "rfBandwidth": 12500,
                    "rgbColor": -65536,
                    "squelch": -30,
                    "squelchGate": 5,
                    "streamIndex": 0,
                    "title": "NFM Demodulator",
                    "useReverseAPI": 0,
                    "volume": 1
                },
                "channelType": "NFMDemod",
                "direction": 0
        }
        # Creates the channel
        response = self.__post_request('/sdrangel/deviceset/0/channel', {}, data)
        self.__log_call_results(response)
        # Now I can truly delete the zero channel
        response = self.__delete_request(f'/sdrangel/deviceset/0/channel/0')
        # Sets the channel properties
        response = self.__put_request('/sdrangel/deviceset/0/channel/0/settings', {}, data)
        self.__log_call_results(response)

    def init_sdr_angel(self):
        self.delete_device_sets()
        self.set_input_device_to_lime()
        self.delete_input_channels()
        self.add_sink_device()
        self.set_output_device_to_lime()
        self.set_lime_parameters()
        self.add_nfm_tx_channel()
        self.add_nfm_rx_channel()

def main():
    ac = SdrAngelControl("192.168.86.28")
    ac.init_sdr_angel()

if __name__ == "__main__":
    main()