#!/user/bin/python

import sys, getopt, csv, os, glob

#from Simple.Taylor.Limb_Provement import generateCuts

def main(argv):
	i,f,o,p,a,l,b = False, False, False, False, False, False, False
	helpText = 'lp-controller.py -i <inputFile> [-f <input format>] [-o <outputFile>] [-p <person>] [-a <algorithm>]  [-l <Max Board Length>] [-b <Blade Width>]'

	inFile = ''
	inFormat = 1
	outFile = ''
	person = ''
	algorithm = ''
	length = 8
	blade = 0
	cuts = []

	try:
		opts, args = getopt.getopt(argv, "hi:f:o:p:a:l:b",["help","iFile=","form=","oFile=","person=","algo=","board=","blade="])
	except getopt.GetoptError:
		print helpText
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print helpText
			sys.exit()
		elif opt in ("-i", "--iFile"):
			i = True
			inFile = arg
		elif opt in ("-f", "--form"):
			f = True;
			inFormat = int(arg)
		elif opt in ("-o", "--oFile"):
			o = True
			outFile = arg
		elif opt in ("-p" , "--person"):
			p = True
			person = arg
		elif opt in ("-a", "--algorithm"):
			a = True
			algorithm = arg
		elif opt in ("-l", "--board"):
			l = True
			length = arg
		elif opt in ("-b", "--blade"):
			b = True
			blade = arg

	if not (i):
		print helpText
		sys.exit()

	# set path/module defaults
	path1, path2, path3 = "Simple", "Taylor", "Limb_Provement"

	if (algorithm.lower() == 'dp'):
		path1 = "DP"
	print "Setting algorithm to:", path1


	if (person.lower() in ("christa", "c")):
		path2 = "Christa"
	elif (person.lower() in ("julie", "j")):
		path2 = "Julie"
	print "Selecting", path2, "implementation"

	mName =	path1+"."+path2+"."+path3
	__import__(mName)
	cutter = sys.modules[mName]


	print 'Input file is:', inFile
	with open(inFile, 'rb') as csvfile:
		cutReader = csv.reader(csvfile, delimiter=',')
		if inFormat == 1:
			for row in cutReader:
				cuts.extend(row)
		elif inFormat == 2:
			for row in cutReader:
				cuts.extend(row[1] * int(row[0]))
	cuts = [int(c) for c in cuts]
				


#	print "Unsorted:", cuts
	cuts.sort(reverse=True)
	print "Sorted:", cuts

	boards = cutter.generateCuts(length, blade, cuts)

	if o:
		print 'Output files is:', outFile
		with open(outFile, 'wb') as csvfile:
			cutwriter = csv.writer(csvfile, delimiter=',')
			cutwriter.writerow(["Board","Waste","Cuts"])
			i=1
			for b in boards:
				row = [i,b[0]]
				row.extend(b[1])
				cutwriter.writerow(row)
				i+=1
	else:
		print boards

	sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])


