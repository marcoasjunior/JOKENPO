import random


def first():
    while True:
        first = input("""Quem será o P1?
        Player = só joga pedra :)
        Randomplayer = joga aleatoriamente
        HumanPlayer = um jogador humano
        ReflectPlayer = um imitador
        CyclePlayer = joga todas as opções seguidas
        """)
        if first == "Player":
            return Player()

        elif first == "Randomplayer":
            return RandomPlayer()

        elif first == "HumanPlayer":
            return HumanPlayer()

        elif first == "ReflectPlayer":
            return ReflectPlayer()

        elif first == "CyclePlayer":
            return CyclePlayer()

        print("Digite o nome do jogador.")


def second():
    while True:
        second = input("""Quem será o P2?
        Player = só joga pedra :)
        Randomplayer = joga aleatoriamente
        HumanPlayer = um jogador humano
        ReflectPlayer = um imitador
        CyclePlayer = joga todas as opções seguidas
        """)
        if second == "Player":
            return Player()

        elif second == "Randomplayer":
            return RandomPlayer()

        elif second == "HumanPlayer":
            return HumanPlayer()

        elif second == "ReflectPlayer":
            return ReflectPlayer()

        elif second == "CyclePlayer":
            return CyclePlayer()

        print("Digite o nome do jogador.")


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    moves = ['rock', 'paper', 'scissors']


class RandomPlayer(Player):
    def move(self):
        return random.choice(Player.moves)


class HumanPlayer(Player):
    def move(self):
        jogada = input("Rock, paper or scissors?:").lower()
        while jogada not in Player.moves:
            print("Essa não é uma jogada válida.")
            jogada = input("Rock, paper or scissors?:").lower()
        else:
            return jogada


class ReflectPlayer(Player):
    def __init__(self):
        self.last_play = None

    def move(self):
        if not self.last_play:
            return random.choice(Player.moves)
        return self.last_play

    def learn(self, my_move, their_move):
        self.last_play = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.lista = []

    def move(self):
        jogada = random.choice(Player.moves)
        while jogada not in self.lista:
            self.lista.append(jogada)
            return jogada
        condition = set(Player.moves).difference(set(self.lista))
        if condition:
            return random.choice(list(condition))
        self.lista = []
        jogada = random.choice(Player.moves)
        self.lista.append(jogada)
        return jogada


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.vitoria1 = 0
        self.vitoria2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.beats(move1, move2)

    def beats(self, move1, move2):
        one = move1
        two = move2

        if ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')):
            self.vitoria1 += 1
            print(f"P1 ganhou!")
            print(f"O jogo está {self.vitoria1} x {self.vitoria2}")

        elif ((two == 'rock' and one == 'scissors') or
              (two == 'scissors' and one == 'paper') or
              (two == 'paper' and one == 'rock')):
            self.vitoria2 += 1
            print(f"P2 ganhou!")
            print(f"O jogo está {self.vitoria1} x {self.vitoria2}")

        else:
            print("Empate!")
            print(f"O jogo está {self.vitoria1} x {self.vitoria2}")

    def number_plays(self):
        while True:
            try:
                plays = int(input("Quantas rodadas terá o jogo?"))

            except ValueError:
                print("Isso é um número? Acho que não. Tente novamente.")
            else:
                return plays

    def winner(self, vit1, vit2):
        if vit1 == vit2:
            print("O jogo terminou empatado!")
        elif vit1 > vit2:
            print("P1 foi o vitorioso!")
        else:
            print("P2 é o vencedor!")

    def continuar(self):
        while True:
            option = input("Deseja continuar jogando? Sim ou não?").lower()
            if option == "sim":
                return self.play_game()

            elif option == "não":
                print("Obrigado por jogar!")
                quit()

            print("Para continuar digite sim, para sair digite não.")

    def play_game(self):
        print("Game start!")
        for round in range(self.number_plays()):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"O P1 ganhou {self.vitoria1} e o P2 ganhou {self.vitoria2}")
        self.winner(self.vitoria1, self.vitoria2)
        self.continuar()


if __name__ == '__main__':
    x1 = first()
    x2 = second()
    game = Game(x1, x2)
    game.play_game()
