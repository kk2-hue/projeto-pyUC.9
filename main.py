alunos=[]

while True:
    print("n--- MENU PRINCIPAL---")
    print('1. Cadastrar aluno')
    print('2. listar alunos')
    print('3. salvar e sair ')
    opcao = input("escolha umas das opçoes").strip()

    if opcao == "1":
            print("\n[Opção 1 Selecionada: Cadastrar Aluno]")
    elif opcao == "2":
            print("\n[Opção 2 Selecionada: Listar Alunos]")
    elif opcao == "3":
            print("\n\nSaindo do sistema... Até logo!")
            break   
    else:   
        print("\nOpção inválida! Tente novamente.")

__name__=="__main__"