import tkinter as tk
from tkinter import messagebox

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

if __name__ == "__main__":
    game = TicTacToe()

    class TicTacToeGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Tic Tac Toe")
            self.game = TicTacToe()
            self.buttons = []
            self.enable_key_bindings()
            
            self.label = tk.Label(root, text=f"Turno: {self.game.current_player}", font=("Arial", 14))
            self.label.grid(row=0, column=0, columnspan=3, pady=10)
            
            for i in range(9):
                btn = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                               command=lambda pos=i: self.on_button_click(pos))
                btn.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
                self.buttons.append(btn)
            
            self.reset_btn = tk.Button(root, text="Reiniciar", command=self.reset_game)
            self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)
        
        def on_button_click(self, position):
            if self.game.make_move(position):
                self.buttons[position].config(text=self.game.current_player)
                
                if self.game.is_winner(self.game.current_player):
                    messagebox.showinfo("Ganador", f"¡Jugador {self.game.current_player} gana!")
                    self.reset_game()
                    return
                
                if self.game.is_board_full():
                    messagebox.showinfo("Empate", "¡Empate!")
                    self.reset_game()
                    return
                
                self.game.switch_player()
                self.label.config(text=f"Turno: {self.game.current_player}")
            else:
                messagebox.showwarning("Inválido", "Movimiento inválido")
        def on_key_press(self, event):
            """
            Detecta pulsaciones del teclado numérico (numpad) y de los dígitos principales
            y las convierte en movimientos del tablero.
            Mapeo (numpad estilo):
              7 8 9    ->  0 1 2
              4 5 6    ->  3 4 5
              1 2 3    ->  6 7 8
            """
            key = event.keysym
            mapping = {
                'KP_7': 6, 'KP_8': 7, 'KP_9': 8,
                'KP_4': 3, 'KP_5': 4, 'KP_6': 5,
                'KP_1': 0, 'KP_2': 1, 'KP_3': 2,
                '7': 0, '8': 1, '9': 2,
                '4': 3, '5': 4, '6': 5,
                '1': 6, '2': 7, '3': 8,
            }

            pos = mapping.get(key)
            if pos is None:
                return  # tecla no manejada

            # Simular pulsación de botón en la posición correspondiente
            self.on_button_click(pos)
        def enable_key_bindings(self):
            """Registrar el handler de teclado. Llamar desde __init__: self.enable_key_bindings()"""
            self.root.bind_all("<Key>", self.on_key_press)
        def reset_game(self):
            self.game = TicTacToe()
            for btn in self.buttons:
                btn.config(text=" ")
            self.label.config(text=f"Turno: {self.game.current_player}")

    if __name__ == "__main__":
        root = tk.Tk()
        gui = TicTacToeGUI(root)
        root.mainloop()