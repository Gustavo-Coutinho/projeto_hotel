class ChuveiroInteligente:
    def ajustar_fluxo_temperatura(self, fluxo_desejado, temperatura_desejada, presenca):
        if presenca == 'hospede':
            return 'Fluxo e temperatura ajustados para os valores desejados pelo hóspede'
        else:
            return 'Fluxo e temperatura ajustados para os valores padrão'
