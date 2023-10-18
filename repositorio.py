personagens = {
    1: {
        "nome": "Naruto Uzumaki",
        "Cla": "Uzumaki",
        "Vila": "Oculta das Folhas",
        "Ocupacao": "Hokage",
        "Habilidades" : "Kekkei Genkai",
        "imagem" : "https://static.printler.com/cache/1/d/1/6/3/2/1d16328afbff8b7fb8d52d5bfb84d9540cd24204.jpg",

    },
    2: {
        "nome" : "Itachi Uchiha",
        "Cla" : "Uchiha",
        "Vila" : "Oculta das Folhas",
        "Ocupacao" : "Capitão da Anbu",
        "Habilidades" : "Sharingan",
        "imagem" : "https://static.wikia.nocookie.net/shinobi-striker/images/b/bb/Itachi.png/revision/latest?cb=20211116160720",
    },
    3: {
        "nome" : "Jiraiya",
        "Cla" : "Hatake",
        "Vila" : "Oculta das Folhas",
        "Ocupacao" : "Escritor",
        "Habilidades" : "Eremita dos Sapos",
        "imagem" : "https://static.wikia.nocookie.net/naruto/images/1/13/Jiraiya_%28Render%29.png/revision/latest?cb=20220430165838&path-prefix=pt-br",
    },
    4: {
        "nome" : "Hashirama Senju",
        "Cla" : "Senju",
        "Vila" : "Oculta das Folhas",
        "Ocupacao" : "Lider do clã Senju",
        "Habilidades" : "Estilo Madeira",
        "imagem" : "https://static.wikia.nocookie.net/naruto/images/5/57/Hashirama_Full.png/revision/latest?cb=20130514231154&path-prefix=pt-br",
    }
}

def gerar_id():
   id = len(personagens) +1
   return id

def criar_personagem(nome,cla,vila,ocupacao,habilidades,imagem):
   personagens[gerar_id()] = {
       "nome" : nome, "cla" : cla, "vila" : vila, "ocupacao" : ocupacao, "habilidades" : habilidades, "imagem" : imagem
   }

def retornar_personagens():
       return personagens
   
def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}

def atualizar_personagem(id:int, dados_personagem):
    personagens[id] = dados_personagem

def remover_personagem(id:int):
    del personagens[id]
