import json

arquivo_banco='alunos.json'

def carregar_dados():
    try:
        with open(arquivo_banco,"r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileExistsError:                 
        return[]

def salvar_dados(alunos):
    try:
        with open(arquivo_banco,"w", encoding="utf=8") as arquivo:

            json.dump(alunos,arquivo, indent=4,ensure_ascii=False)

        print("\ndados salvos com sucesso!")

    except Exception as e :
        print(f"\erro ao salvar dados: {e}")

def criar_id(alunos):

    if len(alunos) == 0:
        novo_id = 1 
    else:
        novo_id = alunos[-1]["id"] + 1 
    return novo_id



