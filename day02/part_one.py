def check_register(r: list):
	order = "asc" if r[0] < r[1] else "desc"
	for i in range(len(r) - 1):
		d = r[i] - r[i + 1]
		if order == "asc" and d > 0:
			return False
		elif order == "desc" and d < 0:
			return False
		if abs(d) not in range(1, 4):
			return False
	return True

def main():
	registers = []
	nb_safes = 0
	with open("input.txt", "r") as file:
		for line in file:
			new_register = list(map(int, line.strip().split()))
			registers.append(new_register)
		for reg in registers:
			if check_register(reg) is True:
				nb_safes += 1
	print(nb_safes)

if __name__ == "__main__":
	main()
