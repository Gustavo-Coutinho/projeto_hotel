from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

class MonitoramentoPresenca(Resource):
    def get(self):
        presenca = random.choice(['hospede', 'funcionario', 'animal', 'vazio'])
        return {'presenca': presenca}

class ControleTermostato(Resource):
    def post(self):
        temperatura_desejada = request.json['temperatura_desejada']
        return {'status': 'temperatura ajustada para {}'.format(temperatura_desejada)}

class ControleChuveiroInteligente(Resource):
    def post(self):
        fluxo_desejado = request.json['fluxo_desejado']
        temperatura_desejada = request.json['temperatura_desejada']
        return {'status': 'fluxo e temperatura ajustados'}

class ControleTomadasProgramaveis(Resource):
    def post(self):
        programacao = request.json['programacao']
        return {'status': 'programação das tomadas ajustada'}

class AjustarDispositivos(Resource):
    def post(self):
        monitoramento = MonitoramentoPresenca()
        presenca = monitoramento.get()['presenca']

        ajustes = {}
        
        if presenca == 'hospede':
            termostato = ControleTermostato()
            ajustes['termostato'] = termostato.post().get('status')

            chuveiro = ControleChuveiroInteligente()
            ajustes['chuveiro'] = chuveiro.post().get('status')

            tomadas = ControleTomadasProgramaveis()
            ajustes['tomadas'] = tomadas.post().get('status')

        elif presenca == 'funcionario' or presenca == 'animal':
            ajustes['status'] = "Nenhum ajuste realizado. A presença detectada é de um funcionário ou animal."

        else:
            ajustes['status'] = "Nenhum ajuste realizado. Não há presença detectada no quarto."

        return ajustes

api.add_resource(MonitoramentoPresenca, '/api/presenca')
api.add_resource(ControleTermostato, '/api/termostato')
api.add_resource(ControleChuveiroInteligente, '/api/chuveiro')
api.add_resource(ControleTomadasProgramaveis, '/api/tomadas')
api.add_resource(AjustarDispositivos, '/api/ajustar_dispositivos')

if __name__ == '__main__':
    app.run(debug=True)