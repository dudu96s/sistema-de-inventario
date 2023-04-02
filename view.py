import sqlite3 as lite
from datetime import datetime

# Criando Conexão
con = lite.connect('dados.db')

# Inserir Inventário


def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventorio (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Deletar Inventario
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventorio WHERE id=?"
        cur.execute(query, i)


# Atualizar Inventário
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventorio")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Item no Inventário
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventorio WHERE id=?", (id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens