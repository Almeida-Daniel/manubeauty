# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:36:46 2021

@author: Daniel Souza
"""

import sqlite3

# função para criar um novo cliente no BD
def criarCliente(nome,datanasc,fone):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO Cliente (nome, datanasc,fone)
                VALUES (?, ?, ?)''', (nome, datanasc, fone))
    
    conn.commit()
    conn.close()

# função para criar um novo serviço no BD
def criarServico(nome, valor, datacriacao):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO Servico (nome, valor, datacriacao)
                VALUES ( ?, ? , ?)''', (nome, valor, datacriacao))
    conn.commit()
    conn.close()
# função que cria uma nova reserva (serviço associado a cliente)   
def criarServicoCliente(nomecliente, servicoid, dataagendada):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT id FROM Cliente WHERE nome = ?', (nomecliente,))
    cliente_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO ServicoCliente (cliente_id, servico_id, dataagendada)
                VALUES (?, ?, ?)''', (cliente_id, servicoid, dataagendada))
    conn.commit()

# Função para consultar reserva dado nome do cliente e data da reserva
def consultarReserva(cliente, datareserva):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT Cliente.nome, Servico.nome, ServicoCliente.dataagendada,
                Servico.valor FROM
                Cliente,Servico JOIN ServicoCliente ON
                (Cliente.id = ServicoCliente.cliente_id 
                AND Servico.id = ServicoCliente.servico_id)
                WHERE (Cliente.nome = ? AND ServicoCliente.dataagendada = ?) ''',
                       (cliente, datareserva))
    dados = cur.fetchall()  # obtém todas as rows e transforma numa lista de tuplas
    if len(dados) == 0:
        print('Nenhuma reserva encontrada')
    else:
        print('Cliente: ', dados[0][0])
        print('Serviços Agendados: ', end = '\n')
        total = 0
        for i in range(len(dados)):
            total += dados[i][3]
            print(f'{i+1} - ', dados[i][1], 'valor: ', dados[i][3],  end= '\n')
        print('Data de agendamento: ', datareserva)
        print('Valor total: ', total)
    conn.close()
    
    # Função para atualizar os dados cadastrais de um cliente
def atualizarCliente(nomecliente, novonome, novofone, novadata):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    if novonome == '' and novadata == '':
        cur.execute('''UPDATE Cliente SET fone = ? WHERE nome = ?''',
                    (novofone, nomecliente))
    elif novofone == '' and novadata == '':
        cur.execute('''UPDATE Cliente SET nome = ? WHERE nome = ?''',
                    (novonome, nomecliente))
    else:
        cur.execute('''UPDATE Cliente SET datanasc = ? WHERE nome = ?''',
                    (novadata, nomecliente))
    conn.commit()
    conn.close()
# Função que consulta o total de clientes no banco
def totalClientes():
    conn = sqlite3.connect('manubeauty.sqlite')
    cur  = conn.cursor()
    cur.execute('SELECT COUNT(Cliente.id) FROM Cliente')
    total = cur.fetchone()[0]
    print('Total de clientes atualmente:', total)
    conn.close()
    # Função que mostra os clientes agendados para uma data
def clientePorData(data):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT DISTINCT Cliente.nome FROM Cliente JOIN ServicoCliente
                ON Cliente.id = ServicoCliente.cliente_id
                WHERE ServicoCliente.dataagendada = ?''', (data, ))
    listaclientes = cur.fetchall()
    if len(listaclientes) == 0:
        print('Nenhum cliente encontrado para esta data')
    else:
        print('Lista de clientes para ', data, ':')
        for i in range(len(listaclientes)):
            print(' ----- ' , listaclientes[i][0], ' ------')
    conn.close()

def excluirReserva(nomecliente,dataagendada):
    conn = sqlite3.connect('manubeauty.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT id FROM Cliente WHERE nome = ? ''', (nomecliente,))
    cliente_id = cur.fetchone()[0]
    if cliente_id is None:
        print('Cliente não encontrado para exclusão da reserva')
    else:
        cur.execute('''DELETE FROM ServicoCliente WHERE ServicoCliente.cliente_id = ?
                    AND dataagendada = ? ''', (cliente_id,dataagendada))
        conn.commit()
        print(f'Reserva de {nomecliente} para {dataagendada} excluída com sucesso!')
    conn.close()
# =============================================================================
#     for row in cur.execute(script):
#         print(str(row[0]), str(row[1]), str(row[2]))
# =============================================================================



    
   