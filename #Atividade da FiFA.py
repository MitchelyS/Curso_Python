
from abc import abstractmethod # Importa a base abstrata e o decorator

#Classe mãe
class ClubeParticipante:
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.raking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(self):# aqui foi a junção usei f que soma string+variavel
        print(f"Clube:{self.nome}| Pais{self.pais}|Confederação{self.confederacao}"|f"ranking: {self.ranking_fifa}|Gols Marcados{self.gols_marcados}|Vitorias{self.vitorias}")


    @abstractmethod
    def calcular_desempenho(self):
        pass # Aqui a filha vai implementar a fórmula de desempenho
    
    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass # Aqui a filha vai gerar o relatório completo

#Subclasse Filha
    class ClubeMity(ClubeParticipante):
        def __int__(self, nome, pais, ranking_fifa, gols_marcados, vitorias):
            # aqui a gente chama o __init__ da classe mãe
            super().__init__(self, nome, pais, "Mity", ranking_fifa, gols_marcados, vitorias)
        
        def calcular_desempenho(self):
            return self.vitórias * 3 + self.gols_marcados * 0,5
        
        def gerar_relatorio_tecnico(self):
            self.exibir_dados()
            print("Desempenho:", self.calcular_desempenho())