import glob
import pylab as pl
from numpy import genfromtxt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('data_summary.pdf')
plots = []
index = [3,4,9,10]
secondplot = True
skiphead = 0
fig = pl.figure(figsize = (8,10))

def get_data_cols(input):
    # find max length columns, return list of indices with same length col
    return [3,4],False

for number,files in enumerate(glob.glob("*.csv")):
    data = genfromtxt(files,delimiter=",",skip_header=skiphead)
    datacols,secondplot = get_data_cols(data)
    pl.subplot(4,2,(number%8)+1)
    pl.title(files)
    pl.plot(data[:,datacols[0]],data[:,datacols[1]])
    if secondplot:
        pl.plot(data[:,datacols[2]],data[:,datacols[3]])
    pl.tick_params(axis='both', labelsize=8)
    print "making plot ", number, ": ", files
    if (number+1)%8==0: 
        pl.tight_layout()
        pp.savefig()
        fig = pl.figure(figsize = (8,10))

pp.savefig()
pp.close()
