# Projeto Hotel - APS

Este projeto foi desenvolvido como parte do trabalho semestral do curso de Ciência da Computação da UNIP. O objetivo da aplicação é ajudar na gestão ambiental de um hotel, minimizando o desperdício de água e energia nos quartos por meio da integração de sensores de presença, termostatos, chuveiros inteligentes e tomadas programáveis.

## Funcionalidades

O projeto consiste em uma API com as seguintes rotas e funcionalidades:

- Monitoramento de presença (`GET /api/presenca`): Simula a detecção de presença no quarto do hotel (hóspede, funcionário, animal ou vazio).
- Controle de termostato (`POST /api/termostato`): Ajusta a temperatura do ar-condicionado ou aquecedor do quarto do hotel com base na presença detectada e nas preferências do hóspede.
- Controle de chuveiro inteligente (`POST /api/chuveiro`): Regula o fluxo e a temperatura da água do chuveiro do quarto do hotel com base na presença detectada e nas preferências do hóspede.
- Controle de tomadas programáveis (`POST /api/tomadas`): Liga ou desliga as tomadas elétricas do quarto do hotel com base na presença detectada e nas preferências do hóspede.
- Ajustar dispositivos (`POST /api/ajustar_dispositivos`): Integra a lógica de interação entre os serviços, ajustando os dispositivos com base na presença detectada no quarto do hotel.

## Requisitos

- Python 3.6 ou superior
- Flask
- Flask-RESTful

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Gustavo-Coutinho/projeto_hotel.git
cd projeto_hotel
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Para iniciar a aplicação, execute o seguinte comando:

```bash
python app.py
```

A aplicação estará disponível no endereço: `http://127.0.0.1:5000`.

## Testando a API

Você pode testar a API usando um cliente REST, como o [Postman](https://www.postman.com/downloads/) ou [Insomnia](https://insomnia.rest/download).

1. Monitoramento de presença: `GET /api/presenca`
   - Abra o Postman e crie uma nova requisição GET.
   - Digite a URL: `http://127.0.0.1:5000/api/presenca`
   - Clique em "Send" e verifique a resposta.

2. Controle de termostato: `POST /api/termostato`
   - Abra o Postman e crie uma nova requisição POST.
   - Digite a URL: `http://127.0.0.1:5000/api/termostato`
   - No corpo da requisição, selecione "raw" e "JSON" como tipo.
   - Insira o JSON: `{"temperatura_desejada": 22}`
   - Clique em "Send" e verifique a resposta.

3. Controle de chuveiro inteligente: `POST /api/chuveiro`
   - Abra o Postman e crie uma nova requisição POST.
   - Digite a URL: `http://127.0.0.1:5000/api/chuveiro`
   - No corpo da requisição, selecione "raw" e "JSON" como tipo.
   - Insira o JSON: `{"fluxo_desejado": 2, "temperatura_desejada": 35}`
   - Clique em "Send" e verifique a resposta.

4. Controle de tomadas programáveis: `POST /api/tomadas`
   - Abra o Postman e crie uma nova requisição POST.
   - Digite a URL: `http://127.0.0.1:5000/api/tomadas`
   - No corpo da requisição, selecione "raw" e "JSON" como tipo.
   - Insira o JSON: `{"programacao": "07:00-23:00"}`
   - Clique em "Send" e verifique a resposta.

5. Ajustar dispositivos: `POST /api/ajustar_dispositivos`
   - Abra o Postman e crie uma nova requisição POST.
   - Digite a URL: `http://127.0.0.1:5000/api/ajustar_dispositivos`
   - No corpo da requisição, selecione "raw" e "JSON" como tipo.
   - Insira o JSON: `{"presenca": "hospede", "temperatura_desejada": 22, "fluxo_desejado": 2, "temperatura_chuveiro_desejada": 35, "programacao_tomadas": "07:00-23:00"}`
   - Clique em "Send" e verifique a resposta.

Com estes passos, você pode testar todas as rotas criadas na APS usando o Postman.

