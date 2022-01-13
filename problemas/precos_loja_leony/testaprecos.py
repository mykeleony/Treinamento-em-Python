'''
* Aplica testes unitários no algoritmo de checagem de preços do arquivo "prices.py". Executar no mesmo diretório do arquivo Python.
* Execução: pytest testaprecos.py
'''

import prices as p
import pytest

def teste_basico():
    assert p.checa_precos(['pao', 'cafe'], [0.5, 15.0], ['cafe', 'cafe'], [0.5, 15.0]) == 1
    

def teste_mesmo_item():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate'], [0.5, 15.0, 4.0, 4.0], ['cafe', 'cafe', 'cafe'], [0.5, 15.0, 0.5]) == 2


def teste_item_nao_listado():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate'], [0.5, 15.0, 4.0, 4.0], ['banana', 'cafe', 'cafe'], [0.5, 15.0, 0.5]) == 2


def teste_mais_produtos_do_que_precos():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [0.5, 15.0, 4.0, 4.0], ['banana', 'cafe', 'cafe'], [0.5, 15.0, 0.5]) == 2


def teste_lista_produtos_vazia():
    assert p.checa_precos([], [0.5, 15.0, 4.0, 4.0], ['banana', 'cafe', 'cafe'], [0.5, 15.0, 0.5]) == 3


def teste_lista_vendidos_vazia():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [0.5, 15.0, 4.0, 4.0], [], [0.5, 15.0, 0.5]) == 0


def teste_lista_precos_produtos_vazia():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [], ['pao', 'cafe', 'morango', 'abacate'], [0.5, 15.0, 0.5, 4.0]) == 4


def teste_lista_precos_produtos_vazia():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [], ['pao', 'cafe', 'morango', 'abacate'], [0.5, 15.0, 0.5, 4.0]) == 4


def teste_lista_precos_vendidos_vazia():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [0.5, 15.0, 4.0, 4.0], ['pao', 'cafe', 'morango', 'abacate'], []) == 4


def teste_lista_e_precos_vazios():
    assert p.checa_precos([], [], ['pao', 'cafe', 'morango', 'abacate'], [0.5, 15.0, 0.5, 4.0]) == 4


def teste_vendidos_e_precos_vendidos_vazios():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [0.5, 15.0, 4.0, 4.0], [], []) == 0


def teste_precos_vendidos_e_precos_vendidos_vazios():
    assert p.checa_precos(['pao', 'cafe', 'morango', 'abacate', 'rum'], [], [], []) == 0


def teste_produtos_precos_vendidos_e_vendidos_vazios():
    assert p.checa_precos([], [0.5, 15.0, 4.0, 4.0], [], []) == 0


def teste_tudo_vazio():
    assert p.checa_precos([], [], [], []) == 0
