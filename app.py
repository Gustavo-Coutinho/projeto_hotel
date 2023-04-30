from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sensor import SensorPresenca
from termostato import Termostato
from chuveiro import ChuveiroInteligente
from tomadas import TomadasProgramaveis

app = Flask(__name__)
api = Api(app)

sensor_presenca = SensorPresenca()
termostato = Termostato()
chuveiro_inteligente = ChuveiroInteligente()
tomadas_programaveis = TomadasProgramaveis()

class AjustarDispositivos(Resource):
    def post(self):
        temperatura_desejada = request.json['temperatura_desejada']
        fluxo_desejado = request.json['fluxo_desejado']
        temperatura_agua_desejada = request.json['temperatura_agua_desejada']
        programacao = request.json['programacao']

        presenca = sensor_presenca.verificar_presenca()

        ajuste_termostato = termostato.ajustar_temperatura(temperatura_desejada, presenca)
        ajuste_chuveiro = chuveiro_inteligente.ajustar_fluxo_temperatura(fluxo_desejado, temperatura_agua_desejada, presenca)
        ajuste_tomadas = tomadas_programaveis.ajustar_programacao(programacao, presenca)

        return {
            'ajuste_termostato': ajuste_termostato,
            'ajuste_chuveiro': ajuste_chuveiro,
            'ajuste_tomadas': ajuste_tomadas
        }

api.add_resource(AjustarDispositivos, '/api/ajustar_dispositivos')

if __name__ == '__main__':
    app.run(debug=True)