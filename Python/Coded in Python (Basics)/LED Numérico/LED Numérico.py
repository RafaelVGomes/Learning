from os import system
system('cls')

inp = list(input("Digite: "))
n = []

for i in range(0, len(inp)):
    inp[i] = int(inp[i])
    n.append(inp[i])

ns =[
["###", "# #", "# #", "# #", "###"],
["  #", "  #", "  #", "  #", "  #"],
["###", "  #", "###", "#  ", "###"],
["###", "  #", "###", "  #", "###"],
["# #", "# #", "###", "  #", "  #"],
["###", "#  ", "###", "  #", "###"],
["###", "#  ", "###", "# #", "###"],
["###", "  #", "  #", "  #", "  #"],
["###", "# #", "###", "# #", "###"],
["###", "# #", "###", "  #", "  #"]
]

board = []
for i in n:
	board.append(ns[i])

for i in zip(*board):
	print(*i)

