import HumanPlayer
import RandomComputerPlayer
import TicTacToe

if __name__ == '__main__':
    x_player = HumanPlayer.HumanPlayer('X')
    o_player = RandomComputerPlayer.RandomComputerPlayer('O')
    t = TicTacToe.TicTacToe()
    TicTacToe.play(t, x_player, o_player, print_game=True)
