textinho = "ana"
textao = "banana"

def conta_subtexto(textinho, textao):

    # Se o subtexto estiver vazio ou for maior que o texto principal,
    # não é possível encontrar nenhuma ocorrência.
    if len(textinho) == 0 or len(textinho) > len(textao):
        return 0

    # Contador de ocorrências encontradas
    contador = 0

    # Tamanho do subtexto procurado
    t = len(textinho)

    # Índice que percorrerá o texto principal
    i = 0

    # Percorre todas as posições possíveis onde o subtexto
    # pode começar dentro do texto principal
    while i <= len(textao) - t:

        # Extrai um trecho do texto principal
        # com o mesmo tamanho do subtexto
        trecho = textao[i:i+t]

        # Verifica se o trecho é igual ao subtexto procurado
        if trecho == textinho:

            # Encontrou uma ocorrência
            contador += 1

        # Avança para a próxima posição
        i += 1

    # Retorna a quantidade total encontrada
    return contador


print(conta_subtexto("ana", "banana"))