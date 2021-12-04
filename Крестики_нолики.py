import random
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
		pl1=(input('Как зовут первого игрока?\n')).capitalize()
		player1num=0
		player2num=0
		pl2=(input('Как зовут второго игрока?\n')).capitalize()
		player1=random.choice([pl2, pl1])
		quest1=True
		board2=False
		while Game.winner(self,Game.board)=='':
			player1num+=1
			player2num+=1
			if board2==False:
				if quest1==True:
					if player1==pl1:
						player2=pl2
						print(f'{player1} ходит первым')
						player1num+=1
					elif player1==pl2:
						player2=pl2
						print(f'{player2} ходит первым')
						player2num+=1
					quest1=0
				else:
					if player1num%2==0:
						print(f'{pl1} делает ход')
					else:
						print(f'{pl2} делает ход')
			if player1num%2==0:
				mesto=int(input('Где ты хочешь поставить крестик?\n'))-1
				if Game.board[mesto]==' ' :
					Game.board[mesto]='X'
					Game.print_board(self,Game.board)
					board2=False
				else:
					print('Эта клетка уже занята')
					player1num-=1
					player2num-=1
					board2=True
			else:
				mesto=int(input('Где ты хочешь поставить нолик?\n'))-1
				if Game.board[mesto]==' ' :
					Game.board[mesto]='O'
					Game.print_board(self,Game.board)
					board2=False
				else:
					print('Эта клетка уже занята')
					player1num-=1
					player2num-=1
					board2=True

		if player1%2==0:
			return 'Player1 win'
		else:
			return 'Player2 win'
g=Game()
g.play_game()
# 