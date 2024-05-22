def descriptador(senha, cont):
    senha_nova = ''
    for i in senha:
        numeros_letras = ord(i) + cont
        # se o valor estiver abaixo de 33, adiciono 93 para add de volta dentro do intervalo 33-126
        # se estiver acima de 126, subtraío 93 para trazer de volta para dentro do intervalo
        while numeros_letras < 33:
            numeros_letras += 93
        while numeros_letras > 126:
            numeros_letras -= 93
        senha_nova += chr(numeros_letras)
    return senha_nova

senha = input("Digite a senha: ")

for cont in range(1, 93):
    print("Senha:", descriptador(senha, cont))
