from __future__ import print_function

from shutil import copyfile

from syscall import SysCall

import os
import sys

class Distruct():
	'Class for preparing distruct output from the output produced by clumpak'

	def __init__(self,wd,otl,cb,ptcb):
		self.wd = wd
		self.nd = os.path.join(self.wd, "best_results")
		
		self.oldtoplabels = otl
		self.bottomlabels = "bottomlabels"
		self.toplabels = os.path.join(wd,self.oldtoplabels)

		#Check if file exists
		self.fileExists(self.toplabels)

		self.colorbrew = cb
		self.pathtocb = ptcb
		self.cbdict=self.makecbsuffixdict()

	def copyFiles(self):
		nf = os.path.join(self.nd, self.oldtoplabels)
		copyfile(self.toplabels,nf)

	def makedir(self,wd,d):
		if not os.path.exists(nd):
			os.makedirs(nd)

	def writeDrawparams(self,pfile, popq, indivq, k, outfile, pops, numind, width):
		drawp = os.path.join(self.nd, pfile)
		#popqdir = os.path.join(self.nd,popq)
		#indivqdir = os.path.join(self.nd,indivq)
		#topdir = os.path.join(self.nd,self.oldtoplabels)
		#btmdir = os.path.join(self.nd,self.oldbottomlabels)
		fh = open(drawp, 'w')
		fh.write("#define INFILE_POPQ ")
		fh.write(popq)
		fh.write("\n")
		fh.write("#define INFILE_INDIVQ ")
		fh.write(indivq)
		fh.write("\n")
		fh.write("#define INFILE_LABEL_BELOW ")
		fh.write(self.bottomlabels)
		fh.write("\n")
		fh.write("#define INFILE_LABEL_ATOP ")
		fh.write(self.oldtoplabels)
		fh.write("\n")
		#fh.write("#define INFILE_CLUST_PERM /home/mussmann/local/src/distruct1.1/ColorBrewer/BrBG_")
		fh.write("#define INFILE_CLUST_PERM ")
		fh.write(self.pathtocb)
		fh.write(self.colorbrew)
		fh.write("_")
		fh.write(k)
		fh.write("_")
		fh.write(self.cbdict[self.colorbrew])
		fh.write("\n")
		fh.write("#define OUTFILE ")
		fh.write(outfile)
		fh.write("\n")
		fh.write("#define K ")
		fh.write(k)
		fh.write("\n")
		fh.write("#define NUMPOPS ")
		fh.write(str(pops))
		fh.write("\n")
		fh.write("#define NUMINDS ")
		fh.write(str(numind))
		fh.write("\n")
		fh.write("#define PRINT_INDIVS 1\n")
		fh.write("#define PRINT_LABEL_ATOP 1\n")
		fh.write("#define PRINT_LABEL_BELOW 0\n")
		fh.write("#define PRINT_SEP 1\n")
		fh.write("#define FONTHEIGHT 6\n")
		fh.write("#define DIST_ABOVE -160\n")
		fh.write("#define DIST_BELOW -50\n")
		fh.write("#define BOXHEIGHT 150\n")
		fh.write("#define INDIVWIDTH ")
		fh.write(width)
		fh.write("\n")
		fh.write("#define ORIENTATION 1\n")
		fh.write("#define XORIGIN 200\n")
		fh.write("#define YORIGIN 10\n")
		fh.write("#define XSCALE 1\n")
		fh.write("#define YSCALE 1\n")
		fh.write("#define ANGLE_LABEL_ATOP 270\n")
		fh.write("#define ANGLE_LABEL_BELOW 270\n")
		fh.write("#define LINEWIDTH_RIM 3\n")
		fh.write("#define LINEWIDTH_SEP 1\n")
		fh.write("#define LINEWIDTH_IND 4\n")
		fh.write("#define GRAYSCALE 0\n")
		fh.write("#define ECHO_DATA 1\n")
		fh.write("#define REPRINT_DATA 1\n")
		fh.write("#define PRINT_INFILE_NAME 0\n")
		fh.write("#define PRINT_COLOR_BREWER 1\n")
		fh.close()

	def runDistruct(self):
		print("Now running distruct for all drawparams files...")
		contents = os.listdir(self.nd)
		
		os.chdir(self.nd)

		for f in contents:
			if f.startswith("drawparams"):
				distructCommand = "distruct -d " + str(f) + "; echo"
				call = SysCall(distructCommand)
				call.run_program()

		print("WARNING: Check that distruct ran properly.")
		print("This program does not check the exit status of DISTRUCT because its exit status always equals 1.")
		print("")

	def fileExists(self, filename):
		if( os.path.isfile(filename) != True ):
			print( filename, "does not exist" )
			print( "Exiting program..." )
			print( "" )
			raise SystemExit
		else:
			print(filename, "Exists")

	def makecbsuffixdict(self):
		cbdict = dict()
		cbdict["Accent"]="qual"
		cbdict["Blues"]="seq"
		cbdict["BrBG"]="div"
		cbdict["BuGn"]="seq"
		cbdict["BuPu"]="seq"
		cbdict["Dark2"]="qual"
		cbdict["GnBu"]="seq"
		cbdict["Greens"]="seq"
		cbdict["Greys"]="seq"
		cbdict["Oranges"]="seq"
		cbdict["OrRd"]="seq"
		cbdict["Paired"]="qual"
		cbdict["Pastel1"]="qual"
		cbdict["Pastel2"]="qual"
		cbdict["PiYG"]="div"
		cbdict["PRGn"]="div"
		cbdict["PuBuGn"]="seq"
		cbdict["PuBu"]="seq"
		cbdict["PuOr"]="div"
		cbdict["PuRd"]="seq"
		cbdict["Purples"]="seq"
		cbdict["RdBu"]="div"
		cbdict["RdGy"]="div"
		cbdict["RdPu"]="seq"
		cbdict["RdYlBu"]="div"
		cbdict["RdYlGn"]="div"
		cbdict["Reds"]="seq"
		cbdict["Set1"]="qual"
		cbdict["Set2"]="qual"
		cbdict["Set3"]="qual"
		cbdict["Spectral"]="div"
		cbdict["YlGnBu"]="seq"
		cbdict["YlGn"]="seq"
		cbdict["YlOrBr"]="seq"
		cbdict["YlOrRd"]="seq"

		return cbdict
