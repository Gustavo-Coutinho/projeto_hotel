class TomadasProgramaveis:
    def ajustar_programacao(self, programacao, presenca):
        if presenca == 'hospede':
            return 'Programação das tomadas ajustada para os valores desejados pelo hóspede'
        else:
            return 'Programação das tomadas ajustada para os valores padrão'
