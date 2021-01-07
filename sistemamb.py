# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:44:30 2021

@author: Daniel Souza
"""

import mbdbfunctions
import mbinterface

print('------------- BEM VINDO(A) ao sistema ManuBeauty -------------')
mbinterface.menu()

while True:
    try:
        opcao = int(input('Digite a opção: '))
        
        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            datanasc = input('Digite a data de nascimento do cliente: ')
            fone = input('Digite o telefone do cliente: ')
            mbdbfunctions.criarCliente(nome,datanasc,fone)
        
        if opcao == 2:
            nomeserv = input('Digite o nome do serviço: ')
            valor = int(input('Digite o valor do serviço: '))
            datacriacao = input('Data de criação do serviço: ')
            mbdbfunctions.criarServico(nomeserv,valor,datacriacao)
        
        if opcao == 3:
            nomecliente = input('Digite o nome da cliente: ')
            datareserva = input('Digite a data da reserva: ')
            print()
            print('Tabela de servicos: ')
            print('1 - Maquiagem') 
            print('2 - Sobrancelhas')    
            print('3 - Unhas')
            print('4 - Pedicure')
            print('5 - LashLifting', end = '\n')
            servico = input('Digite o serviço desejado: ')
            mbdbfunctions.criarServicoCliente(nomecliente, servico, datareserva)
            
        if opcao == 4:
            nomecliente = input('Digite o nome do cliente: ')
            datareserva = input('Digite a data da reserva: ')
            print()
            mbdbfunctions.consultarReserva(nomecliente, datareserva)
            
        if opcao == 5:
            nomecliente = input('Qual cliente deseja atualizar dados? ')
            novonome = input('Digite o novo nome: ')
            novofone = input('Digite o novo telefone: ')
            novadata = input('Digite a nova data de nascimento: ')
            print(novonome, novofone, novadata)
            mbdbfunctions.atualizarCliente(nomecliente, novonome, novofone, novadata)
            
        if opcao == 6:
            mbdbfunctions.totalClientes()
            
        if opcao == 7:
            data = input('Digite a data desejada: ')
            mbdbfunctions.clientePorData(data)
        
        if opcao == 8:
            nomecliente = input('Digite o nome do cliente: ')
            dataagendada = input('Digite a data da reserva a ser excluída: ')
            mbdbfunctions.excluirReserva(nomecliente,dataagendada)
    except:
        print('Dígito não reconhecido')
            
    else:
        novo = input('Deseja continuar? [S/N]')
        if novo in 'Nn': 
            print('Sistema encerrado, volte sempre!')
            break 
        else:
            mbinterface.menu()
              
    

