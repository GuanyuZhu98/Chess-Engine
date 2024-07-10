import chess
import chess.polyglot

def eva(board):
    with chess.polyglot.open_reader("Human.bin") as reader:
        eva_dic = {}#create a dictionary which key is the move and value is the weight
        for entry in reader.find_all(board,minimum_weight = 0):
            eva_dic[entry.move] = entry.weight
        return(eva_dic)

def move():
    turn = 0
    board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')#initialize the board
    print(board)
 
    while board.legal_moves != 0:# the game will end if there's no legal move for one player
        print(eva(board))

        turn = turn +1
        print('{} round'.format(turn))
        #b = board.piece_map()   #where the piece is<a dictionary>
        if turn%2 != 0:
            print('white turn')
        else:
            print('black turn')
        a = board.legal_moves

        print(a)
        i = input('your current move')
        move = chess.Move.from_uci(str(board.parse_san(i)))
        board.push(move)
        print(board)
    return(turn)


def main():
    n = 1
    while n:
        turn = move()
        if turn%2 !=0:
            print('black win')
        else:
            print('white win')
        n = 0
        new = input('type 1 if you want to start a new game')
        if new == 1:
            n = 1


main()
