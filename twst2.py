#def spaces(n, y, t):
#    occupied = 0
#    for i in range(n):
#        if y[i] == "C" and t[i] == "C":
#            occupied += 1
#    return occupied

#print(spaces(30, "....C.CC...CCC.C.CC..C.....CC.", "C.CC.C...C..C..C...C..C..CCC.C"))



#def wizard(owner, N, duels):
#who owns the wand
    #last_owner = owner
#number of times changes
    #changes = 0
#check 1 single battle
#print(duels[0])
#check first character
#"""print(duels[0][0])"""
#check if wand changed hands

#wizard(3, "A", ["BA", "CB", "DA"])





def wizards(N, start, duels):
    owner = start
    num_owners = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            num_owners += 1
    print(owner, num_owners)

wizards(3, "A", ["BA", "CB", "DA"])