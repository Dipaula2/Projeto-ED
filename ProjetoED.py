class Produto:
    def __init__(self, descricao, peso, valor_compra, valor_venda, fabricante):
        self.descricao = descricao
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.valor_lucro = valor_venda - valor_compra
        self.percentual_lucro = (self.valor_lucro / valor_compra) * 100
        self.fabricante = fabricante

class Fabricante:
    def __init__(self, codigo, marca, site, telefone, uf):
        self.codigo = codigo
        self.marca = marca
        self.site = site
        self.telefone = telefone
        self.uf = uf

class UF:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

fabricantes = []
clientes = []
produtos = []

MAX_FABRICANTES = 5
MAX_CLIENTES = 30
MAX_PRODUTOS = 50

def cadastrar_fabricante():
    if len(fabricantes) >= MAX_FABRICANTES:
        print("Limite máximo de fabricantes atingido. Não é possível adicionar mais fabricantes.")
        return

    while True:
        codigo = input("Digite o código do fabricante: ")
        if not codigo.isdigit():
            print("Código inválido. Digite apenas números.")
            continue
        if any(fab.codigo == int(codigo) for fab in fabricantes):
            print("Código de fabricante já existente. Tente novamente.")
        else:
            break
    marca = input("Digite a marca do fabricante: ")
    site = input("Digite o site do fabricante: ")
    telefone = input("Digite o telefone do fabricante: ")
    sigla_uf = input("Digite a sigla da UF do fabricante: ")
    uf = None
    for estado in estados:
        if estado.sigla == sigla_uf:
            uf = estado
            break
    if uf is not None:
        fabricante = Fabricante(int(codigo), marca, site, telefone, uf)
        fabricantes.append(fabricante)
        print("Fabricante cadastrado com sucesso!")
    else:
        print("UF não encontrada.")

def cadastrar_produto():
    if len(produtos) >= MAX_PRODUTOS:
        print("Limite máximo de produtos atingido. Não é possível adicionar mais produtos.")
        return

    descricao = input("Digite a descrição do produto: ")
    peso = input("Digite o peso do produto: ")
    valor_compra = float(input("Digite o valor de compra do produto: "))
    valor_venda = float(input("Digite o valor de venda do produto: "))
    while True:
        codigo_fabricante = input("Digite o código do fabricante: ")
        if not codigo_fabricante.isdigit():
            print("Código inválido. Digite apenas números.")
            continue
        fabricante = next((fab for fab in fabricantes if fab.codigo == int(codigo_fabricante)), None)
        if fabricante is None:
            print("Fabricante não encontrado. Tente novamente.")
        else:
            break
    produto = Produto(descricao, peso, valor_compra, valor_venda, fabricante)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos_fabricante(codigo_fabricante):
    produtos_fabricante = []
    for produto in produtos:
        if produto.fabricante.codigo == codigo_fabricante:
            produtos_fabricante.append(produto)
    produtos_fabricante.sort(key=lambda x: x.descricao)
    if produtos_fabricante:
        for produto in produtos_fabricante:
            print("===== Detalhes do Produto =====")
            print(f"Descrição: {produto.descricao}")
            print(f"Peso: {produto.peso}")
            print(f"Valor de Compra: R${produto.valor_compra:.2f}")
            print(f"Valor de Venda: R${produto.valor_venda:.2f}")
            print(f"Valor do Lucro: R${produto.valor_lucro:.2f}")
            print(f"Percentual do Lucro: {produto.percentual_lucro:.2f}%")
            print(f"Fabricante: {produto.fabricante.marca}")
            print("===============================\n")
    else:
        print("Nenhum produto encontrado para o fabricante informado.")

def estados_com_maior_valor():
    maior_valor = max(produtos, key=lambda x: x.valor_venda).valor_venda
    estados_maior_valor = set()
    for produto in produtos:
        if produto.valor_venda == maior_valor:
            estados_maior_valor.add(produto.fabricante.uf)
    return estados_maior_valor

def fabricantes_com_menor_valor():
    menor_valor = min(produtos, key=lambda x: x.valor_venda).valor_venda
    fabricantes_menor_valor = []
    for produto in produtos:
        if produto.valor_venda == menor_valor:
            fabricantes_menor_valor.append((produto.fabricante, produto))
    return fabricantes_menor_valor

def listar_produtos_ordem_crescente():
    produtos_ordenados = sorted(produtos, key=lambda x: x.valor_venda)
    for produto in produtos_ordenados:
        print("===== Detalhes do Produto =====")
        print(f"Descrição: {produto.descricao}")
        print(f"Peso: {produto.peso}")
        print(f"Valor de Compra: R${produto.valor_compra:.2f}")
        print(f"Valor de Venda: R${produto.valor_venda:.2f}")
        print(f"Valor do Lucro: R${produto.valor_lucro:.2f}")
        print(f"Percentual do Lucro: {produto.percentual_lucro:.2f}%")
        print(f"Fabricante: {produto.fabricante.marca}")
        print("===============================\n")

def listar_produtos_ordem_lucro():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        produtos_ordem_lucro = sorted(produtos, key=lambda x: x.valor_lucro)
        print("===== Produtos em Ordem Crescente de Lucro =====")
        for produto in produtos_ordem_lucro:
            print(f"Descrição: {produto.descricao}")
            print(f"Lucro: R${produto.valor_lucro:.2f}")
            print("===============================")


def cadastrar_cliente():
    if len(clientes) >= MAX_CLIENTES:
        print("Limite máximo de clientes atingido. Não é possível adicionar mais clientes.")
        return

    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    cliente = Cliente(nome, idade)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def verificar_cliente_maior_60():
    for cliente in clientes:
        if cliente.idade > 60:
            return cliente, cliente.idade
    return None, None


def buscar_produto(valor):
    for produto in produtos:
        if produto.valor_venda == valor:
            return True, produto
    return False, None

def atender_clientes_fila():
    if len(clientes) == 0:
        print("Não há clientes na lista.")
        return
    
    print("Atendendo clientes (ordem de acesso baseada em fila):")
    for cliente in clientes:
        print(f"Atendendo cliente: {cliente.nome}")
    clientes.clear()
    print("Todos os clientes foram atendidos.")

def atender_clientes_pilha():
    if len(clientes) == 0:
        print("Não há clientes na lista.")
        return
    
    print("Atendendo clientes (ordem de acesso baseada em pilha):")
    while len(clientes) > 0:
        cliente = clientes.pop()
        print(f"Atendendo cliente: {cliente.nome}")
    print("Todos os clientes foram atendidos.")

def exibir_menu():
    print("\n========== MENU ==========")
    print("[1] Cadastrar fabricante")
    print("[2] Cadastrar produto")
    print("[3] Listar produtos de um fabricante")
    print("[4] Apresentar estado(s) com produtos de maior valor")
    print("[5] Apresentar fabricante(s) com produtos de menor valor")
    print("[6] Listar todos os produtos em ordem crescente de valor")
    print("[7] Listar Produtos em Ordem Crescente de Lucro")
    print("[8] Cadastrar novo cliente")
    print("[9] Verificar se existe cliente com idade superior a 60 anos")
    print("[10] Verificar se existe produto com valor especificado")
    print("[11] Atender clientes (fila)")
    print("[12] Atender clientes (pilha)")
    print("[0] Sair")

estados = [
    UF("AC", "Acre"),
    UF("AL", "Alagoas"),
    UF("AP", "Amapá"),
    UF("AM", "Amazonas"),
    UF("BA", "Bahia"),
    UF("CE", "Ceará"),
    UF("DF", "Distrito Federal"),
    UF("ES", "Espírito Santo"),
    UF("GO", "Goiás"),
    UF("MA", "Maranhão"),
    UF("MT", "Mato Grosso"),
    UF("MS", "Mato Grosso do Sul"),
    UF("MG", "Minas Gerais"),
    UF("PA", "Pará"),
    UF("PB", "Paraíba"),
    UF("PR", "Paraná"),
    UF("PE", "Pernambuco"),
    UF("PI", "Piauí"),
    UF("RJ", "Rio de Janeiro"),
    UF("RN", "Rio Grande do Norte"),
    UF("RS", "Rio Grande do Sul"),
    UF("RO", "Rondônia"),
    UF("RR", "Roraima"),
    UF("SC", "Santa Catarina"),
    UF("SP", "São Paulo"),
    UF("SE", "Sergipe"),
    UF("TO", "Tocantins")
]

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_fabricante()
    elif opcao == "2":
        cadastrar_produto()
    elif opcao == "3":
        codigo_fabricante = input("Digite o código do fabricante: ")
        listar_produtos_fabricante(int(codigo_fabricante))
    elif opcao == "4":
        estados_maior_valor = estados_com_maior_valor()
        print("Estado(s) com produtos de maior valor:")
        for estado in estados_maior_valor:
            print(f"{estado.sigla} - {estado.nome}")
            for produto in produtos:
                 if produto.fabricante.uf == estado:
                     print(f"Produto: {produto.descricao}")
                     print(f"Valor de Venda: R${produto.valor_venda:.2f}")
                     print("===============================\n")
    elif opcao == "5":
        fabricantes_menor_valor = fabricantes_com_menor_valor()
        print("Fabricante(s) com produtos de menor valor:")
        for fabricante, produto in fabricantes_menor_valor:
            print(f"Produto: {produto.descricao}")
            print(f"Valor de Venda: R${produto.valor_venda:.2f}")
            print(f"Fabricante: {fabricante.marca}")
            print(f"Site: {fabricante.site}")
            print(f"Telefone: {fabricante.telefone}")
            print(f"UF: {fabricante.uf.sigla} - {fabricante.uf.nome}")
            print("===============================\n")
    elif opcao == "6":
        listar_produtos_ordem_crescente()
    elif opcao == "7":
        listar_produtos_ordem_lucro()
    elif opcao == "8":
        cadastrar_cliente()
    elif opcao == "9":
        cliente_superior_60, idade_cliente_superior_60 = verificar_cliente_maior_60()
        if cliente_superior_60:
            print(f"Existe cliente com idade superior a 60 anos: {cliente_superior_60.nome} ({idade_cliente_superior_60} anos)")
        else:
            print("Não existem clientes com idade superior a 60 anos.")

    elif opcao == "10":
         valor_produto = float(input("Digite o valor do produto: "))
         encontrado, produto = buscar_produto(valor_produto)
         if encontrado:
             print("Produto encontrado:")
             print(f"Descrição: {produto.descricao}")
             print(f"Peso: {produto.peso}")
         else:
           print("Não existe produto com o valor especificado.")
    elif opcao == "11":
        atender_clientes_fila()
    elif opcao == "12":
        atender_clientes_pilha()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")