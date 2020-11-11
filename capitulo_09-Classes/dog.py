#! /usr/bin/env python3

"""
NOME
    dog.py - Criando a classe Dog.

SINOPSES


DESCRIÇÃO
    Definimos uma classe chamada Dog. Por convenção, nomes com a
    primeira letra maiúscula referem-se a classes em Python. Os
    parênteses na definição da classe estão vazios porque estamos
    criando essa classe do zero.
    Escrevemos uma docstring que descreve o que essa classe faz.

    Cada instância criada a partir da classe Dog armazenará um nome
    (name) e uma idade (age), e daremos a cada cachorro a capacidade de
    sentar (sit()) e rolar (roll_over()).

    - Método __init__()

    Uma função que faz parte de uma classe é um método. Tudo que
    aprendemos sobre funções também se aplica aos métodos.
    
    O método __init__() é um método especial que Python executa
    automaticamente sempre que criamos uma nova instância baseada na
    classe Dog. Esse método tem dois underscores no início e dois no
    final – uma convenção que ajuda a evitar que os nomes default de
    métodos Python entrem em conflito com nomes de métodos criados por
    você.

    Definimos o método __init__() para que tenha três parâmetros: self,
    name e age. O parâmetro self é obrigatório na definição do método e
    deve estar antes dos demais parâmetros. Deve estar incluído na
    definição, pois, quando Python chama esse método __init__() depois
    (para criar uma instância de Dog), a chamada do método passará o
    argumento self automaticamente. Toda chamada de método associada a
    uma classe passa self, que é uma referência à própria instância, de
    modo automático; ele dá acesso aos atributos e métodos da classe à
    instância individual. Quando criamos uma instância de Dog, Python
    chamará o método __init__() da classe Dog. Passaremos um nome e uma
    idade como argumentos para Dog(); self é passado automaticamente,
    portanto não é preciso especificá-lo. Sempre que quisermos criar uma
    instância da classe Dog forneceremos valores apenas para os dois
    últimos parâmetros, que são name e age.
    
    As duas variáveis definidas têm o prefixo self. Qualquer variável
    prefixada com self está disponível a todos os métodos da classe;
    além disso, podemos acessar essas variáveis por meio de qualquer
    instância criada a partir da classe. self.name = name usa o valor
    armazenado no parâmetro name e o armazena na variável name, que é
    então associada à instância criada. O mesmo processo ocorre com
    self.age = age. Variáveis como essas, acessíveis por meio de
    instâncias, são chamadas de atributos.

    A classe Dog tem dois outros métodos definidos: sit() e roll_over().
    Como esses métodos não precisam de informações adicionais como um
    nome ou uma idade, simplesmente os definimos com um parâmetro self.
    As instâncias que criarmos posteriormente terão acesso a esses
    métodos. Em outras palavras, elas terão a capacidade de sentar e
    rolar.
    
    Por enquanto, sit() e roll_over() não fazem muito. Apenas exibem uma
    mensagem dizendo que o cachorro está sentando ou rolando. No
    entanto, o conceito pode ser estendido para situações realistas: se
    essa classe fizesse parte de um jogo de computador de verdade, esses
    métodos conteriam código para fazer a animação de um cachorro
    sentando e rolando. Se essa classe tivesse sido escrita para
    controlar um robô, esses métodos direcionariam os movimentos para
    fazer um cachorro-robô sentar e rolar.

HISTÓRICO
    20201011: João Paulo, novembro de 2020.
        - Criando a classe Dog (pg 200-202).

    20201111: João Paulo, novembro de 2020.
        - Anotações.
"""


class Dog():
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age


    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!")
