import random

def is_present_inbox(grid, row, col, num):
	for i in range(3):
		for j in range(3):
			if grid[row + i][col + j] == num:
				return False
	return True

def is_present_inrow(grid,row,num):
	for j in range(9):
		if grid[row][j]==num:
			return False
	return True

def is_present_incol(grid,col,num):
	for i in range(9):
		if grid[i][col]==num:
			return False
	return True
def is_Safe(grid, row, col, num):
    br = row - row % 3
    bc = col - col % 3
    return (
        is_present_inrow(grid, row, num) and
        is_present_incol(grid, col, num) and
        is_present_inbox(grid, br, bc, num)
    )

def fill_grid(grid, row, col):
	if row == 9:
		return True
	if col == 9:
		return fill_grid(grid, row + 1, 0)
	if grid[row][col] != 0:
		return fill_grid(grid, row, col + 1)

	nums = list(range(1, 10))
	random.shuffle(nums)

	for num in nums:
		if is_Safe(grid, row, col, num):
			grid[row][col] = num
			if fill_grid(grid, row, col + 1):
				return True
			grid[row][col] = 0
	return False

def generate_sudoku():
	grid=[]
	for i in range(9):
		row =[]	
		for j in range(9):
			row.append(0)
		grid.append(row)

	fill_grid(grid, 0, 0)
	return grid
def remove_cells(grid, count):
    removed = 0
    while removed < count:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if grid[r][c] != 0:
            grid[r][c] = 0
            removed += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def user_move(grid,original, row, col, num):
	if original[row][col]!=0:
		return False
	if num==0:
		grid[row][col]=0
		return True
	if is_Safe(grid, row, col, num):
		grid[row][col] = num
		return True
	return False 


sud = generate_sudoku()
puzzle = remove_cells([row[:] for row in sud], 40)
original_puzzle = [row[:] for row in puzzle]

print("Generated puzzle:")
print_grid(puzzle)
print("Type -1 in row to quit and -2 in row to show the full solved puzzle.")
print()
print("To change the value which you added ,go to the specific cell and then give the desired value or set it to zero to erase the value.")
print()

quit_game=False
while True:
	print("\nEnter your move :")
	
	while True:
		r = int(input("Row (0–8): "))
		while (r<0 and( r!=-1 and r!=-2)) or r>=9 :
			print("OUT OF RANGE")
			r = int(input("Row (0–8): "))
		if r == -1:
			print("You quit the game!")
			quit_game = True
			break  
		if r == -2: 
			print("Solved Sudoku:")
			print_grid(sud)
			
			print("Enter your next move:")
			print()
			print("Enter choice 1 to generate a new puzzle:")
			print()
			print("Enter choice -1 to quit")
			print()
			print("To change the value which you added ,Change it to zero and then give the desired value.")
			
			choice = int(input("Enter choice: "))
			
			if choice == 1:
				sud = generate_sudoku()
				puzzle = remove_cells([row[:] for row in sud], 40)
				original_puzzle = [row[:] for row in puzzle]
				print("New Puzzle Generated:")
				print_grid(puzzle)
				continue
			else:
				print("You quit the game!")
				quit_game = True
				break



		c = int(input("Column (0–8): "))
		while c<0 or c>=9  :
			print("OUT OF RANGE")
			c = int(input("Column (0–8): "))
		n = int(input("Number (1–9): "))
		while n<1 or n>9:
			print("OUT OF RANGE")
			n = int(input("Number (1–9): "))

		if user_move(puzzle,original_puzzle, r, c, n):
			print("\nValid move!")
			print("\nUpdated Puzzle:")
			print_grid(puzzle)
			break   
		else:
			print("\nInvalid move! Puzzle unchanged. Try again...")
			print_grid(puzzle)  

	if quit_game:
		break  
















