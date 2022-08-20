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
        self.hypens = "-------------------------------"
        self.student1_times_won = 0
        self.student2_times_won = 0

    def decide_who_is_first(self,student1,student2):
        dice_roll = random.randint(0, 1)
        if dice_roll == 1:
            student1.is_first = True
            student2.is_first = False
        elif dice_roll == 0:
            student2.is_first = True
            student1.is_first = False

    def add(self,addition_amount):
        self.game_number = addition_amount

    def Trial_print(self):
        print(f"-------------------------------\nTrial Number {self.number_ran}:\n-------------------------------")

class Gamer:

    def __init__(self,is_first,is_turn,number,won):
        self.is_first = is_first
        self.is_turn = True
        self.number = number
        self.won = won


    def addition_amount(self):
        # change this to return 7 (or whatever number) if you want to add that specific amount
        return random.randint(1,7)


    def check_winner(student1,student2,game):
        if student2.is_turn: #if student2 had the last turn, and therefore got to 100 first, they won
            print(game.hypens + "\nStudent2 Wins!!!\n" + game.hypens)
            game.student2_times_won += 1

        elif not student2.is_turn: #if student 1 had the last turn, and therefore got to 100 first, they won.
            print(game.hypens + "\nStudent1 Wins!!!\n" + game.hypens)
            game.student1_times_won += 1


    def turn_action(student1,student2,game):

        if student1.is_turn: #if it is student1s turn
            temp_num = student1.addition_amount()
            print("student1:\n" + str(temp_num) + " + " +  str(game.game_number) +  " = " + str(game.game_number+temp_num))
            game.game_number += temp_num #this comes after the last statement because we need to check before we print, because we want to print the last value not the current one.
            if game.game_number >= 100: # the reason this is here, is to not change the turn, because the turn decides who wins, and whoevers turn it just was who added, would win, but it would change if the function
                                        # were to be allowed to continue to run.
                return None
            student1.is_turn = False
            student2.is_turn = True
        elif not student1.is_turn: #if its not student1's turn (so it should be student2's)
            temp_num = student2.addition_amount()
            print("student2:\n" + str(temp_num) + " + " + str(game.game_number) + " = " + str(game.game_number + temp_num))
            game.game_number += temp_num  # this comes after the last statement because we need to check before we print, because we want to print the last value not the current one.
            student1.is_turn = True
            student2.is_turn = False
        else:
            print(" something went wrong")




game = Experiment(0,0)
student1 = Gamer(is_first=False,is_turn=False, number=0, won=False)
student2 = Gamer(is_first=False,is_turn=False, number=0, won=False)


while game.number_ran < 10000:
    game.Trial_print()
    game.decide_who_is_first(student1,student2)
    game.game_number = 0

    if student1.is_first:
        print("student1 is first")
        student1.is_turn = True
        student2.is_turn = False
        while game.game_number <= 100:
            Gamer.turn_action(student1,student2,game)
        Gamer.check_winner(student1,student2,game)

    elif student2.is_first:
        print("Student2 is first\n"+game.hypens)
        student2.is_turn = True
        student1.is_turn = False
        while game.game_number <= 100:
            Gamer.turn_action(student1,student2,game)
        Gamer.check_winner(student1,student2,game)
    game.number_ran += 1


print("Student1 won " + str(game.student1_times_won) + " times")
print("Student2 won " + str(game.student2_times_won) + " times")




