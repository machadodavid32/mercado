from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []  # Vai criar uma lista de produto

carrinho: List[Dict[Produto, int]] = []
"""Será uma lista de dicionária que contém o Produto e 
um inteiro que é a quantidade de produtos"""

def main() -> None:
    menu()

def menu() -> None:
    print('=============================')
    print('======== Bem_Vindo(a) =======')
    print('======== Seu Mercado ========')
    print('=============================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)  # aguardar dois segundos, para que não saia do sistema de forma instântanea
        exit(0)  # sair do sistema
    else:
        print('Opção inválida')
        menu()



def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)  # Aqui nós vamos adicionar na lista produtos criada logo acima

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados')
    sleep(2)
    menu()


def comprar_produto() -> None:
    pass


def visualizar_carrinho() -> None:
    pass


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0  # Aqui é a somatória de valor total do carrinho

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():  # Aqui vai me dar todos os iténs de chave e valor
                print(dados[0])  # na posição 0 estará a chave, que é o Produto(), que mostra todos os dados do produto
                print(f'Quantidade: {dados[1]}')  # Aqui na chave 1 apresentará a quant de produtos
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '--main--':
    main()


