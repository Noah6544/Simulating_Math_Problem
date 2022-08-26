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


    def addition_amount(self,game):
        # change this to return 7 (or whatever number) if you want to add that specific amount
        if game.game_number >= 93:
            return 100-game.game_number

        else:
            return random.randint(1,7)

    def addition_amount_student1_strategic(self,game):
        #this is based on the game strategy I found, which is 92 (the easiest number to find that is the right answer) - 8.

        if game.game_number == 0: #if the game just started:
            return 4
        elif game.game_number > 4 and game.game_number < 12: #it is the winning number
            return 12 - game.game_number
        elif game.game_number > 12 and game.game_number < 20: #it is the winning number
            return 20 - game.game_number
        elif game.game_number > 20 and game.game_number < 28: #it is the winning number
            return 28 - game.game_number
        elif game.game_number > 28 and game.game_number < 36: #it is the winning number
            return 36 - game.game_number
        elif game.game_number > 36 and game.game_number < 44: #it is the winning number
            return 44 - game.game_number
        elif game.game_number > 44 and game.game_number < 52:#it is the winning number
            return 52 - game.game_number
        elif game.game_number > 52 and game.game_number < 60: #it is the winning number
            return 60 - game.game_number
        elif game.game_number > 60 and game.game_number < 68: #it is the winning number
            return 68 - game.game_number
        elif game.game_number > 68 and game.game_number < 76: #it is the winning number
            return 76 - game.game_number
        elif game.game_number > 76 and game.game_number < 84: #it is the winning number
            return 84 - game.game_number
        elif game.game_number > 84 and game.game_number < 92: #it is the winning number
            return 92 - game.game_number
        elif game.game_number >= 93:
            return 100-game.game_number
        else:
            return random.randint(1, 7)
            print("gone wrong wrong")


    def check_winner(student1,student2,game):
        if student2.is_turn: #if student2 had the last turn, and therefore got to 100 first, they won
            print(game.hypens + "\nStudent2 Wins!!!\n" + game.hypens)
            game.student2_times_won += 1

        elif not student2.is_turn: #if student 1 had the last turn, and therefore got to 100 first, they won.
            print(game.hypens + "\nStudent1 Wins!!!\n" + game.hypens)
            game.student1_times_won += 1


    def turn_action(student1,student2,game):
        if student1.is_turn: #if it is student1s turn
            temp_num = student1.addition_amount_student1_strategic(game)
            print("student1:\n" + str(temp_num) + " + " + str(game.game_number) +  " = " + str(game.game_number+temp_num))
            game.game_number += temp_num #this comes after the last statement because we need to check before we print, because we want to print the last value not the current one.
            if game.game_number >= 100: # the reason this is here, is to not change the turn, because the turn decides who wins, and whoevers turn it just was who added, would win, but it would change if the function
                                        # were to be allowed to continue to run.
                return None
            student1.is_turn = False
            student2.is_turn = True
        elif not student1.is_turn: #if its not student1's turn (so it should be student2's)
            temp_num = student2.addition_amount(game)
            print("student2:\n" + str(temp_num) + " + " + str(game.game_number) + " = " + str(game.game_number + temp_num))
            game.game_number += temp_num  # this comes after the last statement because we need to check before we print, because we want to print the last value not the current one.
            student1.is_turn = True
            student2.is_turn = False
        else:
            print(" something went wrong")





while True:
    game = Experiment(0, 0)

    student1 = Gamer(is_first=False, is_turn=False, number=0, won=False)
    student2 = Gamer(is_first=False, is_turn=False, number=0, won=False)
    try:
        print("\n" + game.hypens + "\n")
        is_simulation = input("Run a simulation (type '1')\nplay against CPU (type '2')")
        if int(is_simulation) == 1:

            while game.number_ran < 10000: #total trials/simulations to be run
                game.Trial_print()
                #game.decide_who_is_first(student1,student2) doesn't make sense to use, student1 is always first, cuz student 1 is student 1....
                game.game_number = 0
                student1.is_first, student2.is_first = True, False
                if student1.is_first:
                    print("student1 is first")
                    student1.is_turn = True
                    student2.is_turn = False
                    while game.game_number < 100:
                        Gamer.turn_action(student1,student2,game)

                    Gamer.check_winner(student1,student2,game)

                elif student2.is_first:
                    print("Student2 is first\n"+game.hypens)
                    student2.is_turn = True
                    student1.is_turn = False
                    while game.game_number < 100:
                        Gamer.turn_action(student1,student2,game)

                    Gamer.check_winner(student1,student2,game)
                game.number_ran += 1


            print("Student1 won " + str(game.student1_times_won) + " times")
            print("Student2 won " + str(game.student2_times_won) + " times")

        elif int(is_simulation) == 2:
            addition_num_bool = False
            print(game.hypens)
            choose_player = input("Play as Player 1 (type '1')\nPlay as Player 2 (type '2')?\n(Warning: P1 is pretty good....)\nEnter your player: ")
            print(game.hypens)

            if int(choose_player) == 1:
                while game.game_number <= 100:

                    while addition_num_bool == False:
                        addition_num = int(input("Enter number to add (1-7)"))
                        if addition_num >= 1 and addition_num <= 7:                 #this while loop just checks if the number
                            addition_num_bool = True                                #is really 1- 7 or not, keeping my strategy good.

                        else:
                            print(game.hypens)
                            print("INVALID NUMBER RANGE, try again.")
                            print(game.hypens)

                    print("You:\n" + str(addition_num) + " + " + str(game.game_number) + " = " + str(game.game_number + addition_num))
                    game.game_number += addition_num
                    temp_num = Gamer.addition_amount(game)
                    print("student2:\n" + str(game.game_number) + " + " + str(temp_num) +  " = " + str(game.game_number+temp_num))
                    game.game_number += temp_num

            elif int(choose_player) == 2:
                while game.game_number <= 100:
                    temp_num = student1.addition_amount_student1_strategic(game)
                    print("student1:\n" + str(game.game_number) + " + " + str(temp_num) + " = " + str(game.game_number + temp_num))
                    game.game_number += temp_num

                    while addition_num_bool == False:
                        addition_num = int(input("Enter number to add (1-7)"))
                        if addition_num >= 1 and addition_num <= 7:
                            addition_num_bool = True
                        else:
                            print(game.hypens)
                            print("INVALID NUMBER RANGE, try again.")
                            print(game.hypens)

                    print("You:\n" + str(addition_num) + " + " + str(game.game_number) + " = " + str(game.game_number + addition_num))
                    game.game_number += addition_num
                    addition_num_bool = False

    except:
        print("\n" +game.hypens+ "\n" "INVALID INPUT\nYou probably pressed a letter...\nRestarting Script...\n" + game.hypens + "\n")