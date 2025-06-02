from flask import Flask, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Caminho para o banco de dados SQLite
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def init_db():
    """Cria o banco de dados e a tabela, se não existirem."""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

@app.route("/")
def index():
    """Renderiza a página inicial com o botão START."""
    return render_template("index.html")

@app.route("/start_process", methods=["GET"])
def start_process():
    """
    Quando o usuário clicar no botão, esta rota
    será chamada. Vamos inserir uma linha na tabela.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO processos DEFAULT VALUES")
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/listar")
def listar_processos():
    """
    (Opcional) Rota para listar todos os registros
    inseridos, para verificar que está funcionando.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp FROM processos ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    html = "<h2>Processos Iniciados</h2><ul>"
    for r in rows:
        html += f"<li>#{r[0]} em {r[1]}</li>"
    html += "</ul><a href='/'>← Voltar</a>"
    return html

if __name__ == "__main__":
    init_db()  # Garante que o DB foi criado
    app.run(debug=True, port=5000)
