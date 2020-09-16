import datetime
import json
import time
import win32gui
import win32process
import psutil
import pydirectinput
from threading import Thread, Event, main_thread
from queue import Queue
from pynput.keyboard import Key, Listener

class Feitico(Thread):
  def __init__(self, objeto):
    Thread.__init__(self)
    self.obj = objeto

  def run(self):
    with Listener(on_press=self.on_press) as listener:
      listener.join()

  def on_press(self,key):
    if str(key).strip("'").lower() == 'f':
      if self.obj.telaLol():
        if(self.obj.cdOpen('F')):
          self.obj.setCd('F')
    if str(key).strip("'").lower() == 'd':
      if self.obj.telaLol():
        if(self.obj.cdOpen('D')):
          self.obj.setCd('D')

class FeiticoVivo(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.listaF = []
    self.listaD = []
    configs = open('config.json', 'r')
    self.configs_json = json.load(configs)
    configs.close()
    tempo = datetime.datetime.now() - datetime.timedelta(seconds = 9000)
    self.cd = {'F': tempo, 'D': tempo}

  def run(self):
    while True:
      time.sleep(1)
      if len(self.listaF) > 0:
        if self.cdOpen('F'):
          if self.telaLol():
            pydirectinput.press(self.listaF[0])
            del(self.listaF[0])
      if len(self.listaD) > 0:
        if self.cdOpen('D'):
          if self.telaLol():
            pydirectinput.press(self.listaD[0])
            del(self.listaD[0])

  def setFeiticosF(self,spell):
    self.listaF.append(spell)
  
  def setFeiticosD(self,spell):
    self.listaD.append(spell)

  def setCd(self,tecla):
    self.cd[tecla] = datetime.datetime.now()

  def cdOpen(self,tecla):
    cdPrevisto = self.cd[tecla] + datetime.timedelta(seconds = int(self.configs_json[tecla]["cd"]))
    if datetime.datetime.now() >= cdPrevisto:
      return True
    else:
      return False

  def telaLol(self):
    w = win32gui
    w.GetWindowText (w.GetForegroundWindow())
    pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
    nome = ""
    try:
      nome = psutil.Process(pid[-1]).as_dict(attrs=['name'])
    except:
      print("não achei o nome")
    print(nome['name'])
    if nome['name'].lower() == "league of legends.exe":
      return True
    else:
      return False