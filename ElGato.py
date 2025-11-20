class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        print('\n')
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("-----------")
        print('\n')
    
    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def make_move(self, position):
        if 0 <= position <= 8 and self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        print("¡Bienvenido al Gato!")
        while True:
            self.print_board()
            print(f"Turno del jugador {self.current_player}")
            
            try:
                position = int(input("Ingresa posición (0-8): "))
                if not self.make_move(position):
                    print("Movimiento inválido")
                    continue
            except ValueError:
                print("Entrada inválida")
                continue
            
            if self.is_winner(self.current_player):
                self.print_board()
                print(f"¡Jugador {self.current_player} gana!")
                break
            
            if self.is_board_full():
                self.print_board()
                print("¡Empate!")
                break
            
            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()