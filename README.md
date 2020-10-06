# XtoStream
### O que é o aplicativo?
Um Aplicativo que detecta doações da Twitch.tv e de acordo com a doação utilizar um feitico no League of Legends.
Ele detecta doações da StreamLabs.

### Qual o objetivo?
Vontade de criar um aplicativo assim que ainda não existe, e para melhorar meu portfólio

## Iniciar o aplicativo
## Consumo de API
Como dito anteriormente, ele detecta doações da StreamLabs, é necessarioo consumir a API fornecida por eles, então precisa seguir as instruções da streamlabs para conseguir utilizar sua API.
https://dev.streamlabs.com/docs/getting-started

### Dependencias
```
Kivy (não utiliza o gstreamer)
psutil
PyDirectInput
requests
```

## Configurar
No arquivo `valideCode` alterar essas informações com as informações do seu app, como está especifícado.
```
querystring = {
    "grant_type": "authorization_code",
    "client_id": "client_id do seu App",
    "client_secret": "client_secret do seu App",
    "redirect_uri": "http://localhost:3000/",
    "code": code,
  }
```

## Como utilzar o aplicativo?
Após abrir o aplicativo ele pedirá um código, esse é o código que vem como parâmetro após o usuario aprovar seu aplicativo na conta da streamlabs dele, então no link em que o usuário é redirecionado você precisa que ele copie o código e cole no aplicativo XtoStream.
Após validar o código ele irá para a tela de configuração, ele pode colocar o valor da doação que ira detectar, e o tempo de resfriamento da habilidade, e também poderá ativar ou desativar a detecção para aquela habilidade.
