import random

class SensorPresenca:
    def verificar_presenca(self):
        presenca = random.choice(['hospede', 'funcionario', 'animal', 'vazio'])
        return presenca
