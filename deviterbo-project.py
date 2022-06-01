consant_board = [	["-", "x", "-", "x", "-", "x","-","x","-","x","0"],
					["x", "-", "x", "-", "x","-","x","-","x", "-","1"],
					["-", "x", "-", "x", "-", "x","-","x","-","x","2"],
					["-", "-", "-", "-", "-","-","-","-","-","-","3"],
					["-", "-", "-", "-", "-","-","-","-","-","-","4"],
					["-", "-", "-", "-", "-","-","-","-","-","-","5"],
					["-", "-", "-", "-", "-","-","-","-","-","-","6"],
					["o", "-", "o", "-", "o","-","o","-","o","-","7"],
					["-", "o", "-", "o", "-", "o","-","o","-","o","8"],
					["o", "-", "o", "-", "o","-","o","-","o","-","9"],
					["0", "1", "2","3","4","5","6","7","8","9", " ",]]
#checker_take_after function 
# board = [	["-", "-", "-", "-", "-", "-","-","-","-","-","0"],
# 			["-", "-", "-", "-", "-","-","-","-","-", "-","1"],
# 			["-", "-", "-", "-", "-", "x","-","-","-","-","2"],
# 			["-", "-", "o", "-", "-","-","-","-","-","-","3"],
# 			["-", "-", "-", "-", "-","x","-","-","-","-","4"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","5"],
# 			["-", "-", "-", "x", "-","-","-","-","-","-","6"],
# 			["o", "-", "o", "-", "o","-","o","-","o","-","7"],
# 			["-", "o", "-", "o", "-", "o","-","o","-","o","8"],
# 			["o", "-", "o", "-", "o","-","o","-","o","-","9"],
# 			["0", "1", "2","3","4","5","6","7","8","9", " ",]]
#checker_take_after function player 2
# board = [	["-", "x", "-", "x", "-", "x","-","x","-","x","0"],
# 			["x", "-", "x", "-", "o","-","x","-","x", "-","1"],
# 			["-", "-", "-", "-", "-", "-","-","x","-","x","2"],
# 			["-", "-", "o", "-", "-","-","-","-","-","-","3"],
# 			["-", "-", "-", "-", "-","x","-","-","-","-","4"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","5"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","6"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","7"],
# 			["-", "-", "-", "-", "-", "-","-","-","-","-","8"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","9"],
# 			["0", "1", "2","3","4","5","6","7","8","9", " ",]]

#dama_checker function player 1
# board = [	["-", "-", "-", "-", "-", "-","-","-","-","-","0"],
# 			["-", "-", "-", "-", "-","-","-","-","x", "-","1"],
# 			["-", "-", "-", "x", "-", "x","-","x","-","-","2"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","3"],
# 			["-", "o", "-", "-", "-","x","-","-","-","-","4"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","5"],
# 			["-", "-", "-", "x", "-","-","-","-","-","-","6"],
# 			["-", "-", "O", "-", "-","-","-","-","-","-","7"],
# 			["-", "-", "-", "-", "-", "-","-","-","-","-","8"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","9"],
# 			["0", "1", "2","3","4","5","6","7","8","9", " ",]]
# dama_checker function player 2
# board = [	["-", "-", "-", "-", "-", "-","-","-","-","-","0"],
# 			["-", "X", "-", "-", "-","-","-","o","-", "-","1"],
# 			["-", "-", "o", "-", "-", "-","-","-","-","-","2"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","3"],
# 			["-", "-", "-", "-", "-","-","-","-","o","-","4"],
# 			["-", "-", "-", "-", "-","o","-","-","-","-","5"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","6"],
# 			["-", "-", "-", "-", "-","-","-","o","-","-","7"],
# 			["-", "-", "-", "-", "-", "-","-","-","o","-","8"],
# 			["-", "-", "-", "-", "-","-","-","-","-","-","9"],
# 			["0", "1", "2","3","4","5","6","7","8","9", " ",]]

board = [	["-", "x", "-", "x", "-", "x","-","x","-","x","0"],
			["x", "-", "x", "-", "x","-","x","-","x", "-","1"],
			["-", "x", "-", "x", "-", "x","-","x","-","x","2"],
			["-", "-", "-", "-", "-","-","-","-","-","-","3"],
			["-", "-", "-", "-", "-","-","-","-","-","-","4"],
			["-", "-", "-", "-", "-","-","-","-","-","-","5"],
			["-", "-", "-", "-", "-","-","-","-","-","-","6"],
			["o", "-", "o", "-", "o","-","o","-","o","-","7"],
			["-", "o", "-", "o", "-", "o","-","o","-","o","8"],
			["o", "-", "o", "-", "o","-","o","-","o","-","9"],
			["0", "1", "2","3","4","5","6","7","8","9", " ",]]

def dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	blank_spot  = [] #player1 - it contains valid-available blankspots player1 MUST land his/her piece
	l_x1 = l_x2 #swapping from def(dama) - second coordinates niya will become its first coordinate
	l_y1 = l_y2

	######################### U P P E R  L E F T ##################################
	temp_x = l_x1-1 #itself is not included
	temp_y = l_y1-1
	ordered_pair = [] #valid x's to be taken in heaven 
	while temp_x!=-1 and temp_y!=-1: #upper-left
		if mainboard[temp_y][temp_x]=="o" or mainboard[temp_y][temp_x]=="O":
			break  
		elif (mainboard[temp_y][temp_x]=="x" or mainboard[temp_y][temp_x]=="X") and mainboard[temp_y-1][temp_x-1]=="-" and (mainboard[temp_y+1][temp_x+1]!="x" and mainboard[temp_y+1][temp_x+1]!="X"):  	
			ordered_pair.append([temp_x,temp_y])
		temp_x-=1
		temp_y-=1
	##########################L O W E R  R I G H T ##################################
	temp_x_b = l_x1+1
	temp_y_b = l_y1+1
	ordered_pair_b = [] #valid x's to be taken in heaven 
	while temp_x_b!=10 and temp_y_b!=10: #lower-right
		if mainboard[temp_y_b][temp_x_b]=="o" or mainboard[temp_y_b][temp_x_b]=="O":
			break
		elif (mainboard[temp_y_b][temp_x_b]=="x" or mainboard[temp_y_b][temp_x_b]=="X") and mainboard[temp_y_b+1][temp_x_b+1]=="-" and (mainboard[temp_y_b-1][temp_x_b-1]!="x" and mainboard[temp_y_b-1][temp_x_b-1]!="X"):  	
			ordered_pair_b.append([temp_x_b,temp_y_b])
		temp_x_b+=1
		temp_y_b+=1
	########################## U P P E R  R I G H T #################################
	temp_x_c = l_x1+1
	temp_y_c = l_y1-1
	ordered_pair_c = [] #valid x's to be taken in heaven 
	while temp_x_c!=10 and temp_y_c!=-1: #upper right
		if mainboard[temp_y_c][temp_x_c]=="o" or mainboard[temp_y_c][temp_x_c]=="O":
			break
		elif (mainboard[temp_y_c][temp_x_c]=="x" or mainboard[temp_y_c][temp_x_c]=="X") and mainboard[temp_y_c-1][temp_x_c+1]=="-" and (mainboard[temp_y_c+1][temp_x_c-1]!="x" and mainboard[temp_y_c+1][temp_x_c-1]!="X"):  	
			ordered_pair_c.append([temp_x_c,temp_y_c])
		temp_x_c+=1
		temp_y_c-=1
	########################### L O W E R  L E F T ##############################
	temp_x_d = l_x1-1
	temp_y_d = l_y1+1
	ordered_pair_d = [] #valid x's to be taken in heaven 
	while temp_x_d!=-1 and temp_y_d!=10: #lower-left
		if mainboard[temp_y_d][temp_x_d]=="o" or mainboard[temp_y_d][temp_x_d]=="O":
			break
		elif (mainboard[temp_y_d][temp_x_d]=="x" or mainboard[temp_y_d][temp_x_d]=="X") and mainboard[temp_y_d+1][temp_x_d-1]=="-" and ((mainboard[temp_y_d-1][temp_x_d+1]!="x") and (mainboard[temp_y_d-1][temp_x_d+1]!="X")):  	
			ordered_pair_d.append([temp_x_d,temp_y_d])
		temp_x_d-=1
		temp_y_d+=1
	########################## P A G T A T A T A P O S ###############################

	try: #TRY - OUT OF RANGE --> IF ordered_pair is empty, I assumed all directions consist of x's (so I use "try/except")
		xx = ordered_pair[len(ordered_pair)-1][0] #minus 1 because list starts to count from 0 to n
		yy = ordered_pair[len(ordered_pair)-1][1] #ordered_pair is list
		xx_a = xx-1 #itself ordered_pair of "x" is not included in finding available available blank spots (upper left)
		yy_a = yy-1 
		while xx_a!=-1 and yy_a!=-1: #upper-left - iterates blank valid spots
			if mainboard[yy_a][xx_a]=="-":
				blank_spot.append([xx_a,yy_a])
			else:
				break #break already if it detects non-blank spot (might block already)
			xx_a-=1
			yy_a-=1
	except:
		pass
	try:
		xxb = ordered_pair_b[len(ordered_pair_b)-1][0] #minus 1 because list starts to count from 0 to n
		yyb = ordered_pair_b[len(ordered_pair_b)-1][1]
		xx_b = xxb+1 #itself ordered_pair of "x" is not included in finding available available blank spots (lower right)
		yy_b = yyb+1
		while xx_b!=10 and yy_b!=10: #lower-right - iterates blank valid spots
			if mainboard[yy_b][xx_b]=="-":
				blank_spot.append([xx_b,yy_b])
			else:
				break
			xx_b+=1
			yy_b+=1
	except:
		pass
	try:
		xxc = ordered_pair_c[len(ordered_pair_c)-1][0] #minus 1 because list starts to count from 0 to n
		yyc = ordered_pair_c[len(ordered_pair_c)-1][1]
		xx_c = xxc+1 #itself ordered_pair of "x" is not included in finding available available blank spots (upper right)
		yy_c = yyc-1
		while xx_c!=10 and yy_c!=-1: #upper right - iterates blank valid spots
			if mainboard[yy_c][xx_c]=="-":
				blank_spot.append([xx_c,yy_c])
			else:
				break
			xx_c+=1
			yy_c-=1
	except:
		pass
	try:
		xxd = ordered_pair_d[len(ordered_pair_d)-1][0] #minus 1 because list starts to count from 0 to n
		yyd = ordered_pair_d[len(ordered_pair_d)-1][1]
		xx_d = xxd-1 #itself ordered_pair of "x" is not included in finding available available blank spots (lower left)
		yy_d = yyd+1
		while xx_d!=-1 and yy_d!=10: #lower-left - iterates blank valid spots 
			if mainboard[yy_d][xx_d]=="-":
				blank_spot.append([xx_d,yy_d])
			else:
				break
			xx_d-=1
			yy_d+=1
	except:
		pass

	#if any of the direction given above consists of x's with respective valid landspot, then this player
	#must move his/her piece to take opponent's piece
	if len(ordered_pair)>0 or len(ordered_pair_b)>0 or len(ordered_pair_c)>0 or len(ordered_pair_d)>0:
		while True:
			checkerboard(mainboard)
			try:
				l_x2,l_y2 = input("[O] Move to: ").split(",")
			except:
				while True:
					print("\n\n[1] Save and exit")
					print("[2] Continue playing")
					save_continue = int(input("Select: "))
					if save_continue==1:
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif save_continue==2:
						break
					else:
						print("Invalid choice")
			else:
				l_x2,l_y2 = int(l_x2),int(l_y2) #str to int
				if l_x1>l_x2 and l_y1>l_y2:#upper left ||||||||||||||||||||||N A S A L A   N A||||||||||||||||
					if [l_x2,l_y2] not in blank_spot: #if not in blankspot, then it is invalid
						print("Take available pieces!")
					else: #valid
						mainboard[l_y2][l_x2]="O"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair)): #replacing all x's (opponent's piece) to "-" (taking/eating)
							bye_x = ordered_pair[i][0] #ordered_pair == upper left
							bye_y = ordered_pair[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

				elif l_x1<l_x2 and l_y1<l_y2: #lower right  ||||||||||||||||||||||N A S A L A   N A||||||||||||||||
					if [l_x2,l_y2] not in blank_spot: #if not in blankspot, then it is invalid
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="O"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_b)): #replacing all x's (opponent's piece) to "-" (taking/eating)
							bye_x = ordered_pair_b[i][0] #ordered_pair == lower right
							bye_y = ordered_pair_b[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif l_x1<l_x2 and l_y1>l_y2: #upper right ||||||||||||||||||||||N A S A L A   N A||||||||||||||||
					if [l_x2,l_y2] not in blank_spot: #if not in blankspot, then it is invalid
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="O"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_c)): #replacing all x's (opponent's piece) to "-" (taking/eating)
							bye_x = ordered_pair_c[i][0] #ordered_pair == upper right
							bye_y = ordered_pair_c[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif l_x1>l_x2 and l_y1<l_y2: #lower left ||||||||||||||||||||||N A S A L A   N A||||||||||||||||
					if [l_x2,l_y2] not in blank_spot: #if not in blankspot, then it is invalid
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="O"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_d)): #replacing all x's (opponent's piece) to "-" (taking/eating)
							bye_x = ordered_pair_d[i][0]
							bye_y = ordered_pair_d[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Take available pieces first!")
	else:
		count+=1
		move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)


def dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	blank_spot  = []
	l_x1 = l_x2
	l_y1 = l_y2
	###########################################################
	temp_x = l_x1-1
	temp_y = l_y1-1
	ordered_pair = [] #valid x's to be taken in heaven 
	while temp_x!=-1 and temp_y!=-1: #upper-left
		if mainboard[temp_y][temp_x]=="x" or mainboard[temp_y][temp_x]=="X":
			break  
		elif (mainboard[temp_y][temp_x]=="o" or mainboard[temp_y][temp_x]=="O") and mainboard[temp_y-1][temp_x-1]=="-" and (mainboard[temp_y+1][temp_x+1]!="o" and mainboard[temp_y+1][temp_x+1]!="O"):  	
			ordered_pair.append([temp_x,temp_y])
		temp_x-=1
		temp_y-=1
	#############################################################
	temp_x_b = l_x1+1
	temp_y_b = l_y1+1
	ordered_pair_b = [] #valid x's to be taken in heaven 
	while temp_x_b!=10 and temp_y_b!=10: #lower-right
		if mainboard[temp_y_b][temp_x_b]=="x" or mainboard[temp_y_b][temp_x_b]=="X":
			break
		elif (mainboard[temp_y_b][temp_x_b]=="o" or mainboard[temp_y_b][temp_x_b]=="O") and mainboard[temp_y_b+1][temp_x_b+1]=="-" and (mainboard[temp_y_b-1][temp_x_b-1]!="o" and mainboard[temp_y_b-1][temp_x_b-1]!="O"):  	
			ordered_pair_b.append([temp_x_b,temp_y_b])
		temp_x_b+=1
		temp_y_b+=1
	###########################################################
	temp_x_c = l_x1+1
	temp_y_c = l_y1-1
	ordered_pair_c = [] #valid x's to be taken in heaven 
	while temp_x_c!=10 and temp_y_c!=-1: #upper right
		if mainboard[temp_y_c][temp_x_c]=="x" or mainboard[temp_y_c][temp_x_c]=="X":
			break
		elif (mainboard[temp_y_c][temp_x_c]=="o" or mainboard[temp_y_c][temp_x_c]=="O") and mainboard[temp_y_c-1][temp_x_c+1]=="-" and (mainboard[temp_y_c+1][temp_x_c-1]!="o" and mainboard[temp_y_c+1][temp_x_c-1]!="O"):  	
			ordered_pair_c.append([temp_x_c,temp_y_c])
		temp_x_c+=1
		temp_y_c-=1
	#########################################################
	temp_x_d = l_x1-1
	temp_y_d = l_y1+1
	ordered_pair_d = [] #valid x's to be taken in heaven 
	while temp_x_d!=-1 and temp_y_d!=10: #lower-left
		if mainboard[temp_y_d][temp_x_d]=="x" or mainboard[temp_y_d][temp_x_d]=="X":
			break
		elif (mainboard[temp_y_d][temp_x_d]=="o" or mainboard[temp_y_d][temp_x_d]=="O") and mainboard[temp_y_d+1][temp_x_d-1]=="-" and ((mainboard[temp_y_d-1][temp_x_d+1]!="o") and (mainboard[temp_y_d-1][temp_x_d+1]!="O")):  	
			ordered_pair_d.append([temp_x_d,temp_y_d])
		temp_x_d-=1
		temp_y_d+=1
	#########################################################
	try:
		xx = ordered_pair[len(ordered_pair)-1][0]
		yy = ordered_pair[len(ordered_pair)-1][1]
		xx_a = xx-1 #itself x is not included
		yy_a = yy-1 
		while xx_a!=-1 and yy_a!=-1: #upper-left - iterates blank valid spots
			if mainboard[yy_a][xx_a]=="-":
				blank_spot.append([xx_a,yy_a])
			else:
				break #break already if it detects non-blank spot (might block already)
			xx_a-=1
			yy_a-=1
	except:
		pass
	try:
		xxb = ordered_pair_b[len(ordered_pair_b)-1][0]
		yyb = ordered_pair_b[len(ordered_pair_b)-1][1]
		xx_b = xxb+1
		yy_b = yyb+1
		while xx_b!=10 and yy_b!=10: #lower-right
			if mainboard[yy_b][xx_b]=="-":
				blank_spot.append([xx_b,yy_b])
			else:
				break
			xx_b+=1
			yy_b+=1
	except:
		pass
	try:
		xxc = ordered_pair_c[len(ordered_pair_c)-1][0]
		yyc = ordered_pair_c[len(ordered_pair_c)-1][1]
		xx_c = xxc+1
		yy_c = yyc-1
		while xx_c!=10 and yy_c!=-1: #upper right
			if mainboard[yy_c][xx_c]=="-":
				blank_spot.append([xx_c,yy_c])
			else:
				break
			xx_c+=1
			yy_c-=1
	except:
		pass
	try:
		xxd = ordered_pair_d[len(ordered_pair_d)-1][0]
		yyd = ordered_pair_d[len(ordered_pair_d)-1][1]
		xx_d = xxd-1
		yy_d = yyd+1
		while xx_d!=-1 and yy_d!=10: #lower-left
			if mainboard[yy_d][xx_d]=="-":
				blank_spot.append([xx_d,yy_d])
			else:
				break
			xx_d-=1
			yy_d+=1
	except:
		pass
	if len(ordered_pair)>0 or len(ordered_pair_b)>0 or len(ordered_pair_c)>0 or len(ordered_pair_d)>0:
		while True:
			checkerboard(mainboard)
			try:
				l_x2,l_y2 = input("[X] Move to: ").split(",")
			except:
				while True:
					print("\n\n[1] Save and exit")
					print("[2] Continue playing")
					save_continue = int(input("Select: "))
					if save_continue==1:
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif save_continue==2:
						break
					else:
						print("Invalid choice")
			else:
				l_x2,l_y2 = int(l_x2),int(l_y2)
				if l_x1>l_x2 and l_y1>l_y2:#upper left
					if [l_x2,l_y2] not in blank_spot:
						print("Take available pieces!")
					else:
						mainboard[l_y2][l_x2]="X"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair)):
							bye_x = ordered_pair[i][0]
							bye_y = ordered_pair[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif l_x1<l_x2 and l_y1<l_y2: #lower right
					if [l_x2,l_y2] not in blank_spot:
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="X"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_b)):
							bye_x = ordered_pair_b[i][0]
							bye_y = ordered_pair_b[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif l_x1<l_x2 and l_y1>l_y2: #upper right
					if [l_x2,l_y2] not in blank_spot:
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="X"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_c)):
							bye_x = ordered_pair_c[i][0]
							bye_y = ordered_pair_c[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif l_x1>l_x2 and l_y1<l_y2: #lower left
					if [l_x2,l_y2] not in blank_spot:
						print("Take all available pieces!")
					else:
						mainboard[l_y2][l_x2]="X"
						mainboard[l_y1][l_x1]="-"
						for i in range(len(ordered_pair_d)):
							bye_x = ordered_pair_d[i][0]
							bye_y = ordered_pair_d[i][1]
							mainboard[bye_y][bye_x]="-"
						blank_spot.clear()
						ordered_pair.clear()
						ordered_pair_b.clear()
						ordered_pair_c.clear()
						ordered_pair_d.clear()
						dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Take available pieces first!")
	else:
		count-=1
		move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)




def instruction():
	print("\n\n\n===========================I N S T R U C T I O N===============================")
	print("\n\n-This checkerboard game consists of 10x10 grid starting from 0-9 coordinates in both x and y axes.")
	print("-Each player is in control of one kind of pieces.")
	print("-Player1 will control the 'o' pieces while Player2 will control the 'x' pieces.")
	print("-Pieces must jump the other dash in diagonal direction.")
	print("-Just type your coordinates in comma-separated with no space.")
	print("-Player will be declared a loser if his/her all pieces is completely taken.")
	print("-Player1's king will represent as capital 'O' while Player2's king will represent as capital 'X'")
	print("If any error occured in typing one's input, the program will request to save or continue playing the game.")
	print("\n\n\n============================H O W   TO  S A V E=================================")
	print("-Instead of typing your first/second coordinates, just type 'Save' to save your game")
	print("-Use '.txt' as file extension.\n\n\n")

def check_player2(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2):
	left = 0 #for player 2 - it checks player2's pieces if there are no remaining piece (considered as loser) 
	for y in mainboard:
		for x in y:
			if x=="x" or x=="X":
				left+=1
				break
	else:
		if left==0: #if 0, then player 2 will decalared a winner
			score_p1+=1
			checkerboard(mainboard)
			print("\n----------------------------------Player 1 wins !-----------------------------")
			print("-----Select choice-----")
			print("[1] Save and Exit")
			print("[2] New game")
			while True:
				try:
					choice = int(input("\nSelect: "))
				except:
					print("Enter a valid choice/integer.")
				else:	
					if choice==1:
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						mainboard = new_board #resetting the board by default
						players_turn(count, mainboard,l_x1,l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Enter a valid choice/integer")

def check_player1(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2):
	left2 = 0 #it checks player 1 if there are no more pieces remaining in his/her ...... 
	for y in mainboard:
		for x in y:
			if x=="o" or x=="O":
				left2+=1
				break
	else:
		if left2==0: #if 0, then player 2 will decalared a winner
			score_p2+=1
			checkerboard(mainboard)
			print("\n----------------------------------Player 2 wins !-----------------------------")
			print("Do you want to save?")
			print("[1] Save and exit")
			print("[2] New game")
			while True:
				try:
					choice = int(input("\nSelect: "))
				except:
					print("Enter a valid choice/integer.")
				else:	
					if choice==1:
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						mainboard = new_board
						players_turn(count, mainboard,l_x1,l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Enter a valid choice/integer")
def dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	constant_x = l_x1 #store the value of 1_x1/l_y1 -- for resetting the value of l_x1/l_y1 if error occur
	constant_y = l_y1 #not changing
	while True:
		try:
			k_x2,k_y2 = input("[O] Move to: ").split(",") #getting two input (ordered pair) in one line
		except:
			while True:
				print("\n\n[1] Save and exit")
				print("[2] Continue playing")
				save_continue = int(input("Select: "))
				if save_continue==1:
					save(mainboard,count,score_p2,score_p1)
					exit()
				elif save_continue==2:
					dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Invalid choice")
		else:

			k_x2 = int(k_x2) #converting str to int
			k_y2 = int(k_y2)
			l_x2 = k_x2 #reassigning value for def(dama_checker) function
			l_y2 = k_y2 #reassigning value for def(dama_checker) function
			if mainboard[k_y2][k_x2]!="-": 
				print("Invalid move!")
			elif -1>k_x2 or k_x2>9 or -1>k_y2 or k_y2>9:
				print("Coordinates out of range!")
			else:
######################################### U P P E R   L E F T ###########################################################
				if constant_x>k_x2 and constant_y>k_y2: #if it is in upper left movement 
					a_dama_coordinates = {} #contains all valid coordinates in upper-left
					temp_x1 = l_x1 
					temp_y1 = l_y1 #variable temp as reusability of l_x1/l_y1
					key = 0
					#it collects all valid coordinates in upper-left  
					while l_x1!=-1 and l_y1!=-1: #upper-left
						ordered_pair = [l_x1,l_y1]
						a_dama_coordinates[key] = ordered_pair
						l_x1-=1
						l_y1-=1
						key+=1
					else:
						if [k_x2,k_y2] not in a_dama_coordinates.values(): #if second coordinates not in a_dama_coordinates.values(), then it is not valid
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y #resetting to default (l_x1/l_y1)
							a_dama_coordinates.clear() #clearing for reusability
							dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board) #select again
						a_dama_coordinates.pop(0) #pop because the ordered pair itself is not included for checking
						
						a4_dama_coordinates = [] #collects ordered pair in upper-left but stops if it detecs "o"/"O" (limiter)
						for until in a_dama_coordinates.values(): #.values because it is in list
							xx,yy = until[0],until[1] #checks the a_dama_coordinates if one of those contains "o"/"O", then it is now the "limit/until where" of the movement of the plyaer
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O"):
								a4_dama_coordinates.append(until)
								break #checks only exactly once, one piece of "o"/"O" can block the entire diagonal direction
						if len(a4_dama_coordinates)!=0: #if there is an ordered pair containing 'o'/"O"
							aa = a4_dama_coordinates[0][0]
							bb = a4_dama_coordinates[0][1]
							if temp_x1>k_x2 and temp_y1>k_y2 and k_x2>aa and k_y2>bb: #then it should be in between of the first-coordinate and ordered-pair containing "o"/"O" 
								pass #pass because this if statement is the only valid reason, nothing more. 
										#pass to go to the next code of instruction
							else:
								print("Invalid move!")
								a4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						l_x1 = constant_x
						l_y1 = constant_y


						two_x = [] #detects if there are two x/X's blocking the diagonal direction (it limits also)
						for key,value in a_dama_coordinates.items():
							x = int(value[0]) #a_dama_coordinates values in in list (ordered pair)
							y = int(value[1]) #extracting in x-y coordinates
							if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and (mainboard[y-1][x-1]=="x" or mainboard[y-1][x-1]=="X"):
								two_x.append(key)
	################################################################################
						#AFTER GETTING ALL THE POSSIBLE RESTRICTIONS, IT IS NOW TIME FOR "SALAAN" AT "KAINAN"
						
						a3_dama_coordinates = [] #COORDINATES OF ALL PIECES TO BE TAKEN-UP VALIDLY BY THE OPPONENT (BYE-BYE)
						for until in a_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X") and mainboard[yy-1][xx-1]=="-" and (mainboard[yy+1][xx+1]!="x" and mainboard[yy+1][xx+1]!="X"):
								a3_dama_coordinates.append(until)

						if len(two_x)>0 and len(a3_dama_coordinates)>0:
							#IF BOTH TWO_X AND  A3_DAMA_COORDINATES HAS VALUES, THEN IT LIMITS THE MOVEMENT PLUS 
							#IT EATS ALL OPPONENT'S PIECES AFTER SELECTING VALID COORDINATES
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = a_dama_coordinates[extract_x][0] #x - extract_x is a key of where two x's is located, it finds the value (ordered pair) by getting its key from two_x going to a_dama_coordinates 
							b = a_dama_coordinates[extract_x][1] #y - extract_x is a key of where two x's is located, it finds the value (ordered pair) by getting its key from two_x going to a_dama_coordinates 
							xxx = a3_dama_coordinates[len(a3_dama_coordinates)-1][0]
							#minus 1 because len(starts counting from 1 to n) while lists (starts counting from 0 to n)
							#out of range if no minus 1
							#len because it needs to get the last element or the last x-piece to be eaten
							#in dama, it is mandatory to eat all valid available pieces as possible
							yyy = a3_dama_coordinates[len(a3_dama_coordinates)-1][1]
							if a<k_x2 and k_x2<xxx and b<k_y2 and k_y2<yyy:
							#second move must above the pieces to be eaten (xxx,yyy-eat all) but below the two x's (a,b).
								while temp_x1>k_x2 and temp_y1>k_y2: #upper left1
									if mainboard[temp_y1-1][temp_x1-1]=="-" and (mainboard[temp_y1][temp_x1]=="X" or mainboard[temp_y1][temp_x1]=="x"):
										mainboard[temp_y1][temp_x1]="-"
									temp_x1-=1
									temp_y1-=1
									#changing one by one the opponent's piece to  "-" 
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="O"
									two_x.clear()
									a3_dama_coordinates.clear()
									a_dama_coordinates.clear()
									dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else: #if it is not in between, then it is invalid 
								print("Invalid choice!")
								l_x1 = constant_x
								l_y1 = constant_y
		
						elif len(two_x)>0 and len(a3_dama_coordinates)==0: #if it contains two x's, it limits the move
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = a_dama_coordinates[extract_x][0]
							#x - extract_x is a key of where two x's is located, it finds the value (ordered pair) by getting its key from two_x going to a_dama_coordinates
							b = a_dama_coordinates[extract_x][1]
							#y - extract_x is a key of where two x's is located, it finds the value (ordered pair) by getting its key from two_x going to a_dama_coordinates
							if a<k_x2 and k_x2<temp_x1 and b<k_y2 and k_y2<temp_y1: #it should be in between of that (two x's) and first coordinate
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="O"
								two_x.clear()
								a_dama_coordinates.clear()
								a3_dama_coordinates.clear()
								count+=1 #already done
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move!")
								l_x1 = constant_x
								l_y1 = constant_y

						else: #no two two_x, mandatory to eat all piece
							a2_dama_coordinates = {} #same as a3_dama_coordinates (para mas maintindihan) 
							#a2_dama_coordinates contains also the all x's to be validly eaten
							a2_key = 1
							for key,value in a_dama_coordinates.items():
								x,y = int(value[0]), int(value[1])
								if mainboard[y][x]=="o" or mainboard[y][x]=="O":
									break #if it detects again the O, then it limits the move
								else:
									if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and mainboard[y-1][x-1]=="-" and mainboard[k_y2][k_x2]=="-":
										a2_dama_coordinates[a2_key] = value
										a2_key+=1 #adding all valid x's to be validly eaten

							if len(a2_dama_coordinates)!=0: #eats all available pieces diagonally
								a = a2_dama_coordinates[len(a2_dama_coordinates)][0]
								#contains the last ordered pair of a2_dama_coordinates
								#it is mandatory to eat all pieces as much as possible kaya yung last dapat =)
								#walang minus because the key starts at 1, not 0, so it's okay
								b = a2_dama_coordinates[len(a2_dama_coordinates)][1]
								if k_x2<a and k_y2<b: #it should be in between 
									for coordinates in a2_dama_coordinates.values():
									#changing all x values to "-", process of eating/taking one by one
										a = coordinates[0]
										b = coordinates[1]
										mainboard[b][a]="-"
									else:
										mainboard[k_y2][k_x2]="O"
										mainboard[constant_y][constant_x]="-"
										a3_dama_coordinates.clear()
										a2_dama_coordinates.clear()
										a_dama_coordinates.clear()
										l_x1, l_y1, a2_key=constant_x,constant_y,1
										dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									a2_dama_coordinates.clear()
									a_dama_coordinates.clear()
									l_x1, l_y1, a2_key=constant_x,constant_y,1
							else: #move only
								if [k_x2,k_y2] in a_dama_coordinates.values():
									mainboard[k_y2][k_x2]="O"
									mainboard[constant_y][constant_x]="-"
									a2_dama_coordinates.clear()
									a_dama_coordinates.clear()
									a3_dama_coordinates.clear()
									count+=1
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)


######################################### L O W E R   R I G H T ###########################################################
				elif constant_x<k_x2 and constant_y<k_y2: #if it is in lower-right movement
					b_dama_coordinates = {}
					temp_x1,temp_y1 = l_x1,l_y1
					key = 0
					while l_x1!=10 and l_y1!=10: #lower-right
						ordered_pair = [l_x1,l_y1]
						b_dama_coordinates[key]= ordered_pair
						l_x1+=1
						l_y1+=1
						key+=1
					else:
						if [k_x2,k_y2] not in b_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							b_dama_coordinates.clear()
							dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						b_dama_coordinates.pop(0)

						b4_dama_coordinates = []
						for until in b_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O"):
								b4_dama_coordinates.append(until)
								break
						if len(b4_dama_coordinates)!=0:
							aa = b4_dama_coordinates[0][0]
							bb = b4_dama_coordinates[0][1]
							if temp_x1<k_x2 and temp_y1<k_y2 and k_x2<aa and k_y2<bb:
								pass
							else:
								print(l_x1,l_y1)
								print("Invalid move!")
								b4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						l_x1 = constant_x
						l_y1 = constant_y

						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
									#two_x contains the key where the two x's appear first
						for key,value in b_dama_coordinates.items():
							x,y = int(value[0]),int(value[1])
							if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and (mainboard[y+1][x+1]=="x" or mainboard[y+1][x+1]=="X"):
								two_x.append(key)
						
						b3_dama_coordinates = []
						for until in b_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X") and mainboard[yy+1][xx+1]=="-" and (mainboard[yy-1][xx-1]!="x" and mainboard[yy-1][xx-1]!="X"):
								b3_dama_coordinates.append(until)
						
						if len(two_x)>0 and len(b3_dama_coordinates)>0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = b_dama_coordinates[extract_x][0]
							b = b_dama_coordinates[extract_x][1]
							xxx = b3_dama_coordinates[len(b3_dama_coordinates)-1][0]
							yyy = b3_dama_coordinates[len(b3_dama_coordinates)-1][1]
							
							if a>k_x2 and k_x2>xxx and b>k_y2 and k_y2>yyy:
								while temp_x1<k_x2 and temp_y1<k_y2: #lower right1
									if mainboard[temp_y1+1][temp_x1+1]=="-" and (mainboard[temp_y1][temp_x1]=="x" or mainboard[temp_y1][temp_x1]=="X"):
										mainboard[temp_y1][temp_x1]="-"
									temp_x1+=1
									temp_y1+=1
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="O"
									two_x.clear()
									b3_dama_coordinates.clear()
									b_dama_coordinates.clear()
									dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y

						elif len(two_x)>0 and len(b3_dama_coordinates)==0: 
							extract_x = two_x[0]
							a,b = b_dama_coordinates[extract_x][0],b_dama_coordinates[extract_x][1] 
							if a>k_x2 and k_x2>temp_x1 and b>k_y2 and k_y2>temp_y1:
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="O"
								two_x.clear()
								b3_dama_coordinates.clear()
								b_dama_coordinates.clear()
								count+=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y
						else:
							b2_dama_coordinates = {}
							b2_key = 1
							for key,value in b_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="o" or mainboard[y][x]=="O":
									break
								else:
									if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and mainboard[y+1][x+1]=="-" and mainboard[k_y2][k_x2]=="-":
										b2_dama_coordinates[b2_key] = value
										b2_key+=1	
							if len(b2_dama_coordinates)!=0:	
								a = b2_dama_coordinates[len(b2_dama_coordinates)][0]
								b = b2_dama_coordinates[len(b2_dama_coordinates)][1]							
								if k_x2>a and k_y2>b:	
									for coordinates in b2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1] 
										mainboard[b][a]="-" 
									else:
										mainboard[k_y2][k_x2]="O"
										mainboard[constant_y][constant_x]="-"
										b2_dama_coordinates.clear()
										b_dama_coordinates.clear()
										b3_dama_coordinates.clear()
										l_x1, l_y1, b2_key = constant_x,constant_y,1
										print(149)
										dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									b2_dama_coordinates.clear()
									b_dama_coordinates.clear()
									b3_dama_coordinates.clear()
									l_x1, l_y1, b2_key = constant_x,constant_y,1
							else: #move only
								if [k_x2,k_y2] in b_dama_coordinates.values():
									mainboard[k_y2][k_x2]="O"
									mainboard[constant_y][constant_x]="-"
									b2_dama_coordinates.clear()
									b_dama_coordinates.clear()
									b3_dama_coordinates.clear()
									count+=1
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)									
										
######################################### U P P E R   R I G H T ###########################################################
				elif constant_x<k_x2 and constant_y>k_y2: #if it is in upper-right movement
					c_dama_coordinates = {}
					temp_x1 = l_x1
					temp_y1 = l_y1
					key = 0
					while l_x1!=10 and l_y1!=-1: #upper-right
						ordered_pair = [l_x1,l_y1]
						c_dama_coordinates[key] = ordered_pair
						l_x1+=1
						l_y1-=1
						key+=1
					else:
						if [k_x2,k_y2] not in c_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							c_dama_coordinates.clear()
							dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						c_dama_coordinates.pop(0)
						c4_dama_coordinates = []
						for until in c_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O"):
								c4_dama_coordinates.append(until)
								break
						if len(c4_dama_coordinates)!=0:
							aa = c4_dama_coordinates[0][0]
							bb = c4_dama_coordinates[0][1]
							if temp_x1<k_x2 and temp_y1>k_y2 and k_x2<aa and k_y2>bb:
								pass
							else:
								print("Invalid move!")
								c4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						l_x1 = constant_x
						l_y1 = constant_y




						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
						for key,value in c_dama_coordinates.items():
							x,y = value[0],value[1]
							if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and (mainboard[y-1][x+1]=="x" or mainboard[y-1][x+1]=="X"):
								two_x.append(key)
						
						c3_dama_coordinates=[]

						for until in c_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X") and mainboard[yy-1][xx+1]=="-" and (mainboard[yy+1][xx-1]!="x" and mainboard[yy+1][xx-1]!="X"):
								c3_dama_coordinates.append(until)		

						if len(two_x)>0 and len(c3_dama_coordinates)>0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = c_dama_coordinates[extract_x][0]
							b = c_dama_coordinates[extract_x][1]
							xxx = c3_dama_coordinates[len(c3_dama_coordinates)-1][0]
							yyy = c3_dama_coordinates[len(c3_dama_coordinates)-1][1]
							if a>k_x2 and k_x2>xxx and b<k_y2 and k_y2<yyy:
								while temp_x1<k_x2 and temp_y1>k_y2: #UPPER RIGHT
									if (mainboard[temp_y1-1][temp_x1+1]=="-") and (mainboard[temp_y1][temp_x1]=="x" or mainboard[temp_y1][temp_x1]=="X"):
										mainboard[temp_y1][temp_x1]="-"
									temp_y1-=1
									temp_x1+=1

								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="O"
									two_x.clear()
									c3_dama_coordinates.clear()
									c_dama_coordinates.clear()
									dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								c3_dama_coordinates.clear()
								l_x1,l_y1 = constant_x,constant_y


						elif len(two_x)>0 and len(c3_dama_coordinates)==0: 
							extract_x = two_x[0]
							a,b = c_dama_coordinates[extract_x][0],c_dama_coordinates[extract_x][1]
							if a>k_x2 and k_x2>temp_x1 and b<k_y2 and k_y2<temp_y1:		
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="O"
								two_x.clear()
								c3_dama_coordinates.clear()
								c_dama_coordinates.clear()
								count+=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y
						else:
							c2_dama_coordinates = {}
							c2_key = 1
							for key,value in c_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="o" or mainboard[y][x]=="O":
									break
								else:
									if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and mainboard[y-1][x+1]=="-" and mainboard[k_y2][k_x2]=="-":
										c2_dama_coordinates[c2_key] = value
										c2_key+=1

							if len(c2_dama_coordinates)!=0:
								a = c2_dama_coordinates[len(c2_dama_coordinates)][0]
								b = c2_dama_coordinates[len(c2_dama_coordinates)][1]					
								if k_x2>a and k_y2<b:	
									for coordinates in c2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1] 
										mainboard[b][a]="-" 
									else:
										mainboard[k_y2][k_x2]="O"
										mainboard[constant_y][constant_x]="-"
										c_dama_coordinates.clear()
										c2_dama_coordinates.clear()
										c3_dama_coordinates.clear()
										l_x1,l_y1,c2_key = constant_x,constant_y,1
										dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									c2_dama_coordinates.clear()
									c3_dama_coordinates.clear()
									c_dama_coordinates.clear()
									l_x1,l_y1,c2_key = constant_x,constant_y,1
							else:
								if [k_x2,k_y2] in c_dama_coordinates.values():
									mainboard[k_y2][k_x2]="O"
									mainboard[constant_y][constant_x]="-"
									count+=1
									c2_dama_coordinates.clear()
									c_dama_coordinates.clear()
									c3_dama_coordinates.clear()
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

######################################### L O W E R  L E F T ###########################################################
				elif constant_x>k_x2 and constant_y<k_y2: #if it is in lower-left movement
					d_dama_coordinates = {}
					temp_x1 = l_x1
					temp_y1 = l_y1
					key = 0
					while l_x1!=-1 and l_y1!=10: #lower-left
						ordered_pair = [l_x1,l_y1]
						d_dama_coordinates[key] = ordered_pair
						l_x1-=1
						l_y1+=1
						key+=1
					else:
						if [k_x2,k_y2] not in d_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							d_dama_coordinates.clear()
							dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						d_dama_coordinates.pop(0)

						d4_dama_coordinates = []
						for until in d_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O"):
								d4_dama_coordinates.append(until)
								break
						if len(d4_dama_coordinates)!=0:
							aa = d4_dama_coordinates[0][0]
							bb = d4_dama_coordinates[0][1]
							if temp_x1>k_x2 and temp_y1<k_y2 and k_x2>aa and k_y2<bb:
								pass
							else:
								print("Invalid move!")
								d4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)


						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
						for key,value in d_dama_coordinates.items():
							x,y = value[0],value[1] 
							if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and (mainboard[y+1][x-1]=="x" or mainboard[y+1][x-1]=="X"):
								two_x.append(key)
				
						d3_dama_coordinates = []
						for until in d_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X") and mainboard[yy+1][xx-1]=="-" and (mainboard[yy-1][xx+1]!="x" and mainboard[yy-1][xx+1]!="X"):
								d3_dama_coordinates.append(until)

						if len(two_x)>0 and len(d3_dama_coordinates)>0:
							extract_x = two_x[0]
							a,b = d_dama_coordinates[extract_x][0],d_dama_coordinates[extract_x][1]
							xxx = d3_dama_coordinates[len(d3_dama_coordinates)-1][0]
							yyy = d3_dama_coordinates[len(d3_dama_coordinates)-1][1]

							if a<k_x2 and k_x2<xxx and b>k_y2 and k_y2>yyy:
								while temp_x1>k_x2 and temp_y1<k_y2: #lower left1
									if mainboard[temp_y1+1][temp_x1-1]=="-" and (mainboard[temp_y1][temp_x1]=="x" or mainboard[temp_y1][temp_x1]=="X") and (mainboard[temp_y1-1][temp_x1+1]!="x" or mainboard[temp_y1-1][temp_x1+1]!="X"):
										mainboard[temp_y1][temp_x1]="-"
									temp_y1+=1
									temp_x1-=1
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="O"
									two_x.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()
									dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move!")
								l_x1,l_y1 = constant_x,constant_y

						elif len(two_x)>0 and len(d3_dama_coordinates)==0:
							extract_x = two_x[0]
							a,b = d_dama_coordinates[extract_x][0],d_dama_coordinates[extract_x][1]
							if a<k_x2 and k_x2<temp_x1 and b>k_y2 and k_y2>temp_y1:
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="O"
								two_x.clear()
								d_dama_coordinates.clear()
								d3_dama_coordinates.clear()
								d2_dama_coordinates.clear()
								count+=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

							else:
								print("Invalid move!")
								l_x1,l_y1 = constant_x,constant_y
						else:
							d2_dama_coordinates = {}
							d2_key = 1
							for key,value in d_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="o" or mainboard[y][x]=="O":
									break
								else:
									if (mainboard[y][x]=="x" or mainboard[y][x]=="X") and mainboard[y+1][x-1]=="-" and mainboard[k_y2][k_x2]=="-":
										d2_dama_coordinates[d2_key] = value
										d2_key+=1
							if len(d2_dama_coordinates)!=0:
								a = d2_dama_coordinates[len(d2_dama_coordinates)][0]
								b = d2_dama_coordinates[len(d2_dama_coordinates)][1]
								
								if k_x2<a and k_y2>b:
									for coordinates in d2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1]
										mainboard[b][a]="-"
									else:
										mainboard[k_y2][k_x2]="O"
										mainboard[constant_y][constant_x]="-"
										l_x2 = k_x2
										l_y2 = k_y2
										d_dama_coordinates.clear()
										d2_dama_coordinates.clear()
										l_x1,l_y1,d2_key = constant_x,constant_y,1
										d3_dama_coordinates.clear()
										dama_checker(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									d2_dama_coordinates.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()
									l_x1,l_y1,d2_key = constant_x,constant_y,1
							else:
								if [k_x2,k_y2] in d_dama_coordinates.values():
									mainboard[k_y2][k_x2]="O"
									mainboard[constant_y][constant_x]="-"
									count+=1
									d2_dama_coordinates.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Invalid move, not in diagonal")
def dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	constant_x = l_x1 #restore-preserve the value of l_x1/l_y1
	constant_y = l_y1
	while True:
		try:
			k_x2,k_y2 = input("[X] Move to: ").split(",")
		except:
			while True:
				print("\n\n[1] Save and exit")
				print("[2] Continue playing")
				save_continue = int(input("Select: "))
				if save_continue==1:
					save(mainboard,count,score_p2,score_p1)
					exit()
				elif save_continue==2:
					dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Invalid choice")
		else:
			k_x2 = int(k_x2)
			k_y2 = int(k_y2)
			l_x2 = k_x2
			l_y2 = k_y2
			if mainboard[k_y2][k_x2]!="-":
				print("Invalid move!")
			elif -1>k_x2 or k_x2>9 or -1>k_y2 or k_y2>9:
				print("Coordinates out of range!")
			else:
				if constant_x>k_x2 and constant_y>k_y2:
					a_dama_coordinates = {}
					temp_x1 = l_x1
					temp_y1 = l_y1
					key = 0
					while l_x1!=-1 and l_y1!=-1: #upper-left
						ordered_pair = [l_x1,l_y1]
						a_dama_coordinates[key] = ordered_pair
						l_x1-=1
						l_y1-=1
						key+=1
					else:
						if [k_x2,k_y2] not in a_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							a_dama_coordinates.clear()
							dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						a_dama_coordinates.pop(0)

						a4_dama_coordinates = []
						for until in a_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X"):
								a4_dama_coordinates.append(until)
								break
						if len(a4_dama_coordinates)!=0:
							aa = a4_dama_coordinates[0][0]
							bb = a4_dama_coordinates[0][1]
							if temp_x1>k_x2 and temp_y1>k_y2 and k_x2>aa and k_y2>bb:
								pass
							else:
								print("Invalid move!")
								a4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						a4_dama_coordinates.clear()
						l_x1 = constant_x
						l_y1 = constant_y
						two_x = []
						for key,value in a_dama_coordinates.items():
							x,y = value[0],value[1]
							if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and (mainboard[y-1][x-1]=="o" or mainboard[y-1][x-1]=="O"):
								two_x.append(key)

						a3_dama_coordinates = []
						for until in a_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O") and mainboard[yy-1][xx-1]=="-" and (mainboard[yy+1][xx+1]!="o" and mainboard[yy+1][xx+1]!="O"):
								a3_dama_coordinates.append(until)
						if len(two_x)>0 and len(a3_dama_coordinates)>0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = a_dama_coordinates[extract_x][0]
							b = a_dama_coordinates[extract_x][1]
							xxx = a3_dama_coordinates[len(a3_dama_coordinates)-1][0]
							yyy = a3_dama_coordinates[len(a3_dama_coordinates)-1][1]
							if a<k_x2 and k_x2<xxx and b<k_y2 and k_y2<yyy:
								while temp_x1>k_x2 and temp_y1>k_y2: #upper left1
									if mainboard[temp_y1-1][temp_x1-1]=="-" and (mainboard[temp_y1][temp_x1]=="o" or mainboard[temp_y1][temp_x1]=="O"):
										mainboard[temp_y1][temp_x1]="-"
									temp_x1-=1
									temp_y1-=1
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="X"
									two_x.clear()
									a3_dama_coordinates.clear()
									a_dama_coordinates.clear()
									dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid choice!")
								l_x1 = constant_x
								l_y1 = constant_y
		
						elif len(two_x)>0 and len(a3_dama_coordinates)==0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = a_dama_coordinates[extract_x][0]
							b = a_dama_coordinates[extract_x][1]
							if a<k_x2 and k_x2<temp_x1 and b<k_y2 and k_y2<temp_y1:
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="X"
								two_x.clear()
								a_dama_coordinates.clear()
								a3_dama_coordinates.clear()
								count-=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move!")
								l_x1 = constant_x
								l_y1 = constant_y

						else: #no two two_x, mandatory to eat all piece
							a2_dama_coordinates = {}
							a2_key = 1
							for key,value in a_dama_coordinates.items():
								x,y = int(value[0]), int(value[1])
								if mainboard[y][x]=="x" or mainboard[y][x]=="X":
									break
								else:
									if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and mainboard[y-1][x-1]=="-" and mainboard[k_y2][k_x2]=="-":
										a2_dama_coordinates[a2_key] = value
										a2_key+=1
							if len(a2_dama_coordinates)!=0:
								a = a2_dama_coordinates[len(a2_dama_coordinates)][0]
								b = a2_dama_coordinates[len(a2_dama_coordinates)][1]
								if k_x2<a and k_y2<b:
									for coordinates in a2_dama_coordinates.values():
										a = coordinates[0]
										b = coordinates[1]
										mainboard[b][a]="-"
									else:
										mainboard[k_y2][k_x2]="X"
										mainboard[constant_y][constant_x]="-"
										a2_dama_coordinates.clear()
										a_dama_coordinates.clear()
										a3_dama_coordinates.clear()
										l_x1, l_y1, a2_key=constant_x,constant_y,1
										dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)# count-=1
										
								else:
									print("Take all available pieces")
									a2_dama_coordinates.clear()
									a_dama_coordinates.clear()
									l_x1, l_y1, a2_key=constant_x,constant_y,1
							else:
								if [k_x2,k_y2] in a_dama_coordinates.values():
									mainboard[k_y2][k_x2]="X"
									mainboard[constant_y][constant_x]="-"
									a2_dama_coordinates.clear()
									a_dama_coordinates.clear()
									a3_dama_coordinates.clear()
									count-=1
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

				elif constant_x<k_x2 and constant_y<k_y2:
					b_dama_coordinates = {}
					temp_x1,temp_y1 = l_x1,l_y1
					key = 0
					while l_x1!=10 and l_y1!=10: #lower-right
						ordered_pair = [l_x1,l_y1]
						b_dama_coordinates[key]= ordered_pair
						l_x1+=1
						l_y1+=1
						key+=1
					else:
						if [k_x2,k_y2] not in b_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							b_dama_coordinates.clear()
							dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						b_dama_coordinates.pop(0)
						b4_dama_coordinates = []
						for until in b_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X"):
								b4_dama_coordinates.append(until)
								break
						if len(b4_dama_coordinates)!=0:
							aa = b4_dama_coordinates[0][0]
							bb = b4_dama_coordinates[0][1]
							if temp_x1<k_x2 and temp_y1<k_y2 and k_x2<aa and k_y2<bb:
								pass
							else:
								print("Invalid move!")
								b4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

						b4_dama_coordinates.clear()
						l_x1 = constant_x
						l_y1 = constant_y

						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
						for key,value in b_dama_coordinates.items():
							x,y = int(value[0]),int(value[1])
							if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and (mainboard[y+1][x+1]=="o" or mainboard[y+1][x+1]=="O"):
								two_x.append(key)

						b3_dama_coordinates = []
						for until in b_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O") and mainboard[yy+1][xx+1]=="-" and (mainboard[yy-1][xx-1]!="o" and mainboard[yy-1][xx-1]!="O"):
								b3_dama_coordinates.append(until)
						
						if len(two_x)>0 and len(b3_dama_coordinates)>0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = b_dama_coordinates[extract_x][0]
							b = b_dama_coordinates[extract_x][1]
							xxx = b3_dama_coordinates[len(b3_dama_coordinates)-1][0]
							yyy = b3_dama_coordinates[len(b3_dama_coordinates)-1][1]
							
							if a>k_x2 and k_x2>xxx and b>k_y2 and k_y2>yyy:
								while temp_x1<k_x2 and temp_y1<k_y2: #lower right1
									if mainboard[temp_y1+1][temp_x1+1]=="-" and (mainboard[temp_y1][temp_x1]=="o" or mainboard[temp_y1][temp_x1]=="O"):
										mainboard[temp_y1][temp_x1]="-"
									temp_x1+=1
									temp_y1+=1
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="X"
									two_x.clear()
									b3_dama_coordinates.clear()
									b_dama_coordinates.clear()
									dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y


						elif len(two_x)>0 and len(b3_dama_coordinates)==0: 
							extract_x = two_x[0]
							a,b = b_dama_coordinates[extract_x][0],b_dama_coordinates[extract_x][1] 
							if a>k_x2 and k_x2>temp_x1 and b>k_y2 and k_y2>temp_y1:
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="X"
								two_x.clear()
								b3_dama_coordinates.clear()
								b_dama_coordinates.clear()
								count-=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y
						else:
							b2_dama_coordinates = {}
							b2_key = 1
							for key,value in b_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="x" or mainboard[y][x]=="X":
									break
								else:
									if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and mainboard[y+1][x+1]=="-" and mainboard[k_y2][k_x2]=="-":
										b2_dama_coordinates[b2_key] = value
										b2_key+=1	
							if len(b2_dama_coordinates)!=0:	
								a = b2_dama_coordinates[len(b2_dama_coordinates)][0]
								b = b2_dama_coordinates[len(b2_dama_coordinates)][1]							
								if k_x2>a and k_y2>b:	
									for coordinates in b2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1] 
										mainboard[b][a]="-" 
									else:
										mainboard[k_y2][k_x2]="X"
										mainboard[constant_y][constant_x]="-"
										b2_dama_coordinates.clear()
										b_dama_coordinates.clear()
										b3_dama_coordinates.clear()
										l_x1, l_y1, b2_key = constant_x,constant_y,1
										dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									b2_dama_coordinates.clear()
									b_dama_coordinates.clear()
									b3_dama_coordinates.clear()
									l_x1, l_y1, b2_key = constant_x,constant_y,1
							else: #move only
								if [k_x2,k_y2] in c_dama_coordinates.values():
									mainboard[k_y2][k_x2]="X"
									mainboard[constant_y][constant_x]="-"
									b2_dama_coordinates.clear()
									b_dama_coordinates.clear()
									b3_dama_coordinates.clear()
									count-=1
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)	


				elif constant_x<k_x2 and constant_y>k_y2:
					c_dama_coordinates = {}
					temp_x1 = l_x1
					temp_y1 = l_y1
					key = 0
					while l_x1!=10 and l_y1!=-1: #2upper-right
						ordered_pair = [l_x1,l_y1]
						c_dama_coordinates[key] = ordered_pair
						l_x1+=1
						l_y1-=1
						key+=1
					else:
						if [k_x2,k_y2] not in c_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							c_dama_coordinates.clear()
							dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						c_dama_coordinates.pop(0)

						c4_dama_coordinates = []
						for until in c_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X"):
								c4_dama_coordinates.append(until)
								break
						if len(c4_dama_coordinates)!=0:
							aa = c4_dama_coordinates[0][0]
							bb = c4_dama_coordinates[0][1]
							if temp_x1<k_x2 and temp_y1>k_y2 and k_x2<aa and k_y2>bb:
								pass
							else:
								print(l_x1,l_y1)
								print("Invalid move!")
								c4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						c4_dama_coordinates.clear()
						l_x1 = constant_x
						l_y1 = constant_y
						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
						for key,value in c_dama_coordinates.items():
							x,y = value[0],value[1]
							if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and (mainboard[y-1][x+1]=="o" or mainboard[y-1][x+1]=="O"):
								two_x.append(key)

						c3_dama_coordinates=[]
						for until in c_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O") and mainboard[yy-1][xx+1]=="-" and (mainboard[yy+1][xx-1]!="o" and mainboard[yy+1][xx-1]!="O"):
								c3_dama_coordinates.append(until)		
						if len(two_x)>0 and len(c3_dama_coordinates)>0:
							extract_x = two_x[0] #coz two_x is a list not a numeric value
							a = c_dama_coordinates[extract_x][0]
							b = c_dama_coordinates[extract_x][1]
							xxx = c3_dama_coordinates[len(c3_dama_coordinates)-1][0]
							yyy = c3_dama_coordinates[len(c3_dama_coordinates)-1][1]
							if a>k_x2 and k_x2>xxx and b<k_y2 and k_y2<yyy:
								while temp_x1<k_x2 and temp_y1>k_y2: #UPPER RIGHT
									if (mainboard[temp_y1-1][temp_x1+1]=="-") and (mainboard[temp_y1][temp_x1]=="o" or mainboard[temp_y1][temp_x1]=="O"):
										mainboard[temp_y1][temp_x1]="-"
									temp_y1-=1
									temp_x1+=1

								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="X"
									two_x.clear()
									c3_dama_coordinates.clear()
									c_dama_coordinates.clear()
									dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								c3_dama_coordinates.clear()
								l_x1,l_y1 = constant_x,constant_y

						elif len(two_x)>0 and len(c3_dama_coordinates)==0: 
							extract_x = two_x[0]
							a,b = c_dama_coordinates[extract_x][0],c_dama_coordinates[extract_x][1]
							if a>k_x2 and k_x2>temp_x1 and b<k_y2 and k_y2<temp_y1:		
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="X"
								two_x.clear()
								c3_dama_coordinates.clear()
								c_dama_coordinates.clear()
								count-=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
							else:
								print("Invalid move")
								l_x1,l_y1 = constant_x,constant_y
						else:
							c2_dama_coordinates = {}
							c2_key = 1
							for key,value in c_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="x" or mainboard[y][x]=="X":
									break
								else:
									if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and mainboard[y-1][x+1]=="-" and mainboard[k_y2][k_x2]=="-":
										c2_dama_coordinates[c2_key] = value
										c2_key+=1
							if len(c2_dama_coordinates)!=0:
								a = c2_dama_coordinates[len(c2_dama_coordinates)][0]
								b = c2_dama_coordinates[len(c2_dama_coordinates)][1]					
								if k_x2>a and k_y2<b:	
									for coordinates in c2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1] 
										mainboard[b][a]="-" 
									else:
										mainboard[k_y2][k_x2]="X"
										mainboard[constant_y][constant_x]="-"
										c_dama_coordinates.clear()
										c2_dama_coordinates.clear()
										c3_dama_coordinates.clear()
										l_x1,l_y1,c2_key = constant_x,constant_y,1
										dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									c2_dama_coordinates.clear()
									c3_dama_coordinates.clear()
									c_dama_coordinates.clear()
									l_x1,l_y1,c2_key = constant_x,constant_y,1
							else:
								if [k_x2,k_y2] in c_dama_coordinates.values():
									mainboard[k_y2][k_x2]="X"
									mainboard[constant_y][constant_x]="-"
									count-=1
									c2_dama_coordinates.clear()
									c_dama_coordinates.clear()
									c3_dama_coordinates.clear()
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)



				elif constant_x>k_x2 and constant_y<k_y2:
					d_dama_coordinates = {}
					temp_x1 = l_x1
					temp_y1 = l_y1
					key = 0
					while l_x1!=-1 and l_y1!=10: #lower-left
						ordered_pair = [l_x1,l_y1]
						d_dama_coordinates[key] = ordered_pair
						l_x1-=1
						l_y1+=1
						key+=1
					else:
						if [k_x2,k_y2] not in d_dama_coordinates.values():
							print("Invalid move, not in diagonal")
							l_x1,l_y1 = constant_x, constant_y
							d_dama_coordinates.clear()
							dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						d_dama_coordinates.pop(0)

						d4_dama_coordinates = []
						for until in d_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="x" or mainboard[yy][xx]=="X"):
								d4_dama_coordinates.append(until)
								break
						if len(d4_dama_coordinates)!=0:
							aa = d4_dama_coordinates[0][0]
							bb = d4_dama_coordinates[0][1]
							if temp_x1>k_x2 and temp_y1<k_y2 and k_x2>aa and k_y2<bb:
								pass
							else:
								print(l_x1,l_y1)
								print("Invalid move!")
								d4_dama_coordinates.clear()
								l_x1 = constant_x
								l_y1 = constant_y
								dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
						d4_dama_coordinates.clear()
						l_x1 = constant_x
						l_y1 = constant_y
						two_x = [] #where 2x's will appear (invalid to move below its coordinates)
						for key,value in d_dama_coordinates.items():
							x,y = value[0],value[1] 
							if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and (mainboard[y+1][x-1]=="o" or mainboard[y+1][x-1]=="O"):
								two_x.append(key)

						d3_dama_coordinates = []
						for until in d_dama_coordinates.values():
							xx,yy = until[0],until[1]
							if (mainboard[yy][xx]=="o" or mainboard[yy][xx]=="O") and mainboard[yy+1][xx-1]=="-" and (mainboard[yy-1][xx+1]!="o" and mainboard[yy-1][xx+1]!="O"):
								d3_dama_coordinates.append(until)

						if len(two_x)>0 and len(d3_dama_coordinates)>0:
							extract_x = two_x[0]
							a,b = d_dama_coordinates[extract_x][0],d_dama_coordinates[extract_x][1]
							xxx = d3_dama_coordinates[len(d3_dama_coordinates)-1][0]
							yyy = d3_dama_coordinates[len(d3_dama_coordinates)-1][1]

							if a<k_x2 and k_x2<xxx and b>k_y2 and k_y2>yyy:
								while temp_x1>k_x2 and temp_y1<k_y2: #lower left1
									if mainboard[temp_y1+1][temp_x1-1]=="-" and (mainboard[temp_y1][temp_x1]=="o" or mainboard[temp_y1][temp_x1]=="O") and (mainboard[temp_y1-1][temp_x1+1]!="o" or mainboard[temp_y1-1][temp_x1+1]!="O"):
										mainboard[temp_y1][temp_x1]="-"
									temp_y1+=1
									temp_x1-=1
								else:
									mainboard[constant_y][constant_x]="-"
									mainboard[k_y2][k_x2]="X"
									two_x.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()
									dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

							else:
								print("Invalid move!")
								l_x1,l_y1 = constant_x,constant_y

						elif len(two_x)>0 and len(d3_dama_coordinates)==0:
							extract_x = two_x[0]
							a,b = d_dama_coordinates[extract_x][0],d_dama_coordinates[extract_x][1]
							if a<k_x2 and k_x2<temp_x1 and b>k_y2 and k_y2>temp_y1:
								mainboard[constant_y][constant_x]="-"
								mainboard[k_y2][k_x2]="X"
								two_x.clear()
								d_dama_coordinates.clear()
								d3_dama_coordinates.clear()
								d2_dama_coordinates.clear()
								count-=1
								move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

							else:
								print("Invalid move!")
								l_x1,l_y1 = constant_x,constant_y
						else:
							d2_dama_coordinates = {}
							d2_key = 1
							for key,value in d_dama_coordinates.items():
								x,y = value[0],value[1]
								if mainboard[y][x]=="x" or mainboard[y][x]=="X":
									break
								else:
									if (mainboard[y][x]=="o" or mainboard[y][x]=="O") and mainboard[y+1][x-1]=="-" and mainboard[k_y2][k_x2]=="-":
										d2_dama_coordinates[d2_key] = value
										d2_key+=1
							if len(d2_dama_coordinates)!=0:
								a = d2_dama_coordinates[len(d2_dama_coordinates)][0]
								b = d2_dama_coordinates[len(d2_dama_coordinates)][1]
								
								if k_x2<a and k_y2>b:
									for coordinates in d2_dama_coordinates.values():
										a,b = coordinates[0],coordinates[1]
										mainboard[b][a]="-"
									else:
										mainboard[k_y2][k_x2]="X"
										mainboard[constant_y][constant_x]="-"
										d_dama_coordinates.clear()
										d2_dama_coordinates.clear()
										l_x1,l_y1,d2_key = constant_x,constant_y,1
										d3_dama_coordinates.clear()
										d2_dama_coordinates.clear()
										dama_checker2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
								else:
									print("Take all available pieces")
									d2_dama_coordinates.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()

									l_x1,l_y1,d2_key = constant_x,constant_y,1
							else:
								if [k_x2,k_y2] in d_dama_coordinates.values():
									mainboard[k_y2][k_x2]="X"
									mainboard[constant_y][constant_x]="-"
									count-=1
									d2_dama_coordinates.clear()
									d_dama_coordinates.clear()
									d3_dama_coordinates.clear()
									move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("Invalid move, not in diagonal")
	


def checkerboard(mainboard): #prints the checkerboard
	print()
	for list_item in mainboard:
		for xx in list_item:	
			print(xx, end=" ")
		print()

def isDama2(mainboard): #for player 2
	for x_coordinates in range(0,9):
		if mainboard[9][x_coordinates]=="x":
			mainboard[9][x_coordinates]="X"
			break
def isDama1(mainboard): #for player 1
	for x_coordinates in range(1,10):
		if mainboard[0][x_coordinates]=="o":
			mainboard[0][x_coordinates]="O"
			break

def checker_take2_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board):
	while True:
		l_y1=int(l_y2) #swapping
		l_x1=int(l_x2) #swapping
		if (mainboard[l_y1-1][l_x1+1]=="o" or mainboard[l_y1-1][l_x1+1]=="O") and (mainboard[l_y1-2][l_x1+2]=="-"): #upper-right #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[x] Move to: ").split(",")
				l_x2,l_y2 = int(x2),int(y2)
				if (l_y1-2==l_y2) and (l_x1+2==l_x2):
					mainboard[l_y2][l_x2]="x"											
					mainboard[l_y1-1][l_x1+1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama2(mainboard)
					break
				else:
					print("Take the opponent's piece first!")
		elif (mainboard[l_y1+1][l_x1+1]=="o" or mainboard[l_y1+1][l_x1+1]=="O") and (mainboard[l_y1+2][l_x1+2]=="-"): #lower-right #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[x] Move to: ").split(",")
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1+2==l_y2) and (l_x1+2==l_x2):
					mainboard[l_y2][l_x2]="x"
					mainboard[l_y1+1][l_x1+1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama2(mainboard)
					break
				else:
					print("Take the opponent's piece first!")

		elif (mainboard[l_y1-1][l_x1-1]=="o" or mainboard[l_y1-1][l_x1-1]=="O") and (mainboard[l_y1-2][l_x1-2]=="-"): #upper-left #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[x] Move to: ").split(",")
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1-2==l_y2) and (l_x1-2==l_x2):
					mainboard[l_y2][l_x2]="x"
					mainboard[l_y1-1][l_x1-1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama2(mainboard)
					break
				else:
					print("Take the opponent's piece first!")

		elif (mainboard[l_y1+1][l_x1-1]=="o" or mainboard[l_y1+1][l_x1-1]=="O") and (mainboard[l_y1+2][l_x1-2]=="-"): #lower-left #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[x] Move to: ").split(",") 
				l_x2 = int(x2)
				l_y2 = int(y2)
				if ((l_y1+2==l_y2) and (l_x1-2==l_x2)):  
					mainboard[l_y2][l_x2]="x"
					mainboard[l_y1+1][l_x1-1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama2(mainboard)
					break
				else:
					print("Invalid coordinates!")
		else:
			count-=1
			move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)

def checker_take_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board):
	while True:
		l_y1=int(l_y2) #swapping
		l_x1=int(l_x2) #swapping
		if (mainboard[l_y1-1][l_x1+1]=="x" or mainboard[l_y1-1][l_x1+1]=="X") and (mainboard[l_y1-2][l_x1+2]=="-"): #upper-right #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[o] Move to: ").split(",")				
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1-2!=l_y2) and (l_x1+2!=l_x2):
					print("Take the opponent's piece first!")
				else:
					mainboard[l_y2][l_x2]="o"											
					mainboard[l_y1-1][l_x1+1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama1(mainboard)
					break
		elif (mainboard[l_y1+1][l_x1+1]=="x" or mainboard[l_y1+1][l_x1+1]=="X") and (mainboard[l_y1+2][l_x1+2]=="-"): #lower-right #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[o] Move to: ").split(",")
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1+2!=l_y2) and (l_x1+2!=l_x2):
					print("Take the opponent's piece first!")
				else:
					mainboard[l_y2][l_x2]="o"
					mainboard[l_y1+1][l_x1+1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama1(mainboard)
					break
		elif (mainboard[l_y1-1][l_x1-1]=="x" or mainboard[l_y1-1][l_x1-1]=="X") and (mainboard[l_y1-2][l_x1-2]=="-"): #upper-left #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[o] Move to: ").split(",")
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1-2!=l_y2) and (l_x1-2!=l_x2):
					print("Take the opponent's piece first!")
				else:
					mainboard[l_y2][l_x2]="o"
					mainboard[l_y1-1][l_x1-1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama1(mainboard)
					break

		elif (mainboard[l_y1+1][l_x1-1]=="x" or mainboard[l_y1+1][l_x1-1]=="X") and (mainboard[l_y1+2][l_x1-2]=="-"): #lower-left #correct
			checkerboard(mainboard)
			while True:
				x2,y2 = input("[o] Move to: ").split(",") 
				l_x2 = int(x2)
				l_y2 = int(y2)
				if (l_y1+2!=l_y2) and (l_x1-2!=l_x2):  
					print("Invalid coordinates!")
				else:
					mainboard[l_y2][l_x2]="o"
					mainboard[l_y1+1][l_x1-1]="-"
					mainboard[l_y1][l_x1]="-"
					isDama1(mainboard)
					break
		else:
			count+=1
			move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)


def move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	while True:
		if count==0:
			check_player1(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2)
			check_player2(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2)
			checkerboard(mainboard)
			must_first = {} #ordered pair having "mandatory" taking opponent's piece 
			must_second = {} #ordered pair where it must land 
			must_key = 1 #what key number, important for connecting must_first and must_second
			for y in range(0,10):
				for x in range(0,10):
					if mainboard[y][x]=="o":
						if (mainboard[y-1][x+1]=="x" or mainboard[y-1][x+1]=="X") and mainboard[y-2][x+2]=="-": #upper-right						
							must_first[must_key] = [x,y] #it detects which coordinates this player should select first
							must_second[must_key] = [x+2,y-2] #it detects which coordinates this player should move his first ordered pair
							must_key+=1 #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y-1][x-1]=="x" or mainboard[y-1][x-1]=="X") and mainboard[y-2][x-2]=="-": #upper-left
							must_first[must_key] = [x,y] #it detects which coordinates this player should select first
							must_second[must_key] = [x-2,y-2] #it detects which coordinates this player should move his first ordered pair
							must_key+=1 #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y+1][x-1]=="x" or mainboard[y+1][x-1]=="X") and mainboard[y+2][x-2]=="-": #lower-left						
							must_first[must_key] = [x,y] #it detects which coordinates this player should select first
							must_second[must_key] = [x-2,y+2] #it detects which coordinates this player should move his first ordered pair
							must_key+=1 #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y+1][x+1]=="x" or mainboard[y+1][x+1]=="X") and mainboard[y+2][x+2]=="-": #lower-right						   
							must_first[must_key] = [x,y] #it detects which coordinates this player should select first
							must_second[must_key] = [x+2,y+2] #it detects which coordinates this player should move his first ordered pair
							must_key+=1 #connecting two dictionaries (have same int key for dictionary)
			while True: 
				try:
					x1,y1 = input("\n[o] Player 1: ").split(",") #player 1's first input coordinate
				except: #if error occur, message will pop-up saying continue to play or save (how to save) // typing any string
					print("\n\t\t ------------------------------------------------")
					print("\t\t\t\t [1] Save                                   ")
					print("\t\t\t\t [2] Continue playing						")
					print("\t\t ------------------------------------------------")
					choice = int(input("\n\t\t\t\t  Enter choice: "))
					if choice==1:	
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Select valid choice")
				else:
					l_x1 = int(x1) #string to int
					l_y1 = int(y1) #string to int
					if mainboard[l_y1][l_x1]!="o" and mainboard[l_y1][l_x1]!="O":
						print("Ooops! Check your coordinates!") 
					elif (0>l_x1 or l_x1>9) or (0>l_y1 or l_y1>9): #out of range
						print("Ooops! Coordinates are out of range.")
					elif len(must_first)>0: #if must_first contains an ordered pair, player should select any of that existing ordered pair, else ....
						if [l_x1,l_y1] not in must_first.values():
							print("Please take the opponent's piece first!")
						else:							
							break


					elif mainboard[l_y1][l_x1]=="o": #detects trap movement
						if l_x1==0:
							if (mainboard[l_y1-1][1]=="o" or mainboard[l_y1-1][1]=="O") or ((mainboard[l_y1-1][1]=="x" or mainboard[l_y1-1][1]=="X") and (mainboard[l_y1-2][2]!="-")):
								print("Invalid move") #trap in upper-right 
							else:
								break
						elif l_x1==9:
							if (mainboard[l_y1-1][8]=="o" or mainboard[l_y1-1][8]=="O") or ((mainboard[l_y1-1][8]=="x" or mainboard[l_y1-1][8]=="X") and (mainboard[l_y1-2][7]!="-")):
								print("Invalid move") #trap in upper-left
							else:
								break
						#middle two-way	(o/O in front)	
						elif (mainboard[l_y1-1][l_x1+1]=="o" or mainboard[l_y1-1][l_x1+1]=="O") and (mainboard[l_y1-1][l_x1-1]=="o" or mainboard[l_y1-1][l_x1-1]=="O"):
							if ((mainboard[l_y1+1][l_x1+1]=="x" or mainboard[l_y1+1][l_x1+1]=="X") and (mainboard[l_y1+2][l_x1+2]=="-")) or ((mainboard[l_y1+1][l_x1-1]=="x" or mainboard[l_y1+1][l_x1-1]=="X") and (mainboard[l_y1+2][l_x1-2]=="-")):
								break #eating backwards if trap (in front)
							else:
								print("Invalid choice")

						elif ((mainboard[l_y1-1][l_x1+1]=="x" or mainboard[l_y1-1][l_x1+1]=="X") and (mainboard[l_y1-2][l_x1+2]=="x" or mainboard[l_y1-2][l_x1+2]=="X")) and ((mainboard[l_y1-1][l_x1-1]=="x" or mainboard[l_y1-1][l_x1-1]=="X") and (mainboard[l_y1-2][l_x1-2]=="x" or mainboard[l_y1-2][l_x1-2]=="X")):
							if ((mainboard[l_y1+1][l_x1+1]=="x" or mainboard[l_y1+1][l_x1+1]=="X") and (mainboard[l_y1+2][l_x1+2]=="-")) or ((mainboard[l_y1+1][l_x1-1]=="x" or mainboard[l_y1+1][l_x1-1]=="X") and (mainboard[l_y1+2][l_x1-2]=="-")):
								break #if there are two-X's in both sideways, it checks the back sideways if it is valid to move(eat) 
							else:
								print("Invalid Choice")
						
						#x/X only in 1st block diagonally and "-" in second block diagonally (valid eating) - it falls in else statement
						else:
							break


					elif mainboard[l_y1][l_x1]=="O":
						dama(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					
					else:
						print("Invalid coordinates!")

			while True:
				try:
					x2,y2 = input("[o] Move to: ").split(",") #player's 1 second cooridinate input (where to move)
				except:
					print("\n\t\t ------------------------------------------------")
					print("\t\t\t\t [1] Save                                   ")
					print("\t\t\t\t [2] Continue playing						")
					print("\t\t ------------------------------------------------")
					choice = int(input("\n\t\t\t\t  Enter choice: "))
					if choice==1:	
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Select valid choice!")
				else:
					l_x2 = int(x2) #converting string to int
					l_y2 = int(y2) #converting string to int
					if (0>l_x2 or l_x2>9) or (0>l_y2 or l_y2>9): #out of range
						print("Ooops! Coordinates out of range.")
					elif mainboard[l_y2][l_x2]!="-":
						print("Oooops! Invalid move!")	
					elif len(must_first)>0: #this player should take opponent's piece first
						if [l_x1,l_y1] in must_first.values() and [l_x2,l_y2] in must_second.values():
							if l_y2>l_y1: #moving backwards
								#valid eating (lower-right side) --> moving backwards
								if l_y1+2==l_y2 and l_x1+2==l_x2 and mainboard[l_y1+2][l_x1+2]=="-" and (mainboard[l_y1+1][l_x1+1]=="x" or mainboard[l_y1+1][l_x1+1]=="X"):
									mainboard[l_y2][l_x2]="o" 
									mainboard[l_y1+1][l_x1+1]="-"
									mainboard[l_y1][l_x1]="-"
									must_first.clear() #clear - to clean every time the dictionary (valid or invalid)
									must_second.clear() #clear - to clean every time the dictionary (valid or invalid)
									must_key = 1 #reassignment back to 1 - reset to default
									checker_take_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board) 
								#valid eating (lower-left side) --> moving backwards
								elif l_y1+2==l_y2 and l_x1-2==l_x2 and mainboard[l_y1+2][l_x1-2]=="-" and (mainboard[l_y1+1][l_x1-1]=="x" or mainboard[l_y1+1][l_x1-1]=="X"):
									mainboard[l_y2][l_x2]="o" 
									mainboard[l_y1+1][l_x1-1]="-"
									mainboard[l_y1][l_x1]="-"
									must_first.clear() #clear - to clean every time the dictionary (valid or invalid)
									must_second.clear()#clear - to clean every time the dictionary (valid or invalid)
									must_key = 1 #reassignment back to 1 - reset to default
									checker_take_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
								else:
									print("Invalid move!")
									break
							
							#valid eating (right-side) ---> moving forward
							elif ((l_y1-2==l_y2) and (l_x1+2==l_x2) and (mainboard[l_y1-1][l_x1+1]=="x" or mainboard[l_y1-1][l_x1+1]=="X") and (mainboard[l_y2][l_x2]=="-")): 
								mainboard[l_y2][l_x2]="o"
								mainboard[l_y1-1][l_x1+1]="-"
								mainboard[l_y1][l_x1]="-"   
								must_first.clear() #clear - to clean every time the dictionary (valid or invalid)
								must_second.clear()#clear - to clean every time the dictionary (valid or invalid)
								must_key = 1 #reassignment back to 1 - reset to default
								isDama1(mainboard)
								checker_take_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)

							#valid eating (left-side) ---> moving forward
							elif ((l_y1-2==l_y2) and (l_x1-2==l_x2) and (mainboard[l_y1-1][l_x1-1]=="x" or mainboard[l_y1-1][l_x1-1]=="X") and (mainboard[l_y2][l_x2]=="-")): 
								mainboard[l_y2][l_x2]="o"
								mainboard[l_y1-1][l_x1-1]="-"
								mainboard[l_y1][l_x1]="-"
								must_first.clear() #clear - to clean every time the dictionary (valid or invalid)
								must_second.clear()#clear - to clean every time the dictionary (valid or invalid)
								must_key = 1 #reassignment back to 1 - reset to default
								isDama1(mainboard) #checks if the player is dama (king) already  or not 
								checker_take_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
							else:
								print("Invalid move!")
						else:
							print("Please take opponent's piece first!")
							
					#moving forward only - not eating/taking opponent's piece
					elif ((l_x1+1==l_x2 and l_y1-1==l_y2) or (l_x1-1==l_x2 and l_y1-1==l_y2)) and (mainboard[l_y2][l_x2]=="-"): 
						mainboard[l_y2][l_x2]="o"   
						mainboard[l_y1][l_x1]="-" 	
						count+=1
						isDama1(mainboard)
						break				
					else: 
						print("Oooops! Invalid move!")
					
				isDama1(mainboard)
			
		#player 2's turn or count==1
		else:
			check_player1(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2)
			check_player2(mainboard,count,score_p2,score_p1,new_board,l_x1,l_y1,l_x2,l_y2)
			checkerboard(mainboard)
			must_first2 = {} #if this player has the coordinates to be moved first for mandatory taking/eating
			must_second2 = {} #if this player has the coordinates to be moved first for mandatory taking/eating
			must_key2 = 1 #connecting two dictionaries later on (must_first2 and must_second2)
			for y in range(0,10):
				for x in range(0,10):
					if mainboard[y][x]=="x":
						if (mainboard[y-1][x+1]=="o" or mainboard[y-1][x+1]=="O") and mainboard[y-2][x+2]=="-": #upper-right						
							must_first2[must_key2] = [x,y] #it detects which coordinates this player should select first
							must_second2[must_key2] = [x+2,y-2] #it detects which coordinates this player should move his first ordered pair
							must_key2+=1  #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y-1][x-1]=="o" or mainboard[y-1][x-1]=="O") and mainboard[y-2][x-2]=="-": #upper-left
							must_first2[must_key2] = [x,y] #it detects which coordinates this player should select first
							must_second2[must_key2] = [x-2,y-2] #it detects which coordinates this player should move his first ordered pair
							must_key2+=1 #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y+1][x-1]=="o" or mainboard[y+1][x-1]=="O") and mainboard[y+2][x-2]=="-": #lower-left						
							must_first2[must_key2] = [x,y] #it detects which coordinates this player should select first
							must_second2[must_key2] = [x-2,y+2] #it detects which coordinates this player should move his first ordered pair
							must_key2+=1 #connecting two dictionaries (have same int key for dictionary)
						if (mainboard[y+1][x+1]=="o" or mainboard[y+1][x+1]=="O") and mainboard[y+2][x+2]=="-": #lower-right						   
							must_first2[must_key2] = [x,y] #it detects which coordinates this player should select first
							must_second2[must_key2] = [x+2,y+2] #it detects which coordinates this player should move his first ordered pair
							must_key2+=1 #connecting two dictionaries (have same int key for dictionary)
			while True:
				try:
					x1,y1 = input("\n[x] Player 2: ").split(",")
				except:	
					print("\n\t\t ------------------------------------------------")
					print("\t\t\t\t [1] Save                                   ")
					print("\t\t\t\t [2] Continue playing						")
					print("\t\t ------------------------------------------------")
					choice = int(input("\n\t\t\t\t  Enter choice: "))
					if choice==1:	
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Select valid choice!")
				else:
					l_x1 = int(x1)
					l_y1 = int(y1)
					if (0>l_x1 or l_x1>9) or (0>l_y1 or l_y1>9):
						print("Ooops! Coordinates are out of range.")
					elif mainboard[l_y1][l_x1]!="x" and mainboard[l_y1][l_x1]!="X":
						print("Oooops! Player2, move your own pieces only!")
					elif len(must_first2)>0: #this player should take opponent's piece first
						if [l_x1,l_y1] not in must_first2.values():
							print("Please take the opponent's piece first!")
						else:
							break
					elif mainboard[l_y1][l_x1]=="x": #trap
						if l_x1==0:
							if (mainboard[l_y1+1][1]=="x" or mainboard[l_y1+1][1]=="X") or ((mainboard[l_y1+1][1]=="o" or mainboard[l_y1+1][1]=="O") and (mainboard[l_y1+2][2]!="-")):
								print("Invalid move") #
							else: 
								break
						elif l_x1==9:
							if (mainboard[l_y1+1][8]=="x" or mainboard[l_y1+1][8]=="X") or ((mainboard[l_y1+1][8]=="o" or mainboard[l_y1+1][8]=="O") and (mainboard[l_y1+2][7]!="-")):
								print("Invalid move")
							else:
								break
						elif (mainboard[l_y1+1][l_x1+1]=="x" or mainboard[l_y1+1][l_x1+1]=="X") and (mainboard[l_y1+1][l_x1-1]=="x" or mainboard[l_y1-1][l_x1-1]=="X"):
							if ((mainboard[l_y1-1][l_x1+1]=="o" or mainboard[l_y1-1][l_x1+1]=="O") and (mainboard[l_y1-2][l_x1+2]=="-")) or ((mainboard[l_y1-1][l_x1-1]=="o" or mainboard[l_y1-1][l_x1-1]=="O") and (mainboard[l_y1-2][l_x1-2]=="-")):
								break
							else:
								print("Invalid choice")

						elif ((mainboard[l_y1+1][l_x1+1]=="o" or mainboard[l_y1+1][l_x1+1]=="O") and (mainboard[l_y1+2][l_x1+2]=="o" or mainboard[l_y1+2][l_x1+2]=="O")) and ((mainboard[l_y1+1][l_x1-1]=="o" or mainboard[l_y1+1][l_x1-1]=="O") and (mainboard[l_y1+2][l_x1-2]=="o" or mainboard[l_y1+2][l_x1-2]=="O")):
							if ((mainboard[l_y1-1][l_x1+1]=="o" or mainboard[l_y1-1][l_x1+1]=="O") and (mainboard[l_y1-2][l_x1+2]=="-")) or ((mainboard[l_y1-1][l_x1-1]=="o" or mainboard[l_y1-1][l_x1-1]=="O") and (mainboard[l_y1-2][l_x1-2]=="-")):
								break
							else:
								print("Invalid Choice")
						else:
							break


					elif mainboard[l_y1][l_x1]=="X":
						dama2(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)			
					else:
						print("Invalid coordinates!")
			while True:
				try: 
					x2,y2 = input("[x] Move to: ").split(",")
				except:
					print("\n\t\t ------------------------------------------------")
					print("\t\t\t\t [1] Save                                   ")
					print("\t\t\t\t [2] Continue playing						")
					print("\t\t ------------------------------------------------")
					choice = int(input("\n\t\t\t\t  Enter choice: "))
					if choice==1:	
						save(mainboard,count,score_p2,score_p1)
						exit()
					elif choice==2:
						move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
					else:
						print("Select valid choice!")
				else:
					l_x2 = int(x2)
					l_y2 = int(y2)
					if (0>l_x2 or l_x2>9) or (0>l_y2 or l_y2>9):
						print("Ooops! Coordinates out of range.")
					elif mainboard[l_y2][l_x2]!="-":
						print("Oooops! Invalid move!")			
					elif len(must_first2)>0:
						for must_first_index in must_first2.keys():
							if [l_x1,l_y1] in must_first2.values() and [l_x2,l_y2] in must_second2.values():
								if l_y2<l_y1: #moving backwards
									#valid eating (lower-right) --> moving backwards
									if ((l_y1-2==l_y2 and l_x1+2==l_x2) and (mainboard[l_y2][l_x2]=="-") and (mainboard[l_y1-1][l_x1+1]=="o" or mainboard[l_y1-1][l_x1+1]=="O")):
										mainboard[l_y2][l_x2]="x" 
										mainboard[l_y1-1][l_x1+1]="-" 
										mainboard[l_y1][l_x1]="-" 
										must_first2.clear()
										must_second2.clear()
										must_key2 = 1
										isDama2(mainboard)
										checker_take2_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
									#valid eating (lower left) ---> moving backwards
									elif (l_y1-2==l_y2 and l_x1-2==l_x2) and (mainboard[l_y2][l_x2]=="-") and (mainboard[l_y1-1][l_x1-1]=="o" or mainboard[l_y1-1][l_x1-1]=="O"):
										mainboard[l_y2][l_x2]="x" 
										mainboard[l_y1-1][l_x1-1]="-" 
										mainboard[l_y1][l_x1]="-"  
										must_first2.clear()
										must_second2.clear()
										must_key2 = 1
										isDama2(mainboard)
										checker_take2_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
									else:
										print("Invalid move!")
										break
								#valid eating (upper-right)---> moving forward
								elif ((l_y1+2==l_y2) and (l_x1+2==l_x2) and (mainboard[l_y1+1][l_x1+1]=="o" or mainboard[l_y1+1][l_x1+1]=="O") and (mainboard[l_y2][l_x2]=="-")): 
									mainboard[l_y2][l_x2]="x"
									mainboard[l_y1+1][l_x1+1]="-"
									mainboard[l_y1][l_x1]="-"
									must_first2.clear()
									must_second2.clear()
									must_key2 = 1
									isDama2(mainboard)
									checker_take2_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
								
								#valid eating (upper-left) ---- moving forward
								elif ((l_y1+2==l_y2) and (l_x1-2==l_x2) and (mainboard[l_y1+1][l_x1-1]=="o" or mainboard[l_y1+1][l_x1-1]=="O") and (mainboard[l_y2][l_x2]=="-")): 
									mainboard[l_y2][l_x2]="x"
									mainboard[l_y1+1][l_x1-1]="-"
									mainboard[l_y1][l_x1]="-"
									must_first2.clear()
									must_second2.clear()
									must_key2 = 1
									isDama2(mainboard)
									checker_take2_after(mainboard,l_x1,l_y1,l_x2,l_y2,count,score_p2,score_p1,new_board)
								else:
									print("Invalid move!")
							else:
								print("Please take opponent's piece first!")
								break									
					 #moving forward only (no eating/taking opponent's piece)
					elif ((l_x1+1==l_x2 and l_y1+1==l_y2) or (l_x1-1==l_x2 and l_y1+1==l_y2)) and (mainboard[l_y2][l_x2]=="-"): 
						mainboard[l_y2][l_x2]="x"   
						mainboard[l_y1][l_x1]="-"
						isDama2(mainboard)
						count-=1
						break
					else: 
						print("Oooops! Invalid move!")
				isDama2(mainboard)
def players_turn(count, mainboard,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	count=0
	while True: 
			print("\n\n\t\t\t\t[1] Player 1")
			print("\t\t\t\t[2] Player 2\n")
			try:
				who = int(input("\t\t\t     Who goes first?: "))
			except:
				print("\n\t\t     Enter a valid corresponding integer!")
			else:
				if who==1:
					move_player(mainboard, count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				elif who==2:
					count+=1
					move_player(mainboard, count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board)
				else:
					print("\n\t\t\t   Enter a valid choice!")
def menu_display():
	print("\n\t\t\t      C H E C K E R S")
	print("\t" + " ------------------------------------------------------------------")
	print("\t" + " " + "[1] How to play" + "  " + "[2] Play" + "  " + "[3] Save" + " " + "[4] Load" + " "+ " [5] Scores" + " "+ " [0] Exit")
	print("\t" + " ------------------------------------------------------------------")
def save(mainboard,count,score_p2,score_p1):
	file_name = input("\nFile name: ")
	saving_file = open(file_name, "a")
	for y in range(len(mainboard)): #SEPERATED BY "SPACE"
		saving_file.write(mainboard[y][0] + " " + mainboard[y][1] + " "+ mainboard[y][2] + " "+ mainboard[y][3] + " "+ mainboard[y][4] + " "+ mainboard[y][5] + " "+ mainboard[y][6] + " "+ mainboard[y][7] + " "+ mainboard[y][8] + " "+ mainboard[y][9] + " "+ mainboard[y][10] + " " + str(count) + " " + str(score_p1)+ " " + str(score_p2) + "\n")
	print("Saved!")
	saving_file.close()

def load(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board):
	file_name = input("File name: ")
	try:
		loading_file = open(file_name, "r")
		selected = loading_file.readlines()[-11:] #based on stackoverflow - getting last n lines from files
		#last 11 lines because that's the updated part of the game (current game/position)
		#https://stackoverflow.com/questions/37227909/print-last-line-of-file-read-in-with-python
	except:
		print("\n\n **** File not found! *****") #file not found error
	else:
		mainboard.clear() #clearing the board above, replacing the current position from the file
		indi = []
		for y_axis in selected: #Y-AXIS REPRESENTS THE "PER LINE" FROM THE FILES
			indi = y_axis.split(" ") #seperated by spaces (save function)
			indi2 = indi[:-3] #0 to -2 (-2 is the y-axis coordinates numbers)
			count = int(indi[-3]) #-3 is the "turn" number
			mainboard.append(indi2)
		loading_file.close() #avoid data loss
		move_player(mainboard,count,l_x1, l_y1,l_x2,l_y2,score_p2,score_p1,new_board) #then game na ulet
def score(score_p1,score_p2):
	file_name = input("File name: ")
	try:
		loading_file = open(file_name, "r")
	except:
		print("\n\n **** File does not exist ****")
	else:
		for scores in loading_file:
			scores_split = scores.split(" ") 
			score_p1 = scores_split[-2] #score of player 1
			score_p2 = scores_split[-1] #score of player 2
		print("Player 1: ", score_p1)
		print("Player 2: ", score_p2)
		loading_file.close() #avoid data loss





##################################### W H E R E    I T    A L L   G O T    S T A R T E D ##################################
local_x1=0
local_y1=0
local_x2=0
local_y2=0	
turn = 0
p1_score = 0
p2_score = 0
while True:
	menu_display()
	try:
		choice = int(input("\t\t\t\tSelect: "))
	except:
		print("\n\t\t     Enter a valid corresponding integer!")
	else:
		if choice==1:
			instruction()
		elif choice==2:
			players_turn(turn,board,local_x1, local_y1,local_x2,local_y2,p2_score,p1_score,consant_board)
		elif choice==3:
			save(board,turn,p2_score,p1_score)
		elif choice==4:
			load(board,turn,local_x1, local_y1,local_x2,local_y2,p2_score,p1_score,consant_board)
		elif choice==5:
			score(p1_score,p2_score)
		elif choice==0:
			exit()
		else:
			print("Invalid choice!")