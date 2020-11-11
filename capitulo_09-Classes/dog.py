#! /usr/bin/env python3

"""
NOME
    dog.py - Criando a classe Dog.

SINOPSES
    chmod +x dog.py
    ./dog.py

    My dog's name is Willie.
    My dog is 6 years old.

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

    - Criando uma instância a partir de uma classe:

    Dizemos a Python para criar um cachorro de nome 'willie' e idade
    igual a 6. Quando Python lê essa linha, ele chama o método
    __init__() de Dog com os argumentos 'willie' e 6. O método
    __init__() cria uma instância que representa esse cachorro em
    particular e define os atributos name e age com os valores que
    fornecemos.
    Esse método não tem uma instrução return explícita, mas Python
    devolve automaticamente uma instância que representa esse cachorro.
    Armazenamos essa instância na variável my_dog. A convenção de
    nomenclatura é útil nesse caso: em geral, podemos supor que um nome
    com a primeira letra maiúscula como Dog refere-se a uma classe,
    enquanto um nome com letras minúsculas como my_dog refere-se a uma
    única instância criada a partir de uma classe.
   
    - Acessando atributos:

    Para acessar os atributos de uma instância utilize a notação de
    ponto.
    Acessamos o valor do atributo name de my_dog escrevendo:
    
    my_dog.name

    A notação de ponto é usada com frequência em Python. Essa sintaxe
    mostra como Python encontra o valor de um atributo. Nesse caso, o
    interpretador olha para a instância my_dog e encontra o atributo 
    name associado a ela. É o mesmo atributo referenciado como self.name
    na classe Dog. Usamos a mesma abordagem para trabalhar com o
    atributo age. Em nossa primeira instrução print, my_dog.name.title()
    faz com que 'willie' – o valor do atributo name de my_dog – comece
    com uma letra maiúscula. Na segunda instrução print, str(my_dog.age)
    converte 6 – o valor do atributo age de my_dog – em uma string.
    A saída é um resumo do que sabemos sobre my_dog.

HISTÓRICO
    20201011: João Paulo, novembro de 2020.
        - Criando a classe Dog (pg 200-202).

    20201111: João Paulo, novembro de 2020.
        - Criando uma instância a partir de uma classe (pg 202-203).
        - Acessando atributos (pg 203).

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


my_dog = Dog('willie', 6)

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.\n")
