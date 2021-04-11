#!/usr/bin/python

from distructComline import ComLine
from distruct import Distruct
from clumpp import Clumpp

import sys



def main():
	input = ComLine(sys.argv[1:])

	for k in range(int(input.args.mink),int(input.args.maxk)+1):
		drawp = "drawparams." + str(k)
		outfile = "K" + str(k) + ".ps"

		c = Clumpp(input.args.directory, str(k), input.args.ad)
		popq,indivq = c.copyMajClustFiles()
		popqList,indivqList = c.copyMinClustFiles()

		c.getMajorClusterRuns(input.args.majc)
		c.getMinorClusterRuns()

		c.getMajorClusterCVvalues(input.args.majc)
		c.getMinorClusterCVvalues()

		d = Distruct(input.args.directory, input.args.otl, input.args.colorbrew, input.args.pathtocolorbrew)
		d.copyFiles()

		d.writeDrawparams(drawp, popq, indivq, str(k), outfile, c.pops, c.inds, input.args.width)

		if input.args.run==True:
			d.runDistruct()

main()

raise SystemExit
