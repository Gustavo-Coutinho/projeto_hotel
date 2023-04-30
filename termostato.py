class Termostato:
    def ajustar_temperatura(self, temperatura_desejada, presenca):
        if presenca == 'hospede':
            return 'Temperatura ajustada para {}'.format(temperatura_desejada)
        else:
            return 'Temperatura ajustada para a temperatura padrão'
