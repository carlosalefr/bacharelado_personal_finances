#coding: utf-8

import unittest
from should_dsl import should
from pessoa import Pessoa
from gasto import Gasto

class TestPessoa(unittest.TestCase):

    def teste_criar_pessoa(self):
        pessoa = Pessoa("Maria", 1000, 10)
        pessoa.nome |should| equal_to("Maria")
        pessoa.salario |should| equal_to(1000)
        pessoa.dia_pagamento |should| equal_to(10)
        
         
        
if __name__=="__main__":
    unittest.main()
