#print("let's see if this works")
def print_grid(n):
	gaps = (n-3)//2
	minuses = "- " * gaps
	border = '+ ' + minuses + '+ ' + minuses + '+' + '\n'
	spaces = '  '* gaps
	middle = '| ' + spaces + '| ' + spaces + '| ' + '\n'
	grid = border + middle * gaps + border + middle * gaps + border
	print (grid)

print_grid(12)