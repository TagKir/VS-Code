board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def print_board():
	for i,c in enumerate(board):
		if (i+1)%3==0:
			print(f'{c}')
		else:
			print(f'{c}|', end='')
print_board()
winner_comb=[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
def winner():