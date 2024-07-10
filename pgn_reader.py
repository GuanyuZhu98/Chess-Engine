import chess.pgn
pgn = open(r"C:\Users\70545\Desktop\purdue\CS\chess\Morphy.pgn")#change this,My computer cannot use relative path
dummy = 1
count = 0
game = {}
#get the number of games in PGN file
#A dictionary includes all the games
#something wrong with this while loop
while dummy:
    game[count] = chess.pgn.read_game(pgn)
    count = count+1
    if game[count-1] is None:
        dummy = 0

#check the winner 

for i in range(count-1):
    move_counter = 0
    log_board = []
    board = game[i].board()
    for move in game[i].mainline_moves():
        board.push(move)
        log_board.append(board)
        move_counter = move_counter+1
    if move_counter%2!=0:
        winner = 'w'
    else:
        winner = 'b'
    for n in range(move_counter):
        print(log_board[n])
        print(winner)
