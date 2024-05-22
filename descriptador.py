def descriptador(senha, cont):
    senha_nova = ''
    for i in senha:
        numeros_letras = ord(i) + cont
        # Se o valor estiver abaixo de 33, adicionamos 93 para envolvê-lo de volta dentro do intervalo 33-126
        # Se estiver acima de 126, subtraímos 93 para trazê-lo de volta para dentro do intervalo
        while numeros_letras < 33:
            numeros_letras += 93
        while numeros_letras > 126:
            numeros_letras -= 93
        senha_nova += chr(numeros_letras)
    return senha_nova

# Solicitar a senha ao usuário
senha = input("Digite a senha: ")

# Loop de 1 a 92
for cont in range(1, 93):
    print("Senha:", descriptador(senha, cont))