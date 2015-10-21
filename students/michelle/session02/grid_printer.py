#print("let's see if this works")
def print_grid(n):
	gaps = (n-3)//2
	minuses = "- " * gaps
	border = '+ ' + minuses + '+ ' + minuses + '+' + '\n'
	spaces = '  '* gaps
	middle = '| ' + spaces + '| ' + spaces + '| ' + '\n'
	grid = border + middle * gaps + border + middle * gaps + border
	print (grid)

def print_grid(cols, rows):
	adj_col = (cols-3)//2
	adj_row = (rows-3)//2  
	minuses = "- " * adj_col
	border = '+ ' + minuses + '+ ' + minuses + '+' + '\n'
	spaces = '  '* adj_col
	middle = '| ' + spaces + '| ' + spaces + '| ' + '\n'
	grid = border + middle * adj_row + border + middle * adj_row + border
	print (grid)

print_grid(10,50)