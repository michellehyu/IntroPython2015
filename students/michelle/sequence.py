sequence = "123456789" 
'''
return a string with the first and last characters exchanged.
'''
def exchange_first_last (sequence):
	return sequence[-1] + sequence[:-1]

print (exchange_first_last(sequence))

'''
return a string with every other character removed
'''
def remove_every_other(sequence):
	return sequence[::2]

print (remove_every_other(sequence))

'''
return a string with the first and last 4 characters removed, and every other char in between
'''
def first_last_four(sequence):
	return remove_every_other(sequence[1:-4])

print (first_last_four(sequence))
'''
return a string reversed (just with slicing)
'''
def slice_reverse(sequence):
	return sequence[::-1]

print (slice_reverse(sequence))

'''
return a string with the middle third, then last third, then first third in the new order
'''
def  reorder(sequence):
	m = len(sequence)//2
	return sequence[m-1:m+1]+sequence[-4:]+sequence[0:3]
print (reorder(sequence))

