usuarios = [
    {"id": 21, "nome": "Aline", "plano": "Premium"},
    {"id": 22, "nome": "Bruno", "plano": "Básico"},
    {"id": 23, "nome": "Cesar", "plano": "Premium"},
    {"id": 24, "nome": "Dani", "plano": "Básico"}
]

filmes = [
    {"cod": "F1", "titulo": "Aventura Total", "genero": "Ação"},
    {"cod": "F2", "titulo": "Noite de Terror", "genero": "Terror"},
    {"cod": "F3", "titulo": "Amor em Paris", "genero": "Romance"},
    {"cod": "F4", "titulo": "Risos Sem Fim", "genero": "Comédia"}
]

avaliacoes = [
    {"idUsuario": 21, "codFilme": "F1", "nota": 9},
    {"idUsuario": 21, "codFilme": "F2", "nota": 4},
    {"idUsuario": 22, "codFilme": "F3", "nota": 6},
    {"idUsuario": 23, "codFilme": "F4", "nota": 3},
    {"idUsuario": 24, "codFilme": "F1", "nota": 8}
]

def usuariosquederamnotamenorquecinco (usuarios, filmes, avaliacoes):

    if len(usuarios) == 0 or len(filmes) == 0 or len(avaliacoes) == 0:
        return None
    
    i = 0
    idusuariosmenosquecinco = []
    idfilmecomnotabaixa = []
    nomefilmecomnotabaixa = []
    nomeusuariosmenosquecinco = []

    while i < len(avaliacoes):
        if avaliacoes[i]["nota"] < 5:
            idusuariosmenosquecinco.append(avaliacoes[i]["idUsuario"])
            idfilmecomnotabaixa.append(avaliacoes[i]["codFilme"])
        i += 1

    j = 0 
    while j < len(filmes): 
        if filmes[j]["cod"] in idfilmecomnotabaixa:
            nomefilmecomnotabaixa.append(filmes[j]["titulo"])
        j += 1
    k = 0 
    while k < len(usuarios):
        if usuarios[k]["id"] in idusuariosmenosquecinco:
            nomeusuariosmenosquecinco.append(usuarios[k]["nome"])
        k += 1

    return nomeusuariosmenosquecinco, nomefilmecomnotabaixa

print(usuariosquederamnotamenorquecinco(usuarios, filmes, avaliacoes))

