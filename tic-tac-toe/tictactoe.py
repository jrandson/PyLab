
class TicTacToe:

	def __init__(self):
		self._board = [[' '] * 3 for i in range(3)]
		self._player = 'X'

	def get_current_player(self):
		return self._player

	def mark(self,i,j):
		
		is_in_border = (0 <= i <= 2) and (0 <= j <= 2)
			
			#raise ValueEror('Ivalid board position')

		position_is_free =  self._board[i][j] != ' '
			
			#raise ValueError('Position already occupied')

		game_is_over = not (self.winner() is None) or not self.border_is_full()
			
			#raise ValueError('Game is already complete')

		if not (is_in_border and position_is_free and game_is_over):

			self._board[i][j] = self._player
			if self._player == 'X':
				self._player = 'O'
			else:
				self._player = 'X'
		
		print self.__str__()

	def border_is_full(self):
		board = self._board
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					return False

		return True

	def _is_win(self,mark):

		board = self._board

		return (mark == board[0][0] == board[0][1] == board[0][2] or
				mark == board[1][0] == board[1][1] == board[1][2] or
				mark == board[2][0] == board[2][1] == board[2][2] or
				mark == board[0][0] == board[1][0] == board[2][0] or
				mark == board[1][0] == board[1][1] == board[1][2] or
				mark == board[2][0] == board[2][1] == board[2][2] or
				mark == board[0][0] == board[1][1] == board[2][2] or
				mark == board[2][0] == board[1][1] == board[0][2])

	def winner(self):
		
		for mark in 'XO':
			if self._is_win(mark):
				return mark
		return None

	def __str__(self):
		rows = [' | '.join(self._board[r]) for r in range(3)]
		return '\n---------\n'.join(rows)


game = TicTacToe()
while True:
	mark_str = raw_input("Player " + game.get_current_player() + " (x, y): ")
	mark_int = []

	for r in mark_str:
		if not r == ' ':
			mark_int.append(int(r))
			if len(mark_int) >= 2:
				break

	print game.mark(mark_int[0], mark_int[1])

	if game.winner() is not None or game.border_is_full():
		break

if not game.winner() ==  None:
	print "Winner: " + game.winner()

