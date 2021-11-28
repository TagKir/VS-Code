class Game():
	board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	def print_board(self,state):
		for i,a in enumerate(state):
			if (i+1)%3==0:
				print(f'{a}')
			else:
				print(f'{a}|',end="")
	def winner(self,state):
		win_comb=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
		for z,x,c in win_comb:
			if state[z]==state[x] and state[x]==state[c] and (state[z]=='X' or state[z]=='O'):
				return True
			else:
				return ''
	def play_game(self):
		player1=1
		player2=0
		while Game.winner(self,Game.board)=='':
			player1+=1
			player2+=1
			if player1%2==0:
				print('player1 делает ход')
				mesto=int(input('Where'))-1
				Game.board[mesto]='X'
				Game.print_board(self,Game.board)
			else:
				print('player2 делает ход')
				mesto=int(input('Where'))
g=Game()
g.play_game()