import webbrowser
import requests
import time
import json
import os
import sys
from gerenciar import Gerenciar
from valideCode import verificar, gravarToken, validarAuto
from threading import Thread, Event
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.resources import resource_add_path

if getattr(sys, 'frozen', False):
  resource_add_path(sys._MEIPASS)
  resource_add_path(os.path.join(sys._MEIPASS, 'resources'))

Window.clearcolor = get_color_from_hex("#151719")
content = Label(text='Salvou com Sucesso!')
popup = Popup(content=content,size_hint=(None,None),title="Aviso",size=(200,200))
popupSalvarErro = Popup(content=Label(text='Digite apenas números.'),size_hint=(None,None),title="Aviso",size=(200,200))
popupToken = Popup(content=Label(text='Código está errado\nSe persistir o erro\nTente gerar outro Codigo'),size_hint=(None,None),title="Aviso",size=(200,200))


if not os.path.exists('config.json'):
  criar_json = {"F": {"valorDonate": 50, "cd": 300}, "D": {"valorDonate": 30, "cd": 120}}
  criar = open('config.json', 'w')
  json.dump(criar_json, criar)
  criar.close()

class Gerenciador(ScreenManager):
  def primeira(self):
    pass

class ImageButton(ButtonBehavior, Image):  
    pass

class GridButton(ButtonBehavior, FloatLayout):
  pass

class TeclaF(Screen):
  def on_checkbox_active(self,value):
    gerenciadorStream.setCheckboxF(value)

  def Salvar(self):
    try:
      configs = open('config.json', 'r')
      configs_json = json.load(configs)
      configs.close()
      configs_json["F"]["cd"] = float(self.ids.cdF.text)
      configs_json["F"]["valorDonate"] = float(self.ids.doacaoF.text)
      configs = open('config.json', 'w')
      json.dump(configs_json, configs)
      popup.open()
      self.ids.doacaoF.text = ""
      self.ids.cdF.text = ""
    except:
      popupSalvarErro.open()

class TeclaD(Screen):
  def on_checkbox_active(self,value):
    gerenciadorStream.setCheckboxD(value)
  def Salvar(self):
    try:
      configs = open('config.json', 'r')
      configs_json = json.load(configs)
      configs.close()
      configs_json["D"]["cd"] = float(self.ids.cdF.text)
      configs_json["D"]["valorDonate"] = float(self.ids.doacaoF.text)
      configs = open('config.json', 'w')
      json.dump(configs_json, configs)
      popup.open()
      self.ids.doacaoF.text = ""
      self.ids.cdF.text = ""
    except:
      popupSalvarErro.open()

class MinhaTela(GridLayout):
  def canalYt(self):
    webbrowser.open('https://youtu.be/7SnefYn219s')
  
  def insta(self):
    webbrowser.open('https://www.instagram.com/antonioh__/?hl=pt-br')
    
  def aoClickF(self):
    App.get_running_app().root.current = 'teclaD' 
  
  def aoClickD(self):
    App.get_running_app().root.current = 'teclaF'

class Telar(Screen):
  def on_enter(self):
    Clock.schedule_once(self.change_screen)

  def change_screen(self, dt):
    response = validarAuto()
    if response[0] == 200:
      gerenciadorStream.setToken(response[1])
      gerenciadorStream.start()
      self.manager.current = "teclaD"

  def aoClick(self):
    response = verificar(self.ids.codigo.text)
    if response.status_code == 200:
      gravarToken(response.json()['access_token'])
      gerenciadorStream.setToken(response.json()['access_token'])
      gerenciadorStream.start()
      self.manager.current = 'teclaD'
    else:
      popupToken.open()

  def canalYt(self):
    webbrowser.open('https://youtu.be/7SnefYn219s')

class TelaApp(App):
  title = 'Xto Stream'
  icon = './assets/xtoiconekv.png'
  def build(self):
    return Gerenciador(transition=NoTransition())

if __name__ == '__main__':
  gerenciadorStream = Gerenciar()
  gerenciadorStream.daemon = True
  TelaApp().run()
