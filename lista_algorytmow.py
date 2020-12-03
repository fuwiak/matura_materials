def decimalToBinary(num):
    num_=""
    if num > 1:
        decimalToBinary(num // 2)
        num_+=str(num % 2)
    
    return num_



def is_prime(n):
	if n<2:
		return False
	else:
		N = n//2 +1 
		for x in range(2, N):
			if n%x==0:
				return False


		return True
	
def perfect(num):
	dzieln = []
	for x in range(1, num):
		if num % x == 0:
			dzieln.append(x)
	if sum(dzieln) == num:
		return True
	return False
