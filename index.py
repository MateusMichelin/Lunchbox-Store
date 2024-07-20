# Imprime o cabeçalho de boas-vindas e o cardápio da loja
print('    Olá, seja bem-vindo a loja de Marmitas do Mateus Mangini Michelin!\n\
     --------------------------Cardápio----------------------------')
print('     ---| Tamanho |  Bife acebolado (BA) | Filé de frango (FF) |---\n\
     ---|    P    |       R$ 16.00       |       R$ 15.00      |---\n\
     ---|    M    |       R$ 18.00       |       R$ 17.00      |---\n\
     ---|    G    |       R$ 22.00       |       R$ 21.00      |---\n\
     --------------------------------------------------------------')

pedir = True
# Valores das marmitas de filé de frango
valorMarmitaFF = [15, 17, 21]
# Valores das marmitas de bife acebolado
valorMarmitaBA = [16, 18, 22]
sabor = ''
# Tamanhos disponíveis das marmitas
marmitas = ['P', 'M', 'G']
valorMarmita = []

# Quantidade de tipos de tamanhos de marmitas
qtdeMarmitas = len(marmitas)
indice = 0

# Loop principal para realizar os pedidos
while pedir:
    # Solicita o sabor da marmita e converte para maiúsculo
    saborMarmita = str(input('Digite o sabor da sua marmita (BA) ou (FF): ')).upper()
    
    # Verifica se o sabor é válido
    if saborMarmita != 'BA' and saborMarmita != 'FF':
        print('Sabor inválido. Tente novamente.\n')
        continue  # Pula para a próxima iteração do loop

    # Solicita o tamanho da marmita e converte para maiúsculo
    tamanhoMarmita = str(input('Digite o tamanho da marmita (P) (M) (G): ')).upper()
    
    # Verifica se o tamanho é válido
    if tamanhoMarmita not in marmitas:
        print('Tamanho inválido. Tente novamente.\n')
        continue  # Pula para a próxima iteração do loop
    
    indice = 0  # Reinicia o índice para cada novo pedido
     
    # Loop para associar o sabor e tamanho ao preço correto
    while indice < qtdeMarmitas:
        if saborMarmita == 'BA':
            sabor = 'Bife Acebolado'
            if tamanhoMarmita == marmitas[indice]:
                valorMarmita.append(valorMarmitaBA[indice])
                
        elif saborMarmita == 'FF':
            sabor = 'Filé de Frango'
            if tamanhoMarmita == marmitas[indice]:
                valorMarmita.append(valorMarmitaFF[indice])
                
        indice += 1
    
    # Imprime o pedido atual
    print('Você pediu um {} no tamanho {}:  R$ {:.2f}'.format(sabor, tamanhoMarmita, valorMarmita[-1]))

    # Pergunta se o usuário deseja fazer mais pedidos
    pedirNovamente = str(input('\nDeseja mais alguma coisa? (S) ou (N): ')).upper()
    
    # Verifica a resposta do usuário para continuar ou encerrar
    if pedirNovamente == 'N':
        pedir = False
        break

# Verifica se houve pedidos válidos
if not valorMarmita:   
    print('Você não selecionou corretamente. Tente novamente')
else:
    # Imprime o valor total a ser pago
    print('\nO valor total a ser pago é de: R$ {:.2f}'.format(sum(valorMarmita)))
