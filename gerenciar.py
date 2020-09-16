import json
from threading import Thread, Event, main_thread
from LerDonate import LerDonations
from feiticoVivo import Feitico, FeiticoVivo
from queue import Queue

class Gerenciar(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.checkboxf = False
    self.checkboxd = False

  def run(self):
    #Ler configurações
    configs = open('config.json', 'r')
    configs_json = json.load(configs)
    configs.close()
    #Método para receber infos
    infos_uteis = Queue()
    #Eventos
    evento = Event()
    #Instanciar Objeto
    leitor = LerDonations(evento,infos_uteis,self.token,configs_json)
    usarSpeel = FeiticoVivo()
    verifySpeel = Feitico(usarSpeel)

    verifySpeel.daemon = True
    usarSpeel.daemon = True
    leitor.daemon = True
    verifySpeel.start()
    usarSpeel.start()
    leitor.start()
    while True:
      evento.wait()
      evento.clear()
      menu = infos_uteis.get()
      if configs_json["F"]["valorDonate"] in menu and self.checkboxf:
        for i in range(menu.count(configs_json["F"]["valorDonate"])):
          usarSpeel.setFeiticosF('f')

      if configs_json["D"]["valorDonate"] in menu and self.checkboxd:
        for i in range(menu.count(configs_json["D"]["valorDonate"])):
          usarSpeel.setFeiticosD('d')

  def setToken(self,token):
    self.token = token

  def setCheckboxF(self,value):
    self.checkboxf = value

  def setCheckboxD(self,value):
    self.checkboxd = value