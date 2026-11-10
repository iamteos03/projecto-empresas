"""Backend: API REST (FastAPI + SQLite) para o CRUD de empresas."""
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

DB = Path(__file__).parent / "empresas.db"

app = FastAPI(title="Cadastro de Empresas", version="1.0")


def conn():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def criar_tabela():
    with conn() as c:
        c.execute(
            """CREATE TABLE IF NOT EXISTS empresas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nif TEXT,
                telefone TEXT,
                cidade TEXT
            )"""
        )


criar_tabela()


class Empresa(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nome: str = Field(min_length=1, max_length=100)
    nif: str = Field(default="", max_length=30)
    telefone: str = Field(default="", max_length=30)
    cidade: str = Field(default="", max_length=60)


@app.get("/")
def raiz():
    return {"mensagem": "API de Cadastro de Empresas a funcionar. Veja /docs"}


# CREATE
@app.post("/empresas", status_code=201)
def criar(e: Empresa):
    with conn() as c:
        cur = c.execute(
            "INSERT INTO empresas(nome, nif, telefone, cidade) VALUES(?,?,?,?)",
            (e.nome, e.nif, e.telefone, e.cidade),
        )
        return {"id": cur.lastrowid, **e.model_dump()}


# READ (todas)
@app.get("/empresas")
def listar():
    with conn() as c:
        return [dict(r) for r in c.execute("SELECT * FROM empresas ORDER BY id")]


# READ (uma)
@app.get("/empresas/{id}")
def obter(id: int):
    with conn() as c:
        r = c.execute("SELECT * FROM empresas WHERE id=?", (id,)).fetchone()
    if not r:
        raise HTTPException(404, "Empresa não encontrada")
    return dict(r)


# UPDATE
@app.put("/empresas/{id}")
def atualizar(id: int, e: Empresa):
    with conn() as c:
        cur = c.execute(
            "UPDATE empresas SET nome=?, nif=?, telefone=?, cidade=? WHERE id=?",
            (e.nome, e.nif, e.telefone, e.cidade, id),
        )
    if cur.rowcount == 0:
        raise HTTPException(404, "Empresa não encontrada")
    return {"id": id, **e.model_dump()}


# DELETE
@app.delete("/empresas/{id}")
def apagar(id: int):
    with conn() as c:
        cur = c.execute("DELETE FROM empresas WHERE id=?", (id,))
    if cur.rowcount == 0:
        raise HTTPException(404, "Empresa não encontrada")
    return {"apagado": id}
