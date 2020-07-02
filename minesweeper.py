import random
from IPython.display import clear_output
class Board():

    def __init__(self):

        if diff == 1:
            self.tiles = [" " for c in range(12)]
        elif diff == 2:
            self.tiles = [" " for c in range(20)]
        
    def display(self):

        if diff == 1:

            print(f"| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} |")
            print("-------------")
            print(f"| {self.tiles[3]} | {self.tiles[4]} | {self.tiles[5]} |")
            print("-------------")
            print(f"| {self.tiles[6]} | {self.tiles[7]} | {self.tiles[8]} |")
            print("-------------")
            print(f"| {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |")

        elif diff == 2:
            print(f"| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} | {self.tiles[3]} |")
            print("-----------------")
            print(f"| {self.tiles[4]} | {self.tiles[5]} | {self.tiles[6]} | {self.tiles[7]} |")
            print("-----------------")
            print(f"| {self.tiles[8]} | {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |")
            print("-----------------")
            print(f"| {self.tiles[12]} | {self.tiles[13]} | {self.tiles[14]} | {self.tiles[15]} |")
            print("-----------------")
            print(f"| {self.tiles[16]} | {self.tiles[17]} | {self.tiles[18]} | {self.tiles[19]} |")

class Mines(Board):

    def __init__(self):
        Board.__init__(self)

        if diff == 1:
            self.mines = [" " for c in range(12)]

            for num in range(3):
                self.mines[num] = "X"
            random.shuffle(self.mines)

        elif diff == 2:
            self.mines = [" " for c in range(20)]

            for num in range(5):
                self.mines[num] = "X"
            random.shuffle(self.mines)
  
    def reveal(self):

        marks = []

        for num, item in enumerate(self.mines):
            if item == "X":
                marks.append(num)

        for num in marks:
            self.tiles[num] = "X"

        if diff == 1:    

            print(f"| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} |")
            print("-------------")
            print(f"| {self.tiles[3]} | {self.tiles[4]} | {self.tiles[5]} |")
            print("-------------")
            print(f"| {self.tiles[6]} | {self.tiles[7]} | {self.tiles[8]} |")
            print("-------------")
            print(f"| {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |")

        elif diff == 2:

            print(f"| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} | {self.tiles[3]} |")
            print("-----------------")
            print(f"| {self.tiles[4]} | {self.tiles[5]} | {self.tiles[6]} | {self.tiles[7]} |")
            print("-----------------")
            print(f"| {self.tiles[8]} | {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |")
            print("-----------------")
            print(f"| {self.tiles[12]} | {self.tiles[13]} | {self.tiles[14]} | {self.tiles[15]} |")
            print("-----------------")
            print(f"| {self.tiles[16]} | {self.tiles[17]} | {self.tiles[18]} | {self.tiles[19]} |")

    def mine_pos(self):
        
        if diff == 1: 
            print(f"| {self.mines[0]} | {self.mines[1]} | {self.mines[2]} |")
            print("-------------")
            print(f"| {self.mines[3]} | {self.mines[4]} | {self.mines[5]} |")
            print("-------------")
            print(f"| {self.mines[6]} | {self.mines[7]} | {self.mines[8]} |")
            print("-------------")
            print(f"| {self.mines[9]} | {self.mines[10]} | {self.mines[11]} |")  
            
        elif diff == 2:
            print(f"| {self.mines[0]} | {self.mines[1]} | {self.mines[2]} | {self.mines[3]} |")
            print("-----------------")
            print(f"| {self.mines[4]} | {self.mines[5]} | {self.mines[6]} | {self.mines[7]} |")
            print("-----------------")
            print(f"| {self.mines[8]} | {self.mines[9]} | {self.mines[10]} | {self.mines[11]} |")
            print("-----------------")
            print(f"| {self.mines[12]} | {self.mines[13]} | {self.mines[14]} | {self.mines[15]} |")
            print("-----------------")
            print(f"| {self.mines[16]} | {self.mines[17]} | {self.mines[18]} | {self.mines[19]} |")
            
    def touch(self,pos):
    
        def the_check(self,arr,pos):
            global count
            global game_over
            global win_count
            
            count = 0
            win_count = 0
            
            for item in self.tiles:
                if item in [0,1,2,3,4,5]:
                    win_count+=1

            if self.mines[pos-1] == "X":
                game_over = True

            elif self.tiles[pos-1] in [0,1,2,3,4,5]:
                clear_output()
                print("Position taken!")

            else:
                for num in arr:
                    if self.mines[num] == "X":
                        count+=1
                self.tiles[pos-1] = count
                clear_output()
    
        # Starting at top right corner
        if diff == 1:
            if pos-1 == 0:
                the_check(self,[1,3,4],pos)

            elif pos-1 == 1:
                the_check(self,[0,2,3,4,5],pos)

            elif pos-1 == 2:
                the_check(self,[1,4,5],pos)

            elif pos-1 == 3:
                the_check(self,[0,1,4,6,7],pos)

            elif pos-1 == 4:
                the_check(self,[0,1,2,3,5,6,7,8],pos)

            elif pos-1 == 5:
                the_check(self,[1,2,4,7,8],pos)

            elif pos-1 == 6:
                the_check(self,[3,4,7,9,10],pos)

            elif pos-1 == 7:
                the_check(self,[3,4,5,6,8,9,10,11],pos)

            elif pos-1 == 8:
                the_check(self,[4,5,7,10,11],pos)

            elif pos-1 == 9:
                the_check(self,[6,7,10],pos)

            elif pos-1 == 10:
                the_check(self,[6,7,8,9,11],pos)

            elif pos-1 == 11:
                the_check(self,[7,8,10],pos)            

        elif diff == 2:
            
            if pos-1 == 0:
                the_check(self,[1,4,5],pos)

            elif pos-1 == 1:
                the_check(self,[0,2,4,5,6],pos)

            elif pos-1 == 2:
                the_check(self,[1,3,5,6,7],pos)

            elif pos-1 == 3:
                the_check(self,[2,6,7],pos)

            elif pos-1 == 4:
                the_check(self,[0,1,5,8,9],pos)

            elif pos-1 == 5:
                the_check(self,[0,1,2,4,6,8,9,10],pos)

            elif pos-1 == 6:
                the_check(self,[1,2,3,5,7,9,10,11],pos)

            elif pos-1 == 7:
                the_check(self,[2,3,6,10,11],pos)

            elif pos-1 == 8:
                the_check(self,[4,5,9,12,13],pos)

            elif pos-1 == 9:
                the_check(self,[4,5,6,8,10,12,13,14],pos)

            elif pos-1 == 10:
                the_check(self,[5,6,7,9,11,13,14,15],pos)

            elif pos-1 == 11:
                the_check(self,[6,7,10,14,15],pos)
                
            elif pos-1 == 12:
                the_check(self,[8,9,13,16,17],pos)  
                
            elif pos-1 == 13:
                the_check(self,[8,9,10,12,14,16,17,18],pos)

            elif pos-1 == 14:
                the_check(self,[9,10,11,13,15,17,18,19],pos) 
                
            elif pos-1 == 15:
                the_check(self,[10,11,14,18,19],pos) 
                
            elif pos-1 == 16:
                the_check(self,[12,13,17],pos) 
                
            elif pos-1 == 17:
                the_check(self,[12,13,14,16,18],pos) 
                
            elif pos-1 == 18:
                the_check(self,[13,14,15,17,19],pos) 
                
            elif pos-1 == 19:
                the_check(self,[14,15,18],pos)
                
def replay():
    global mine_board
    global game_over
    global playing
    
    while True:
        try:
            rep = input("Would you like to play again?: ")
            
            if rep.lower()[0] not in ("y","n"):
                clear_output()
                print("Please enter in yes or no!")
                continue
                
        except:
            clear_output()
            print("Please enter in yes or no!")
            
        else:            
            if rep.lower()[0] == "y":
                clear_output()
                playing = True
                game_over = False
                game_difficulty()
                mine_board = Mines()
                break
            else:
                print("Thanks for playing!")
                playing = False
                break

def game_difficulty():
    global diff
    while True:
        try:
            print("{0}              {1}".format("1) 3 x 4","2) 4 x 5"))
            diff = int(input("What size grid would you like to play?: "))
        except:
            clear_output()
            print("Please enter in 1 or 2!")
        else:
            if diff not in (1,2):
                clear_output()
                print("Please enter in 1 or 2!")
            else:
                clear_output()
                if diff == 1:
                    print("You have selected grid size 3 x 4!\nThere are 3 mines!")
                    break
                    
                if diff == 2:
                    print("You have selected grid size 4 x 5!\nThere are 5 mines!")
                    break                    

ask = True
playing = True
game_over = False
diff =""


print("Welcome to Minesweeper!")

game_difficulty()
mine_board = Mines()

while playing:
    
    mine_board.display()
    
    while ask:
        try:
            pos = int(input("What position would you like to choose?: "))
        except:
            clear_output()
            print("Please choose a number!")
            mine_board.display()
        else:
            break
            
    mine_board.touch(pos)

    if game_over:
        clear_output()
        print("GAME OVER\n")
        mine_board.reveal()
        replay()
    
    elif diff == 1 and win_count == 8:
        print("GAME WIN!")
        mine_board.reveal()
        replay()
        
    elif diff == 2 and win_count == 14:
        print("GAME WIN!")
        mine_board.reveal()
        replay()