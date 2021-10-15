import random
ch = "y"
while ch == "y":
	a= random.randint(1,6) # random number is generated 
	
	if a== 1:
		print("[-----]")
		print("[   . ]")
		print("[ . . ]")
		print("[   . ]")
		print("[   . ]")
		print("[ ....]")
		print("[-----]")
		print("the number rolled is 1")
	elif a== 2:
		print("[-----]")
		print("[.....]")
		print("[    .]")
		print("[.....]")
		print("[.    ]")
		print("[.....]")
		print("[-----]")
		print("the number rolled is 2")
	elif a== 3:
		print("[-----]")
		print("[.....]")
		print("[    .]")
		print("[.....]")
		print("[    .]")
		print("[.....]")
		print("[-----]")
		print("the number rolled is 3")
	elif a== 4:
		print("[-----]")
		print("[.   .]")
		print("[.   .]")
		print("[.....]")
		print("[    .]")
		print("[    .]")
		print("[-----]")
		print("the number rolled is 4")
	elif a== 5:
		print("[-----]")
		print("[.....]")
		print("[.    ]")
		print("[.....]")
		print("[    .]")
		print("[.....]")
		print("[-----]")
		print("the number rolled is 5")
	else:
		print("[-----]")
		print("[.....]")
		print("[.    ]")
		print("[.....]")
		print("[.   .]")
		print("[.....]")
		print("[-----]")
		print("the number rolled is 6")
		
	ch=input("press y if you want to continue and n to stop:")
    #if input y than while loop executes again