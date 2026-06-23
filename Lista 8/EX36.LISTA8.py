alunos = [
    {"ra": 101, "nome": "João", "curso": "ADS"},
    {"ra": 102, "nome": "Maria", "curso": "ADS"},
    {"ra": 103, "nome": "Carlos", "curso": "SI"}
]

disciplinas = [
    {"cod": "D1", "nome": "Python"},
    {"cod": "D2", "nome": "Banco"},
    {"cod": "D3", "nome": "POO"}
]

matriculas = [
    {"ra": 101, "materias": ["D1"]},
    {"ra": 101, "materias": ["D2", "D3"]},
    {"ra": 102, "materias": ["D1"]},
    {"ra": 103, "materias": ["D3"]}
]

def mediamatriculasumamateria(alunos, matriculas, curso): 

    qtd = 0 
    soma = 0 

    i = 0 

    while i < len(alunos): 

        raaluno = alunos[i]["ra"]

        if alunos[i]["curso"] == curso: 
            qtd += 1 
            cont = 0 

            j = 0 
            while j < len(matriculas):
                if matriculas[j]["ra"] == raaluno:
                    if len(matriculas[j]["materias"]) == 1: 
                        cont += 1
                j +=1
            
            soma += cont
            media = soma / qtd
        i += 1
    return media
print(mediamatriculasumamateria(alunos, matriculas, "ADS"))