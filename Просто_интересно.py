def valid_ISBN10(isbn): 
	ISBN = 100
	if len(isbn)==10:
		if isbn[-1]=='X': isbn = isbn[:-1]
		else: ISBN-=100
		ISBN += [isb*int(pos) for isb,pos in enumerate(isbn, start= 1)]
		return True if ISBN % 11 == 0 else False
	else:
		return False
print(valid_ISBN10('048665088X'))