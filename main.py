from funcao import (
    menu,
    cadastrar_caminhao,
    listar_caminhoes,
    procurar_placa,
    procurar_motorista,
    procurar_cidade,
    procurar_estado,
    procurar_carga,
    alterar_caminhao,
    remover_caminhao,
    estatisticas
)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

while True:

    menu()

    opcao = input("Escolha uma opção: ")

    print()

    if opcao == "1":
        cadastrar_caminhao()

    elif opcao == "2":
        listar_caminhoes()

    elif opcao == "3":
        procurar_placa()

    elif opcao == "4":
        procurar_motorista()

    elif opcao == "5":
        procurar_cidade()

    elif opcao == "6":
        procurar_estado()

    elif opcao == "7":
        procurar_carga()

    elif opcao == "8":
        alterar_caminhao()

    elif opcao == "9":
        remover_caminhao()

    elif opcao == "10":
        estatisticas()

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("❌ Opção inválida!")
