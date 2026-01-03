from flask import Flask, render_template, request, redirect, url_for

tarefas = [
    
]

def quantidade_tarefas():
    qnt_tarefas_pendente = 0
    qnt_tarefas_concluida = 0
    for tarefa in tarefas:
        if tarefa["status"] == False:
            qnt_tarefas_pendente += 1
            continue
        qnt_tarefas_concluida += 1
    quantidade = {
        "qnt_concluidas": qnt_tarefas_concluida,
        "qnt_pendentes": qnt_tarefas_pendente,
        "qnt_todas":qnt_tarefas_pendente + qnt_tarefas_concluida
        }
    return quantidade


app = Flask(__name__)

@app.route("/")
def index():
    quantidade = quantidade_tarefas()
    return render_template("index.html", tarefas=tarefas, quantidade=quantidade)

@app.route("/escolha_aba/<int:id>")
def escolha_aba(id):
    quantidade = quantidade_tarefas()
    return render_template('index.html', id=id, tarefas=tarefas, quantidade=quantidade)

@app.route("/atualizar_status/<int:id_tarefa>", methods=["POST"])
def atualizar_status(id_tarefa):
    if (tarefas[id_tarefa]["status"] == False):
        tarefas[id_tarefa]["status"] = True
    else:
        tarefas[id_tarefa]["status"] = False
    return redirect(url_for('index'))

@app.route("/adicionar_tarefa", methods=["POST"])
def adicionar_tarefa():
    tarefa = request.form["tarefa"]
    descricao = request.form["descricao"]
    if (len(tarefas) > 0):
        id = tarefas[-1]["id"] + 1
    else:
        id = 0
    tarefas.append(
        {
            "id": id,
            "tarefa": tarefa,
            "descricao": descricao,
            "status": False
        })
    return redirect(url_for('index'))

@app.route("/excluir_tarefa/<int:id>")
def excluir_tarefa(id):
    del tarefas[id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)