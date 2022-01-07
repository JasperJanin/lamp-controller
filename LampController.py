import requests
import color as c


class Lamp:

    def __init__(self, bridgeIP, bridgeToken, address="/lights/1/state"):
        self.bridgeURL = "http://" + bridgeIP + "/api"
        self.bridgeToken = bridgeToken
        self.userURL = self.bridgeURL + "/" + bridgeToken if bridgeToken else ""
        self.lampURL = self.userURL + address

    def setLight(self, color):
        body = color
        requests.put(self.lampURL, json={"effect": color["effect"]})
        requests.put(self.lampURL, json=body)

    def setMaxColor(self, hue):
        self.setLight(c.maxColor(hue))

    def colorloop(self):
        body = {"effect": "colorloop"}
        requests.put(self.lampURL, json=body)
