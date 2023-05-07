def exibir_problemas_aritmeticos(problemas, exibir_respostas=False):
    """
    Função que exibe os problemas aritméticos de forma vertical e lado a lado.
    
    Args:
        problemas (list): lista de strings contendo os problemas aritméticos.
        exibir_respostas (bool, opcional): se True, exibe as respostas dos problemas.
            Default: False.
    """
    # Verifica se a lista de problemas é vazia
    if not problemas:
        print("Lista de problemas vazia!")
        return
    
    # Verifica se todos os problemas têm o mesmo tamanho
    tamanho_problema = len(problemas[0])
    if not all(len(p) == tamanho_problema for p in problemas):
        print("Todos os problemas devem ter o mesmo tamanho!")
        return
    
    # Inicializa as listas que vão armazenar os elementos dos problemas
    operadores = []
    numeros = []
    
    # Percorre os problemas e extrai os operadores e números
    for problema in problemas:
        op, num = problema.split()
        operadores.append(op)
        numeros.append(num)
    
    # Imprime os problemas e as respostas (se solicitado)
    for i in range(len(problemas)):
        print(numeros[i][::-1] + " " + operadores[i] + " " + numeros[i])
        print("-" * tamanho_problema)
    
    if exibir_respostas:
        respostas = []
        for i in range(len(problemas)):
            if operadores[i] == "+":
                respostas.append(str(int(numeros[i]) + int(numeros[i][::-1])))
            else:
                respostas.append(str(int(numeros[i]) - int(numeros[i][::-1])))
        print(" " * (tamanho_problema - len(respostas[0])) + " ".join(respostas))
