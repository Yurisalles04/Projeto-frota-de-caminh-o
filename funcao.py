# ============================================================
#              🚛 SISTEMA DE CONTROLE DE FROTA
# ============================================================

# Lista que irá armazenar os caminhões
frota = []

# ============================================================
# FUNÇÃO: NORMALIZAR TEXTO
# ============================================================

def normalizar(texto):

    texto = texto.strip().lower()

    return texto


# ============================================================
# FUNÇÃO: NORMALIZAR ESTADO
# ============================================================

def normalizar_estado(estado):

    estado = normalizar(estado)

    if estado == "sao paulo" or estado == "sp":
        return "SP"

    elif estado == "parana" or estado == "pr":
        return "PR"

    elif estado == "minas gerais" or estado == "mg":
        return "MG"

    elif estado == "rio de janeiro" or estado == "rj":
        return "RJ"

    elif estado == "santa catarina" or estado == "sc":
        return "SC"

    elif estado == "rio grande do sul" or estado == "rs":
        return "RS"

    elif estado == "bahia" or estado == "ba":
        return "BA"

    elif estado == "goias" or estado == "go":
        return "GO"

    else:
        return estado.upper()
# ============================================================
# FUNÇÃO: CADASTRAR CAMINHÃO
# ============================================================

def cadastrar_caminhao():

    print()
    print("====================================")
    print("       CADASTRAR CAMINHÃO")
    print("====================================")

    placa = input("Digite a placa: ")
    modelo = input("Digite o modelo: ")
    motorista = input("Digite o motorista: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    carga = str(input("Digite o tipo de carga: "))

    # Padronizando as informações
    placa = placa.strip().upper()
    modelo = modelo.strip()
    motorista = motorista.strip()
    cidade = cidade.strip()
    estado = normalizar_estado(estado)
    carga = carga.strip()

    # Verificar se a placa já está cadastrada

    placa_existe = False

    for caminhao in frota:

        if caminhao["placa"] == placa:

            placa_existe = True

    if placa_existe:

        print()
        print("❌ Essa placa já está cadastrada!")

        return

    # Criando o caminhão

    caminhao = {
        "placa": placa,
        "modelo": modelo,
        "motorista": motorista,
        "cidade": cidade,
        "estado": estado,
        "carga": carga
    }

    # Adicionando na frota

    frota.append(caminhao)

    print()
    print("✅ Caminhão cadastrado com sucesso!")


# ============================================================
# FUNÇÃO: LISTAR CAMINHÕES
# ============================================================

def listar_caminhoes():

    print()
    print("====================================")
    print("          FROTA CADASTRADA")
    print("====================================")

    if len(frota) == 0:

        print("Nenhum caminhão cadastrado.")

        return

    for numero in range(len(frota)):

        caminhao = frota[numero]

        print()
        print("Caminhão", numero + 1)
        print("----------------------------")

        print("Placa:", caminhao["placa"])
        print("Modelo:", caminhao["modelo"])
        print("Motorista:", caminhao["motorista"])
        print("Cidade:", caminhao["cidade"])
        print("Estado:", caminhao["estado"])
        print("Carga:", caminhao["carga"])


# ============================================================
# FUNÇÃO: PROCURAR POR PLACA
# ============================================================

def procurar_placa():

    print()
    print("====================================")
    print("          PROCURAR CAMINHÃO")
    print("====================================")

    placa = input("Digite a placa: ")

    placa = placa.strip().upper()

    encontrado = False

    for caminhao in frota:

        if caminhao["placa"] == placa:

            print()
            print("✅ CAMINHÃO ENCONTRADO!")
            print("----------------------------")

            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Cidade:", caminhao["cidade"])
            print("Estado:", caminhao["estado"])
            print("Carga:", caminhao["carga"])

            encontrado = True

    if encontrado == False:

        print()
        print("❌ Caminhão não encontrado.")


# ============================================================
# FUNÇÃO: PROCURAR POR MOTORISTA
# ============================================================

def procurar_motorista():

    print()
    print("====================================")
    print("          PROCURAR MOTORISTA")
    print("====================================")

    nome = input("Digite o nome do motorista: ")

    nome = normalizar(nome)

    encontrado = False

    for caminhao in frota:

        motorista = normalizar(
            caminhao["motorista"]
        )

        if motorista == nome:

            print()
            print("Caminhão encontrado:")
            print("----------------------------")

            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Cidade:", caminhao["cidade"])
            print("Estado:", caminhao["estado"])
            print("Carga:", caminhao["carga"])

            encontrado = True

    if encontrado == False:

        print()
        print("❌ Nenhum caminhão encontrado.")


# ============================================================
# FUNÇÃO: PROCURAR POR CIDADE
# ============================================================

def procurar_cidade():

    print()
    print("====================================")
    print("          PROCURAR POR CIDADE")
    print("====================================")

    cidade = input("Digite a cidade: ")

    cidade = normalizar(cidade)

    encontrado = False

    for caminhao in frota:

        cidade_caminhao = normalizar(
            caminhao["cidade"]
        )

        if cidade_caminhao == cidade:

            print()
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Estado:", caminhao["estado"])
            print("Carga:", caminhao["carga"])

            encontrado = True

    if encontrado == False:

        print()
        print("❌ Nenhum caminhão encontrado nessa cidade.")


# ============================================================
# FUNÇÃO: PROCURAR POR ESTADO
# ============================================================

def procurar_estado():

    print()
    print("====================================")
    print("          PROCURAR POR ESTADO")
    print("====================================")

    estado = input("Digite o estado: ")

    estado = normalizar_estado(estado)

    encontrado = False

    for caminhao in frota:

        if caminhao["estado"] == estado:

            print()
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Cidade:", caminhao["cidade"])
            print("Carga:", caminhao["carga"])

            encontrado = True

    if encontrado == False:

        print()
        print("❌ Nenhum caminhão encontrado nesse estado.")


# ============================================================
# FUNÇÃO: PROCURAR POR CARGA
# ============================================================

def procurar_carga():

    print()
    print("====================================")
    print("          PROCURAR POR CARGA")
    print("====================================")

    carga = input("Digite o tipo de carga: ")

    carga = normalizar(carga)

    encontrado = False

    for caminhao in frota:

        carga_caminhao = normalizar(
            caminhao["carga"]
        )

        if carga_caminhao == carga:

            print()
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Cidade:", caminhao["cidade"])
            print("Estado:", caminhao["estado"])

            encontrado = True

    if encontrado == False:

        print()
        print("❌ Nenhum caminhão encontrado.")


# ============================================================
# FUNÇÃO: ALTERAR CAMINHÃO
# ============================================================

def alterar_caminhao():

    print()
    print("====================================")
    print("          ALTERAR CAMINHÃO")
    print("====================================")

    placa = input("Digite a placa do caminhão: ")

    placa = placa.strip().upper()

    encontrado = False

    for caminhao in frota:

        if caminhao["placa"] == placa:

            encontrado = True

            print()
            print("Caminhão encontrado!")

            print("Deixe vazio para manter a informação atual.")

            modelo = input(
                "Novo modelo: "
            )

            motorista = input(
                "Novo motorista: "
            )

            cidade = input(
                "Nova cidade: "
            )

            estado = input(
                "Novo estado: "
            )

            carga = input(
                "Nova carga: "
            )

            if modelo != "":
                caminhao["modelo"] = modelo.strip()

            if motorista != "":
                caminhao["motorista"] = motorista.strip()

            if cidade != "":
                caminhao["cidade"] = cidade.strip()

            if estado != "":
                caminhao["estado"] = normalizar_estado(
                    estado
                )

            if carga != "":
                caminhao["carga"] = carga.strip()

            print()
            print("✅ Caminhão alterado com sucesso!")

    if encontrado == False:

        print()
        print("❌ Caminhão não encontrado.")


# ============================================================
# FUNÇÃO: REMOVER CAMINHÃO
# ============================================================

def remover_caminhao():

    print()
    print("====================================")
    print("          REMOVER CAMINHÃO")
    print("====================================")

    placa = input("Digite a placa: ")

    placa = placa.strip().upper()

    encontrado = False

    for caminhao in frota:

        if caminhao["placa"] == placa:

            encontrado = True

            confirmacao = input(
                "Deseja realmente remover? (S/N): "
            )

            confirmacao = confirmacao.strip().upper()

            if confirmacao == "S":

                frota.remove(caminhao)

                print()
                print("✅ Caminhão removido!")

            else:

                print()
                print("Operação cancelada.")

            break

    if encontrado == False:

        print()
        print("❌ Caminhão não encontrado.")


# ============================================================
# FUNÇÃO: ESTATÍSTICAS
# ============================================================

def estatisticas():

    print()
    print("====================================")
    print("           ESTATÍSTICAS")
    print("====================================")

    if len(frota) == 0:

        print("Nenhum caminhão cadastrado.")

        return

    total = len(frota)

    sp = 0
    pr = 0
    mg = 0
    rj = 0
    outros = 0

    for caminhao in frota:

        estado = caminhao["estado"]

        if estado == "SP":

            sp += 1

        elif estado == "PR":

            pr += 1

        elif estado == "MG":

            mg += 1

        elif estado == "RJ":

            rj += 1

        else:

            outros += 1

    print()
    print("Total de caminhões:", total)

    print()
    print("Caminhões por estado:")
    print("SP:", sp)
    print("PR:", pr)
    print("MG:", mg)
    print("RJ:", rj)
    print("Outros:", outros)


# ============================================================
# FUNÇÃO: MENU
# ============================================================

def menu():

    print()
    print("============================================")
    print("          🚛 CONTROLE DE FROTA")
    print("============================================")

    print("1  - Cadastrar caminhão")
    print("2  - Listar caminhões")
    print("3  - Procurar por placa")
    print("4  - Procurar por motorista")
    print("5  - Procurar por cidade")
    print("6  - Procurar por estado")
    print("7  - Procurar por carga")
    print("8  - Alterar caminhão")
    print("9  - Remover caminhão")
    print("10 - Estatísticas")
    print("0  - Sair")

    print("============================================")


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