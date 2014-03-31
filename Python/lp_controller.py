#!/user/bin/python

import sys, getopt, csv, os, glob

#from Simple.Taylor.Limb_Provement import generateCuts

def main(argv):
	i,o,p,a,l,b = False, False, False, False, False, False
	helpText = 'lp-controller.py [-i <inputFile>] [-o <outputFile>] -p <person> -a <algorithm>  [-l <Max Board Length>] [-b <Blade Width>]'

	inFile = ''
	outFile = ''
	person = ''
	algorithm = ''
	length = 8
	blade = 0
	cuts = []

	try:
		opts, args = getopt.getopt(argv, "hi:o:p:a:l:b",["help","iFile=","oFile=","person=","algo=","board=","blade="])
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

	if not (p and a):
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

	if i:
		# TODO read in input file and dispatch generateCuts
		print 'Input file is:', inFile
		with open(inFile, 'rb') as csvfile:
			cutReader = csv.reader(csvfile, delimiter=',')
			for row in cutReader:
				# TODO read in rows, concatenate
				cuts.extend(row)
		cuts = [int(c) for c in cuts]

	print "Unsorted:", cuts
	cuts.sort(reverse=True)
	print "Sorted:", cuts

	boards = cutter.generateCuts(length, blade, cuts)

	if o:
		print 'Output files is:', outFile



if __name__ == "__main__":
	main(sys.argv[1:])


