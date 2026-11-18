import sqlite3
import json
from datetime import date


def conectar(arquivo="cineflix.db", catalogo_arquivo="catalogo.json"):
    conn = sqlite3.connect(arquivo)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS titulos (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano INTEGER NOT NULL,
            duracao_min INTEGER NOT NULL,
            classificacao INTEGER NOT NULL,
            nota REAL NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS visualizacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfil TEXT NOT NULL,
            titulo_id INTEGER NOT NULL,
            minutos INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (titulo_id) REFERENCES titulos(id)
        )
    """)
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM titulos").fetchone()[0]
    if total == 0:
        with open(catalogo_arquivo, "r", encoding="utf-8") as arquivo_json:
            catalogo = json.load(arquivo_json)
        for t in catalogo:
            conn.execute("""
                INSERT INTO titulos
                (id, titulo, tipo, genero, ano, duracao_min, classificacao, nota)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (t["id"], t["titulo"], t["tipo"], t["genero"], t["ano"],
                  t["duracao_min"], t["classificacao"], t["nota"]))
        conn.commit()
        print(f"{len(catalogo)} títulos importados do catalogo.json.")
    return conn


def catalogo(conn):
    return conn.execute("SELECT * FROM titulos ORDER BY id").fetchall()


def registrar(conn, perfil, titulo_id, minutos):
    existe = conn.execute("SELECT id FROM titulos WHERE id = ?", (titulo_id,)).fetchone()
    if existe is None:
        return False
    conn.execute(
        "INSERT INTO visualizacoes (perfil, titulo_id, minutos, data) VALUES (?, ?, ?, ?)",
        (perfil, titulo_id, minutos, date.today().isoformat())
    )
    conn.commit()
    return True


def historico(conn, perfil):
    return conn.execute("""
        SELECT visualizacoes.data, titulos.titulo, visualizacoes.minutos
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        WHERE visualizacoes.perfil = ?
        ORDER BY visualizacoes.id DESC
    """, (perfil,)).fetchall()


def mais_assistidos(conn):
    return conn.execute("""
        SELECT titulos.titulo, COUNT(*) AS vezes
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        GROUP BY titulos.id, titulos.titulo
        ORDER BY vezes DESC, titulos.titulo
        LIMIT 5
    """).fetchall()


def tempo_por_perfil(conn):
    return conn.execute("""
        SELECT perfil, SUM(minutos) AS total
        FROM visualizacoes
        GROUP BY perfil
        ORDER BY total DESC
    """).fetchall()


def dados_relatorio(conn):
    return {
        "data": date.today().isoformat(),
        "mais_assistidos": [
            {"titulo": titulo, "vezes": vezes}
            for titulo, vezes in mais_assistidos(conn)
        ],
        "tempo_por_perfil": [
            {"perfil": perfil, "minutos": total}
            for perfil, total in tempo_por_perfil(conn)
        ]
    }
