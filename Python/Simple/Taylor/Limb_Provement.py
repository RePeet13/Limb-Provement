def generateCuts(length, blade, cuts):
	print cuts
	outCuts = [[length, [] ]] # used, waste, cuts
	for c in cuts:
		if (c > length):
			print "Cut is longer than Length!",c," Exiting"
			return
		added = False
		for oc in outCuts:
			if c <= oc[0]:
				oc[0] = max(0, oc[0]-(c+blade) )
				oc[1].append(c)
				added = True
				break
		if not added:
			outCuts.append([length-c-blade, [c]])
	print "Success:"
	print outCuts


if (__name__ == "__main__"):

## Call Function ##

	mlength = 8
	mblade = 0
	mcuts = [5]
	generateCuts(mlength, mblade, mcuts)


## Testing ##

	print "Should be [[1,[1]]"
	generateCuts(2,0,[1])

	print "Should error"
	generateCuts(2,0,[3])
	
	print "Should be [[0.5,[1.5]],[0.5,[1.5]]]"
	generateCuts(2,0,[1.5,1.5])

