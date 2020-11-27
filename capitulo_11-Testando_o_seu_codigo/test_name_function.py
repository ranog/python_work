#! /usr/bin/env python3

"""
NOME
    test_name_function.py - Um teste que passa.

SINOPSES
    $ chmod +x test_name_function.py
    $ ./test_name_function.py
    .
    --------------------------------------------------------------------
    --
    Ran 1 test in 0.001s

    OK
    --------------------------------------------------------------------
    ----

DESCRIÇÃO
    - Um teste que passa:
         Inicialmente importamos unittest e a função
         get_formatted_name() que queremos testar. Criamos uma classe
         chamada NamesTestCase, que conterá uma série de testes de
         unidade para get_formatted_name(). Você pode dar o nome que
         quiser para a classe, mas é melhor nomeá-la com palavras
         relacionadas à função que você está prestes a testar e usar a
         palavra Test no nome da classe. Essa classe deve herdar da
         classe unittest.TestCase para que Python saiba executar os
         testes que você escrever.
        
        NamesTestCase contém um único método que testa um aspecto de
        get_formatted_name(). Chamamos esse método de 
        test_first_last_name() porque estamos verificando se os nomes
        que têm apenas o primeiro nome e o sobrenome são formatados
        corretamente. Qualquer método que comece com test_ será
        executado de modo automático quando test_name_function.py for
        executado. Nesse método de teste, chamamos a função que queremos
        testar e armazenamos um valor de retorno que estamos
        interessados em testar. Nesse exemplo, chamamos
        get_formatted_name() com os argumentos 'janis' e 'joplin' e
        armazenamos o resultado em formatted_name. Usamos um dos
        recursos mais úteis de unittest: um método de asserção.

        Os métodos de asserção verificam se um resultado recebido é
        igual ao resultado que você esperava receber. Nesse caso, como
        sabemos que get_formatted_name() deve devolver um nome completo,
        com as letras iniciais maiúsculas e os espaços apropriados,
        esperamos que o valor em formatted_name seja Janis Joplin. Para
        conferir se isso é verdade, usamos o método assertEqual() de
        unittest e lhe passamos formatted_name e 'Janis Joplin'. A linha
        self.assertEqual(formatted_name, 'Janis Joplin') diz o seguinte:
        “Compare o valor em formatted_name com a string 'Janis Joplin'.
        Se forem iguais conforme esperado, tudo bem.
        Contudo, se não forem iguais, me avise!”.

        A linha unittest.main() diz a Python para executar os testes
        desse arquivo.

        O ponto na primeira linha da saída nos informa que um único
        teste passou. A próxima linha diz que Python executou um teste e
        demorou menos de 0,001 segundo para fazê-lo. O OK no final
        informa que todos os testes de unidade do caso de teste
        passaram.
        Essa saída mostra que a função get_formatted_name() sempre
        funcionará para nomes que tenham o primeiro nome e o sobrenome,
        a menos que a função seja modificada. Se modificarmos
        get_formatted_name(), poderemos executar esse teste novamente.
        Se o caso de teste passar, saberemos que a função continua
        funcionando para nomes como Janis Joplin.

------------------------------------------------------------------------

HISTÓRICO
    20202711: João Paulo, novembro de 2020.
        - Um teste que passa (pg 258-259).

"""


import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""
    
    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        
        formatted_name = get_formatted_name('janis', 'joplin')

        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
