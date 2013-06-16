import glob
import pylab as pl
from numpy import genfromtxt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('data_summary.pdf')
plots = []
fig = pl.figure(figsize = (8,10))
for number,files in enumerate(glob.glob("*.csv")):
	data = genfromtxt(files,delimiter=",",skip_header=18)
	pl.subplot(4,2,(number%8)+1)
	pl.title(files)
	pl.plot(data[:,0],data[:,1])
	pl.tick_params(axis='both', labelsize=8)
	print "making plot ", number, ": ", files
	if (number+1)%8==0: 
		pl.tight_layout()
		pp.savefig()
		fig = pl.figure(figsize = (8,10))

pp.savefig()
pp.close()