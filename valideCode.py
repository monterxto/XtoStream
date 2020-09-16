import os
import requests
dir_path = os.environ['APPDATA'] + '\Xto Stream'
txt_path = os.environ['APPDATA'] + '\Xto Stream\important'

def verificar(code):
  url = "https://streamlabs.com/api/v1.0/token"
  querystring = {
    "grant_type": "authorization_code",
    "client_id": "uldnv67vZD925bTfm6QyQFD93x3KR4nRgPwu2Mm2",
    "client_secret": "sDSN7brB8pCWIsxJudp2KUCLiu80L6JKCxbLKiG6",
    "redirect_uri": "http://localhost:3000/",
    "code": code,
  }
  response = requests.request("POST", url, data=querystring)
  return response

def gravarToken(token):
  if not os.path.exists(dir_path):
      os.makedirs(dir_path)
  arq = open(txt_path, 'wb')
  arq.write(token.encode(encoding='UTF-8'))
  arq.close()

def validarAuto():
  if os.path.exists(txt_path):
    ler = open(txt_path, "rb")
    url = "https://streamlabs.com/api/v1.0/donations"
    token = ler.read().decode('utf8')
    response = requests.request("GET", url, params={"access_token":token})
    ler.close()
    if response.status_code == 200:
      return [response.status_code,token]
    else:
      return [400]
  else:
    return [400]