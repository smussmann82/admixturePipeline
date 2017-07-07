from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-m", "--popmap",
							dest='popmap',
							default="map.txt",
							help="Specify a tab-delimited population map (sample -> population)"
		)
		parser.add_argument("-v", "--vcf",
							dest='vcf',
							default="input.vcf",
							help="Specify a phylip file for input."
		)
		parser.add_argument("-o", "--out",
							dest='out',
							default="output.txt",
							help="Specify an output file name."
		)
		parser.add_argument("-w", "--window",
							dest='window',
							default=50,
							help="Window size for filtering in plink."
		)
		parser.add_argument("-a", "--advance",
							dest='advance',
							default=10,
							help="Value by which window is advanced when filtering in plink."
		)
		parser.add_argument("-r", "--rsquare",
							dest='rsquare',
							default=0.1,
							help="R^2 value for filtering in plink."
		)
		parser.add_argument("-f", "--filter",
							dest='filter',
							default=False,
							action='store_true',
							help="Turn on filtering in plink."
		)
		parser.add_argument("-k", "--minK",
							dest='minK',
							default=1,
							help="minimum K value."
		)
		parser.add_argument("-K", "--maxK",
							dest='maxK',
							default=20,
							help="maximum K value."
		)
		parser.add_argument("-n", "--np",
							dest='np',
							default=1,
							help="Number of processors."
		)
		parser.add_argument("-R", "--rep",
							dest='rep',
							default=20,
							help="Number of replicates per K."
		)
		
		self.args = parser.parse_args()

		#check if files exist
		#self.exists( self.args.popmap )
		self.exists( self.args.vcf )



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
