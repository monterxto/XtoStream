from threading import Thread, Event
import requests
import time
from queue import Queue
class LerDonations(Thread):
    def __init__(self,evento, infos, access_token, valores):
        Thread.__init__(self)
        self.evento = evento
        self.token = access_token
        self.infos = infos
        self.valor = valores
        self.amount = []

    def run(self):
      url = "https://streamlabs.com/api/v1.0/donations"
      first = 1
      while True:
        time.sleep(13)
        querystring = {
          "access_token":self.token,
          "limit": 10
        }
        response = requests.request("GET", url, params=querystring)
        doacao = response.json()['data']
        if first == 2:
          for i in range(len(doacao)):
            if not self.elementoJson(doacao_ref,doacao[i]['donation_id']):
              if float(doacao[i]['amount']) == self.valor["F"]["valorDonate"] or float(doacao[i]['amount']) == self.valor["D"]["valorDonate"]:
                self.amount.append(float(doacao[i]['amount']))
          if len(self.amount) > 0:
            self.infos.put(self.amount)
            self.amount = []
            self.evento.set()

        first = 2
        doacao_ref = response.json()['data']

    def elementoJson(self,jsonObj, valor):
      for dict in jsonObj:
        if dict['donation_id'] == valor:
          return True