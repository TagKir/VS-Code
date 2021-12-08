board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def print_board(board):
	for i,c in enumerate(board):
		if (i+1)%3==0:
			print(f'{c}')
		else:
			print(f'{c}|', end='')

winner_comb=[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
def winner(board):
	for x, z, y in winner_comb:
		if board[x]==board[z] and board[z]==board[y] and board[x]=='X' or board[x]==board[z] and board[z]==board[y] and board[x]==board[y] and board[x]=='O':
			return ''
	return 0

def play_game():
	global board
	word='X'
	player1=input('Кто играет за крестик?\n')
	player2=input('Кто играет за нолик?\n')
	common_player=player1
	print('Приятно с вами познакомиться,а теперь приступаем к игре!')
	while winner(board)==0:
		index=int(input(f'{common_player},где ты хочешь поставить' +(' крестик' if word=='X' else ' нолик')+ '\n'))
		if board[index-1]!='X' and 'O': 
			board[index-1]=word
		else:
			print('Писать в одно и тоже место нельзя!')
			continue
		print_board(board)
		word='O' if word=='X' else 'X'
		common_player=player2 if common_player==player1 else player1
		draw=[draw for draw in board if draw==' ']
		if draw!=[]:
			continue
		else:
			print('Ничья,продолжаем играть')
			common_player=player1
			word='X'
			board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	print('Победитель:' + (player2 if common_player==player1 else player1))
play_game()
# *  Урааааааааааааааааааааааааааааааааааааааааа
# Todo     Настрой Microsoft Edge