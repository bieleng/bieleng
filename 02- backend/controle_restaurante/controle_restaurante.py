import os

lista_codigo_produto = []
lista_nome_produto = []
lista_preco_produto = []

# função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# função para mostrar o nome do programa
def mostrar_nome():
    print('---- SISTEMA DE PRODUTOS ----')

# função para mostrar o menu principal
def menu_princ():
    print('1. Administrador')
    print('2. Operador')
    print('0. Sair\n')

# função para mostrar o menu do adm 
def menu_adm():
    print('\n---- MENU ADMINISTRADOR ----\n ')
    print('1. Cadastrar produtos')
    print('2. Listar produtos')
    print('3. Alterar produtos')
    print('4. Apagar produtos')
    print('0. Voltar\n')

# função para mostrar o menu do operador 
def menu_opr():
    print('\n---- MENU OPERADOR ----\n ')
    print('1. Listar produtos')
    print('2. Realizar pedido')
    print('0. Voltar')

# função de cadastro de poduto
def cadastro_prd():
    limpa_tela() # limpa a tela 
    mostrar_nome() # mosta o nome do programa

    carregar_listas_dos_produtos() # carrega os produtos já cadastrados

     # define o código do produto com base no último código existente ou 1 se não houver
    if lista_codigo_produto:
        codigo_produto = max(lista_codigo_produto) + 1 # pega o último código e soma 1
    else:
        codigo_produto = 1 # começa com 1 se não tiver produto nenhum

    while True: # inicia o cadastro dos produtos
        print(f'\nCódigo do produto gerado automaticamente: {codigo_produto}')
  
        # cadastro de nome
        nome_produto = input(f'Insira o nome do produto {codigo_produto}: ')
       
        # controle de erro caso o usuário envia uma string vazia no nome do produto
        while nome_produto == "":
            print('\nInsira um nome válido')
            nome_produto = input(f'Insira o nome do produto {codigo_produto}: ')

        # cadastro do preço do produto
        preco_produto = input(f'\nDigite o preço desejado para o produto {nome_produto}: ')

        # validação do preço
        while True:
            preco_tratado = '' # string para armazenar os caracteres válidos
            separador = 0 # contador de vírgula ou ponto
            invalido = 0 # contador de caracteres inválidos

            for i in preco_produto:
                if i == '.' or i == ',':
                    separador += 1 # conta quantos separadores foram usados
                    preco_tratado += ',' # converte qualquer separador para vírgula
                elif i in '1234567890':
                    preco_tratado += i # converte qualquer separador para vírgula
                else:
                    invalido += 1  # encontrou caractere inválido
            
            if preco_produto != '' and separador <= 1 and invalido == 0:
                preco_produto = preco_tratado  # usa o valor final com vírgula
                break  # se tudo estiver certo, sai do laço

            else:
                 print('\nPreço inválido! Use apenas números com ponto ou vírgula. Ex: 10,50 ou 11.99')
                 preco_produto = input(f'\nDigite o preço desejado para o produto {nome_produto}: ')

        # controle de erro caso o usuário envie uma string vazia ou letras no preço
        while preco_produto == '' or preco_produto.isalpha():
            print('\nPreço inválido, insira um preço válido!')
            preco_produto = input(f'\nDigite o preço desejado para o produto {nome_produto}: ')
  
        # adiciona os dados as listas  
        lista_codigo_produto.append(codigo_produto) # adiciona o código do produto na lista dos códigos
        lista_nome_produto .append(nome_produto) # adiciona o nome do produto na lista dos nomes
        lista_preco_produto.append(preco_produto) # adiciona o preço do produto na lista de preços

        #pergunta se o usuário quer continuar o cadastro
        continuar_cadastro = input('\nDeseja cadastrar outro produto (s/n): ').lower() # .lower tranforma tudo oque o usuário envia em letras minusculas

        # controle de erro caso o usuário digite qualquer coisa diferente de 's' ou 'n'
        while continuar_cadastro != 's' and continuar_cadastro != 'n':
            print('\nValor inválido, digite "s" para continuar ou "n" para encerrar')
            continuar_cadastro = input('\nDeseja cadastrar outro produto (s/n): ').lower() # .lower tranforma tudo oque o usuário envia em letras minusculas

        if continuar_cadastro == 'n':  # se o usuário digitar 'n' ele sai do cadastrar produtos
            break
        else:
            codigo_produto += 1 # se não for 'n' passa para o próximo código somando mais 1

    arquivo = open('produtos.txt', 'a+', encoding= 'utf-8') # abre ou cria um arquivo para adicionar os dados armazenados nas listas
    for i in range (len(lista_codigo_produto)): # escreves todos os dados armazenados nas listas

        # cria uma linha com as informações de cada produto
        linha = f'Código: {lista_codigo_produto[i]} - Nome: {lista_nome_produto[i]} - Preço: {lista_preco_produto[i]}\n'
        arquivo.write(linha) # escreve a linha no arquivo
    arquivo.close() # fecha o aquivo depois de escrever tudo

# função para listar os produtos cadastrados
def listar_prd():
    limpa_tela()
    mostrar_nome() # mostra o nome do programa

    arquivo = open('produtos.txt', 'a+', encoding='utf-8')  # abre ou cria o arquivo se não existir, com permissão para leitura e escrita
    arquivo.seek(0)  # move o cursor para o início do arquivo para poder ler seu conteúdo
    linhas = arquivo.readlines()  # lê todas as linhas do arquivo e armazena na variável "linhas"
    arquivo.close()  # fecha o arquivo após a leitura

    print('\n---- PRODUTOS CADASTRADOS ----\n')  # nome da seção listagem

    if len(linhas) == 0:  # verifica se a lista de linhas está vazia
        print('Nenhum produto cadastrado.\n')  # exibe mensagem informando que não há produtos
    else:  # se houver produtos cadastrados
        for linha in linhas:  # percorre cada linha do arquivo
            print(linha.strip())  # remove espaços em branco e quebra de linha do final e imprime o produto
    input('\nPressione qualquer tecla para sair da listagem de produtos: ')  # pausa o programa até o usuário enviar qualquer coisa

# função para manter as listas com as informações de cada produto mesmo depois de reiniciar o programa 
def carregar_listas_dos_produtos(): 
    lista_codigo_produto.clear()
    lista_nome_produto.clear()
    lista_preco_produto.clear() 

    arquivo = open('produtos.txt', 'a+', encoding= 'utf-8') # Abre o arquivo para leitura com codificação UTF-8
    arquivo.seek(0) # move o cursor para o início do arquivo para poder ler
    linhas = arquivo.readlines() # Lê todas as linhas do arquivo e armazena em uma variável
    arquivo.close() # fecha o arquivo depoois da leitura

    for linha in linhas:
        partes = linha.strip().split(' - ')  # Tira espaços extras e separa a linha em partes usando " - "

        if len(partes) == 3:  # garante que há exatamente 3 partes (Código, Nome, Preço)
            codigo_do_prod = int(partes[0].split(': ')[1])  # extrai o código
            nome_do_prod = partes[1].split(': ')[1]         # extrai o nome
            preco_do_prod = partes[2].split(': ')[1]        # extrai o preço

        # adiciona cada dado em sua lista
        lista_codigo_produto.append(codigo_do_prod)
        lista_nome_produto.append(nome_do_prod)
        lista_preco_produto.append(preco_do_prod)

# função para alterar produto
def alterar_prd():
    limpa_tela() # limpa a tela
    mostrar_nome() # mostra o nome do programa
    carregar_listas_dos_produtos()
    listar_prd()
    
    while True:
        codigo_digitado = input('\nInsira o código do produto que deseja alterar: ')

        numeros = '1234567890' # variável para guardar os números para a conversão
        
        # controle de erros na escolha do produto que deseja alterar
        caracteres_validos = '' # string para armazenar os caracteres válidos
        for caractere in codigo_digitado: # verifica cada caractere digitado pelo usuário
            if caractere in numeros: # se oque o usuário digitou está na variável números é pq é um número
                caracteres_validos += caractere # adiciona os números na variável caracteres_validos
        
        if caracteres_validos == codigo_digitado and codigo_digitado != '': # se o código digitado for válido segue o processo
            codigo_alterar = int(codigo_digitado) # adiciona o número validado na variável codigo_alterar e converte para int
            print(f'\nCódigo válido: {codigo_alterar}')
        

        if codigo_alterar in lista_codigo_produto: # verifica se o código digitado existe na lista
            posicao_produto = lista_codigo_produto.index(codigo_alterar) # pega a posição desse produto nas listas

            novo_nome = input('Digite o novo nome do produto: ') # solicita um novo nome
            novo_preco = input('Digite o novo preço do produto: ') # solicita um novo preço

            # validação do preço
            while True:
                preco_tratado = '' # string para armazenar os caracteres válidos
                separador = 0 # contador de vírgula ou ponto
                invalido = 0 # contador de caracteres inválidos

                for i in novo_preco:
                    if i == '.' or i == ',':
                        separador += 1 # conta quantos separadores foram usados
                        preco_tratado += ',' # converte qualquer separador para vírgula
                    elif i in '1234567890':
                        preco_tratado += i # converte qualquer separador para vírgula
                    else:
                        invalido += 1  # encontrou caractere inválido
            
                if novo_preco != '' and separador <= 1 and invalido == 0:
                    novo_preco = preco_tratado  # usa o valor final com vírgula
                    break  # se tudo estiver certo, sai do laço

                else:
                    print('\nPreço inválido! Use apenas números com ponto ou vírgula. Ex: 10,50 ou 11.99')
                    novo_preco = input(f'\nDigite o preço desejado para o produto {codigo_digitado}: ')

            lista_nome_produto[posicao_produto] = novo_nome # atualiza o nome do produto na lista
            lista_preco_produto[posicao_produto] = novo_preco # atualiza o preço do produto na lista

            arquivo = open('produtos.txt', 'w', encoding= 'utf-8') # abre o arquivo para atualizar os produtos

            # reescreve todos os produtos atualizados
            for i in range(len(lista_codigo_produto)):
                linhas = f'Código: {lista_codigo_produto[i]} - Nome: {lista_nome_produto[i]} - Preço: {lista_preco_produto[i]}\n'
                arquivo.write(linhas)
            arquivo.close() # fecha o arquivo após salvar tudo

            print('\nProduto alterado!')

        else: # se o código não estiver na lista mostra que não encontrou 
            print('\nCódigo não encontrado')

        # Pergunta se quer continuar alterando produtos
        continuar_alterando = input('\nDeseja alterar outro produto? (s/n): ').lower()
        while continuar_alterando != 's' and continuar_alterando != 'n':
            print('\nValor inválido, digite "s" para continuar ou "n" para encerrar')
            continuar_alterando = input('\nDeseja alterar outro produto? (s/n): ').lower()

        if continuar_alterando == 'n':
            break

# função para apagar produto
def apagar_prd():
    limpa_tela() # limoa a tela
    mostrar_nome() # mostra o nome do programa
    carregar_listas_dos_produtos() # carrega os produtos do arquivo para as listas
    listar_prd() # lista os produtos cadastardos

    while True:
        print('\n---- APAGAR PRODUTOS ----')
        codigo_apagar_produto = input('\nInsira o código do produto que deseja apagar: ')

        numeros = '1234567890' # números válidos para converter 
        caracteres_validos = ''  # Inicializa string para guardar só os números digitados

        for caractere in codigo_apagar_produto:  # Percorre cada caractere do código digitado
            if caractere in numeros:  # Se o caractere for número, adiciona na string caracteres_validos
                caracteres_validos += caractere

        # Verifica se o que o usuário digitou são apenas números e não está vazio
        if caracteres_validos == codigo_apagar_produto and codigo_apagar_produto != '':
            codigo_apagar = int(codigo_apagar_produto)  # Converte o código válido para inteiro
            print(f'\nCódigo válido: {codigo_apagar}')
        else:
            print('\nCódigo inválido! Digite apenas números.')  # Informa erro se código inválido
            continue  # Volta para o início do loop para tentar novamente

        # Verifica se o código existe na lista de produtos
        if codigo_apagar in lista_codigo_produto:
            posicao_produto = lista_codigo_produto.index(codigo_apagar)  # Encontra a posição do produto nas listas

            # Remove o produto das listas, usando a posição encontrada
            lista_codigo_produto.pop(posicao_produto)
            lista_nome_produto.pop(posicao_produto)
            lista_preco_produto.pop(posicao_produto)

            # Reabre o arquivo para reescrever os dados atualizados, sem o produto removido
            arquivo = open('produtos.txt', 'w', encoding='utf-8')
            for i in range(len(lista_codigo_produto)):
                linha = f'Código: {lista_codigo_produto[i]} - Nome: {lista_nome_produto[i]} - Preço: {lista_preco_produto[i]}\n'
                arquivo.write(linha)  # Escreve cada linha no arquivo
            arquivo.close()  # Fecha o arquivo após a gravação

            print('\nProduto apagado com sucesso!')  # Confirmação para o usuário

        else:
            print('\nCódigo não encontrado!')  # Caso o código não exista

        
        # Pergunta se o usuário deseja apagar outro produto
        continuar_apagando = input('\nDeseja apagar outro produto? (s/n): ').lower()
        while continuar_apagando != 's' and continuar_apagando != 'n':  # Validação da resposta
            print('\nValor inválido, digite "s" para continuar ou "n" para encerrar')
            continuar_apagando = input('\nDeseja apagar outro produto? (s/n): ').lower()

        if continuar_apagando == 'n':  # Se não quiser apagar mais produtos, sai do loop
            break

# função para realizar pedido
def realizar_pdd():
    limpa_tela() # limpa a tela
    mostrar_nome() # mostra o nome do programa 
    carregar_listas_dos_produtos() # carrega os dados dos produtos cadastrados

    # verifica se há produtos cadastrados
    if len(lista_codigo_produto) == 0:
        print('\nNenhum produto cadastrado.')
        input('\Insira qualquer tecla para voltar ao menu: ')
        return # sai da função para evitar continuar com a lista vazia

    else:
        listar_prd() # lista os produtos cadastrados
            
        total = 0.0
        
        while True:
            print('\n---- REALIZAR PEDIDO ----')
            codigo_pedido = input('\nInsira o código do produto que deseja pedir: ')

            numeros = '1234567890' # define os caracteres válidos para o código
            codigo_valido = '' # váriavel para armazenar apenas os números válidos digitados

            for caractere in codigo_pedido:
                if caractere in numeros:  # verifica se o caractere é um número
                    codigo_valido += caractere  # adiciona o número na váriavel de caracter válido

            # se o código digitado for válido
            if codigo_valido == codigo_pedido and codigo_pedido != '':
                codigo_digitado = int(codigo_pedido)  # converte para inteiro

                if codigo_digitado in lista_codigo_produto:  # verifica se o código existe
                    posicao = lista_codigo_produto.index(codigo_digitado)  # pega a posição do produto nas listas

                    nome_produto = lista_nome_produto[posicao]  # pega o nome do produto

                    preco_str = lista_preco_produto[posicao].replace(',', '.')  # pega o preço do produto e substitui vírgula por ponto para converter
                    preco_produto = float(preco_str) # pega o preço do produto

                    preco_formatado = f'{preco_produto:.2f}'.replace('.', ',')  # formata o preço com vírgula no lugar do ponto

                    print(f'\nProduto escolhido: {nome_produto} - Preço: R${preco_formatado}')  # mostra produto pedido

                    total += preco_produto  # soma o valor do produto ao total

                else:
                    print('\nCódigo não encontrado.')  # caso o código não exista
            else:
                print('\nCódigo inválido.')  # se o código for inválido (letras ou vazio)

            mais_pedidos = input('\nDeseja pedir outro produto? (s/n): ').lower()
            while mais_pedidos != 's' and mais_pedidos != 'n':  # valida se a resposta é s ou n 
                print('\nValor inválido, digite "s" para continuar ou "n" para encerrar')
                mais_pedidos = input('\nDeseja pedir outro produto? (s/n): ').lower()

            if mais_pedidos == 'n':  # encerra pedido se digitar "n"
                break

        total_formatado = f'{total:.2f}'.replace('.', ',')  # formata o total com vírgula no lugar do ponto

        print(f'\nValor total do pedido: R${total_formatado}') # mostra o valor final da compra

        input('\nInsira qualquer tecla para voltar ao menu: ')  # espera o usuário antes de voltar ao menu


while True:
    limpa_tela()
    mostrar_nome()
    menu_princ()
    opcao_principal = input('Escolha uma opção: ')

    if opcao_principal == '1':  # ADMINISTRADOR
        while True:
            limpa_tela()
            mostrar_nome()
            menu_adm()
            opcao_adm = input('Escolha uma opção: ')

            if opcao_adm == '1':
                cadastro_prd()
            elif opcao_adm == '2':
                listar_prd()
            elif opcao_adm == '3':
                alterar_prd()
            elif opcao_adm == '4':
                apagar_prd()
            elif opcao_adm == '0':
                limpa_tela()
                mostrar_nome()
                break  # volta ao menu principal
            else:
                print('\nOpção inválida. Tente novamente.')

    elif opcao_principal == '2':  # OPERADOR
        while True:
            limpa_tela()
            mostrar_nome()
            menu_opr()
            opcao_opr = input('\nEscolha uma opção: ')

            if opcao_opr == '1':
                listar_prd()
            elif opcao_opr == '2':
                realizar_pdd()
            elif opcao_opr == '0':
                limpa_tela()
                mostrar_nome()
                break  # volta ao menu principal
                    
            else:
                print('\nOpção inválida. Tente novamente.')

    elif opcao_principal == '0':  # SAIR
        limpa_tela()
        print('Encerrando o sistema...')
        break

    else:
        print('\nOpção inválida. Digite 1, 2 ou 0.')
