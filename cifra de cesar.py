try:
    txt = str(input('Qual senha você deseja criptografar? '))
    while txt == '':
        txt = str(input('Qual senha você deseja criptografar? '))
    desloc = input('Qual o deslocamento de letras que deseja? ')
    while not desloc.isdigit(): # confirma se o deslocamento for um numero, se nao, repete
        desloc = input('Qual o deslocamento de letras que deseja? ')
    desloc = int(desloc)

    senha_criptografada = ''

#PROGRAMA PRINCIPAL
    lista_letras = list(txt)
    for letras in lista_letras:
        letras_ascii = ord(letras) + desloc
        while letras_ascii > 126: # se a letra convertida em ascii for maior que 126, ele diminiu 93
            letras_ascii -= 93 # preciso deixar a letra dentro do limite ascii, que é 32 a 126
        while letras_ascii < 33: # se a letra convertida em ascii for menor que 33, ele aumenta 93
            letras_ascii += 93
        senha_criptografada += chr(letras_ascii)

    print(f'A senha "{txt}" criptografada com um deslocamento de {desloc} caracteres, é "{senha_criptografada}"')
except:
    print('Ocorreu algum erro inesperado! Reinicie o programa')
finally:
    print('Volte sempre!')