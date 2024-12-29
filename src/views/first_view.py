def introduction_page():
    message='''
        Sistema Cadastral

        [1]     Cadastrar pessoa
        [2]     Buscar pessoa
        [5]     Sair

    '''
    print(message)
    command = input('Comando:       ')
    return command