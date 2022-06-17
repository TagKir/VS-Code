def valid(isbn):
	isn = 100
	if len(isbn) ==10:
		if isbn[-1] == 'X': isbn = isbn[:-1]
		else: isn -= 100
		isn += [isb*int(pos) for isb, pos in enumerate(isbn, start= 1)]
		return True if isn % 11 == 0 else False
	else:
		return False
print(valid('048665088X'))