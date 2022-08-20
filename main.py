#imports
import random
#variables
num = 92
experiments_ran = 0


class Experiment:
    def __init__(self,number_ran,game_number):
        self.number_ran = 0
        self.game_number = game_number
        self.odd_even_number = 1

    def decide_who_is_first(self,student1,student2):
        dice_roll = random.randint(0, 1)
        print(dice_roll)
        if dice_roll == 1:
            student1.is_first = True
            student2.is_first = False
        elif dice_roll == 0:
            student2.is_first = True
            student1.is_first = False

    def add(self,addition_amount):
        self.game_number = addition_amount

class Gamer:

    def __init__(self,is_first,is_turn,addition_amount,number,won):
        self.is_first = is_first
        self.is_turn = True
        self.addition_amount = addition_amount
        self.number = number
        self.won = won

    def switch_turn(self,student1,student2):

        if student1.is_turn:
            student1.is_turn = False
            student2.is_turn = True
        elif not student1.is_turn:
            student2.is_turn = True
            student1.is_turn = False


    def check_winner(self,student1,student2,experiment):
        if student2.is_turn:
            experiment_student



class student1(Gamer):

    def __init__(self,is_first,is_turn,addition_amount,number,won):
        super().__init__(is_first,is_turn,addition_amount,number,won)


class student2(Gamer):

    def __init__(self,is_first,is_turn,addition_amount,number,won):
        super().__init__(is_first,is_turn,addition_amount,number,won)

    def something():
        print("bark")


game = Experiment(0,0)
student1 = student1(is_first=False,is_turn=False, addition_amount=random.randint(1, 7), number=0, won=False)
student2 = student2(is_first=False,is_turn=False, addition_amount=random.randint(1, 7), number=0, won=False)

while game.number_ran < 10000:
    game.decide_who_is_first(student1,student2)
    if student1.is_first:
        while game.game_number <= 100:
            game.game_number += student1.addition_amount
            print(student2.addition_amount)

            game.odd_even_number += 1
    elif student2.is_first:
        while game.game_number <= 100:
            game.game_number += student2.addition_amount
            print(student2.addition_amount)
            def check_turn():
                if student1.turn:
                    winner = student1
                    not_winner = student2
                elif not student1:
                    winner = student2
                    not_winner = student1

            #player1 number to add
            #player2 number to add
            #total number
            #repeat


    Gamer.add()
    print(student2.is_first,student1.is_first)



print(student2.is_first)



