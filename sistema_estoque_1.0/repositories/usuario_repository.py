from banco import conector

#admin; DROP DATABASE; ["adiministrador","admin", "123", "administrador"]
# usuario(nome: "administrador")

def buscar_por_login(login):
    conexao = conector()
    usuario = conexao.execuute(
        """
        SELECT * FROM usuario WHERE loguin = ?
        """, 
        (login,)
    ).fetchone()
    return usuario