# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:45:10 2021

@author: Daniel Souza
"""

import sqlite3

#abre a conexão com o db

conn = sqlite3.connect('manubeauty.sqlite')
cur = conn.cursor()

#Cria algumas tabelas

cur.executescript('''
DROP TABLE IF EXISTS Cliente;
DROP TABLE IF EXISTS Servico;
DROP TABLE IF EXISTS ServicoCliente;


CREATE TABLE Cliente ( 
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    datanasc TEXT,
    fone TEXT
    );

CREATE TABLE Servico (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    valor INTEGER,
    datacriacao TEXT);

CREATE TABLE ServicoCliente (
    cliente_id INTEGER,
    servico_id INTEGER,
    dataagendada TEXT,
    PRIMARY KEY (cliente_id, servico_id)
    );

''')
conn.commit()