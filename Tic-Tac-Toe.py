
import json
import random

def draw_board(board):
    # display the tic-tac-toe game board
    print('-----------')
    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]+'|')
    print('-----------')
    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2]+'|')
    print('-----------')
    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2]+'|')
    print('-----------')


def welcome(board):
    print('Welcome to the "Unbeatable Noughts and crosses" game.\nThe board layout is shown below: ')
    #draw function is called to display game board
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')


def initialise_board(board):
    # initialize the elements of the board to empty spaces, where i represents row and j irepresents column
    for i in range(3):  
        for j in range(3):
            board[i][j] = ' '


#get a move from the player and return the corresponding row and column indices of the board.
def get_player_move(board):
    while True:
        player_move = input(
            " 1 2 3 \n 4 5 6 \n 7 8 9 \n choose your square:")

        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_move = int(player_move)-1
            if board[int(player_move/3)][player_move % 3] == ' ':
                return int(player_move/3), player_move % 3
            else:
                print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


# choose a move for the computer player and return the corresponding row and column indices of the board.
def choose_computer_move(board):
  '''valid = False: Initialize a  variable to keep track of whether a valid move has been found yet.'''
  valid = False
  while not valid:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if board[row][col] == ' ':
      valid = True
  return (row, col)


#check if there is a winning combination on the board based on the player's mark.
def check_for_win(board, mark):
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False


#checking if the tic-tac-toe board is in a draw state
def check_for_draw(board):
    #returns true if ' ' isnot found while iterating over all cells in the 3*3 board
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    # board  is initialized now board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    initialise_board(board)
    while True:
        player_move = get_player_move(board)
        if player_move != None:
            board[player_move[0]][player_move[1]] = "X"
            draw_board(board)
            if check_for_win(board, "X"):
                return 1
            elif check_for_draw(board):
                return 0
            computer_move = choose_computer_move(board)
            board[computer_move[0]][computer_move[1]] = "O"
            print("Computer made a choice")
            draw_board(board)

            if check_for_win(board, "O"):
                return -1
            elif check_for_draw(board):
                return 0
            else:
                continue

def menu():
    # Loop run continuously until user input valid data (1,2,3,q);
    while True:
        # user input is stored in choice.
        choice = input(
            "1. Play game\n2. Save score\n3. Leaderboard \nq. Quit\nEnter your choice: ")
        # check if choice is a valid data which is (1 to play game, 2, 3, q);
        if choice in ['1', '2', '3', 'q']:
            # if choice is valid it is returned.
            return choice
        else:
            # if choice is not valid loop run continuously.
            print("Invalid input. Please enter a valid choice.")

def load_scores():
    """Loads the leaderboard from a .txt file and returns it as a dictionary"""
    try:
        # open the file in read mode
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    except:
        # if the file doesn't exist, create a new dictionary
        leaderboard = {}

    return leaderboard


def save_score(score):
    # Saves the name in leaderboard
    player_name = input("Enter your name: ")
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except:
        data = {}
        
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)


def display_leaderboard(leaders):
    print("Name: Score")
    for name, score in leaders.items():
        print(f"{name}: {score}")


def main():
    # Two Dimension array
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    # Calls Welcome function with argument board.
    welcome(board)
    total_score = 0
    # While is an infinite loop which run continuously until the user press q.
    while True:
         
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:', total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


if __name__ == '__main__':
    main()
