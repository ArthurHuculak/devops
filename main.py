import json
import os
import sys


ARQUIVO = "tarefas.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)


def add(desc):
    tarefas = carregar()
    tarefas.append({"desc": desc, "feita": False})
    salvar(tarefas)
    print("adicionado:", desc)


def listar():
    tarefas = carregar()
    for i, t in enumerate(tarefas, 1):
        s = "x" if t["feita"] else " "
        print(f"{i}. [{s}] {t['desc']}")


def done(i):
    tarefas = carregar()
    tarefas[i - 1]["feita"] = True
    salvar(tarefas)


def remove(i):
    tarefas = carregar()
    tarefas.pop(i - 1)
    salvar(tarefas)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    if cmd == "add":
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        listar()
    elif cmd == "done":
        done(int(sys.argv[2]))
    elif cmd == "remove":
        remove(int(sys.argv[2]))
    else:
        print("uso: add / list / done N / remove N")


