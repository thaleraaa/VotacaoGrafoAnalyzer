import requests
import json
from tqdm import tqdm

class Grafo:
    def __init__(self):
        self.lista = {}
        self.caminhos = 0
        self.nos = 0

    def criarno(self,no):
        if no not in self.lista:
            self.lista[no] = {}
            self.nos += 1
    
    def criarcaminho(self,no1,no2,peso):
        if no1 not in self.lista:
            self.criarno(no1)
        if no2 not in self.lista:
            self.criarno(no2)

        self.lista[no1][no2] = peso
        self.caminhos += 1

    def criarnos(self,nos):
        for no in nos:
            self.criarno(no)

    def criar2caminhos(self,no1,no2,peso):
        self.criarcaminho(no1,no2,peso)
        self.criarcaminho(no2,no1,peso)

    def removerno(self,no1):
        if no1 in self.lista:
            self.lista.pop(no1)
            self.nos -= 1
        else:
            print("no nao existe")
            return
        for no in self.lista:
            if no1 in self.lista[no]:
                del self.lista[no][no1]
                self.caminhos -= 1
        
    def removercaminho(self,no1,no2):
        if no2 in self.lista[no1]:
            del self.lista[no1][no2]

    def grausaida(self,no):
        return len(self.lista[no])
    
    def graudeentrada(self,no):
        somador = 0
        for node in self.lista:
            if no in self.lista[node]:
                somador += 1
        return somador
    
    def __str__(self) -> str:
        output = "Nós: " + str(self.nos) + "\n" 
        output += "Caminhos: " + str(self.caminhos) + "\n" 
        output += str(self.lista)
        return output
    
    def verificar_apontado_por(self, no):
        for node in self.lista:
            if no in self.lista[node]:
                return True
        return False


    def ler_arquivo(self,nome_arquivo):
        cont = 0
        contador = 0
        conte = 0
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')  
        arquivo1 = open(nome_arquivo, 'r', encoding='utf-8')  
        
        for line in tqdm(arquivo):
            if conte != 0:
                conteudo1 = line.strip().split(";")
                idVotacao1 = conteudo1[0]
                voto1 = conteudo1[3]
                deputado_nome1 = conteudo1[6]
                for linha1 in arquivo1:
                    if cont >= contador:
                        conteudo2 = linha1.strip().split(";")
                        idVotacao2 = conteudo2[0]
                        voto2 = conteudo2[3]
                        deputado_nome2 = conteudo2[6]
                        if deputado_nome1 != deputado_nome2:
                            if idVotacao1 == idVotacao2:
                                if voto2 == voto1:
                                    if deputado_nome1 not in self.lista or deputado_nome2 not in self.lista:
                                        self.criarno(deputado_nome1)
                                        self.criarno(deputado_nome2)
                                    if deputado_nome2 not in self.lista[deputado_nome1]:
                                        self.criar2caminhos(deputado_nome2,deputado_nome1,1)
                                    else:
                                        self.lista[deputado_nome2][deputado_nome1] += 1
                                        self.lista[deputado_nome1][deputado_nome2] += 1
                    else:
                        cont += 1
            conte += 1
            contador += 1
            cont = 0
            arquivo1 = open(nome_arquivo, 'r', encoding='utf-8') 
        arquivo.close()
        arquivo1.close()

    def escrever_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(f"{self.nos} {int(self.caminhos/2)}\n")
            visited_edges = set()  
            for no1 in self.lista:
                for no2, peso in self.lista[no1].items():
                    edge = tuple(sorted([no1, no2]))  
                    if edge not in visited_edges:
                        arquivo.write(f"{no1} {no2} {peso}\n")
                        visited_edges.add(edge)
            
    def pesosaida(self,nome_arquivo,nomesaida):
        with open(nomesaida, 'w', encoding='utf-8') as arquivo:
            a = 0
            conte = 0
            for no in self.lista:
                arquivo1 = open(nome_arquivo, 'r', encoding='utf-8') 
                for line in arquivo1:
                    if conte != 0:
                        conteudo1 = line.strip().split(";")
                        deputado_nome1 = conteudo1[6]
                        if deputado_nome1 == no:
                            a += 1
                    else:
                        conte += 1
                arquivo.write(f"{no} {a}\n")
                a = 0
        arquivo1.close()
            
    def api(self):
        cont = 0
        contador = 0
        response = requests.get("https://dadosabertos.camara.leg.br/api/v2/votacoes")
        data = json.loads(response.text)
        for votacoes in tqdm(data['dados']):
            id = votacoes["id"]
            resp = requests.get(("https://dadosabertos.camara.leg.br/api/v2/votacoes/"+id+"/votos"))
            dat = json.loads(resp.text)
            if not dat['dados']:
                continue
            for idvotacao in dat['dados']:
                len(dat)
                tipvot = idvotacao["tipoVoto"]
                deputado_nome1 = idvotacao["deputado_"]["nome"]
                self.criarno(deputado_nome1)
                for idvotacao2 in dat['dados']:
                    if cont >= contador:
                        tipvot2 = idvotacao2["tipoVoto"]
                        deputado_nome2 = idvotacao2["deputado_"]["nome"]
                        if tipvot2 == tipvot:
                            if deputado_nome1 != deputado_nome2:
                                if deputado_nome2 in self.lista[deputado_nome1]:
                                    self.lista[deputado_nome2][deputado_nome1] += 1
                                    self.lista[deputado_nome1][deputado_nome2] += 1
                                else:
                                    self.criar2caminhos(deputado_nome1,deputado_nome2,1)
                    else:
                        cont += 1
                contador += 1
                cont = 0
            contador = 0





                

