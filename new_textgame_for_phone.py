import os

txt = open("main.txt", "r", encoding="utf-8")
game = list(txt.read())

index = 0
for i in game:
	if i == "p":
		playerIndex = index
	index += 1

index = 0
for i in game:
	if i == "\n":
		width = index + 1
		break
	index += 1

run = True
while run:
	os.system("clear")
	print("", end=" ")
	for i in game:
		print(i, end=" ")

	a = input("<DDOOOOOOOS>::")

	if a == "w":
		game[playerIndex] = " "
		playerIndex -= width
		if game[playerIndex] != " ":
			playerIndex += width
			game[playerIndex] = "p"
		else:
			game[playerIndex] = "p"
	if a == "s":
		game[playerIndex] = " "
		playerIndex += width
		if game[playerIndex] != " ":
			playerIndex -= width
			game[playerIndex] = "p"
		else:
			game[playerIndex] = "p"
	if a == "a":
		game[playerIndex] = " "
		playerIndex -= 1
		if game[playerIndex] != " ":
			playerIndex += 1
			game[playerIndex] = "p"
		else:
			game[playerIndex] = "p"
	if a == "d":
		game[playerIndex] = " "
		playerIndex += 1
		if game[playerIndex] != " ":
			playerIndex -= 1
			game[playerIndex] = "p"
		else:
			game[playerIndex] = "p"
	if a == "e":
		run = False