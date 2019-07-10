# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10

@author: Rubens Barbosa

* Criar variáveis para nome (str), idade (int) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
* Exibir um texto com dos os valores na tela usando F-Strings (com as chaves)

"""
ano_atual = 2019

name = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: ')) 

ano_nasci = (ano_atual - idade)

print(f'Bem vindo(a) {name}, você nasceu em {ano_nasci}. Correto?')
