#import mysql-Connector 
import sqlite3

def conectar():
    conexao = sqlite3.connect("estoque.db")
    return conexao

def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(""" """)
    cursor.execute(""" CREATE TABLE IF NOT EXISTS ususarios
    ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL, 
    loguin TEXT UNIQUE NOT NULL,
    senha TEXT UNIQUE NOT NULL,  
    perfil TEXT NOT NULL)""")

    cursor.execute(""" CREATE TABELA IF NOT EXISTE produtos
    ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL, 
    tipo TEXT NOT NULL, 
    quantidade INTERGER NOT NULL, 
    valor REAL NOT NULL, 
    enderaco TEXT NOT NULL,
    estoque_minimo INTEGER NOT NULL, 
    estoque_maximo INTEGER NOT NULL)""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTE movimentacoes
    ( id  INTERGER PRIMARY KEY AUTOINCREMENT, 
    produto_id INTEGER NOT NULL) 
    tipo TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data_hora TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)""")

    cursor.execute(""" INSERT OR IGNORE INTO usuarios
        (nome, login, senha, perfil)
        VALUES (?, ?, ?, ?)""", 
        ("Administrador",
        "admin",
        "123",
        "Administrador"
    ))
    cursor.execute(""" INSERT OR IGNORE INTO usuarios
        (nome, login, senha, perfil)
        VALUES (?, ?, ?, ?) """, 
        ( "Operador",
        "operador",
        "123",
        "Operador"
    ))

    conexao.commit()
    conexao.close()
criar_banco()