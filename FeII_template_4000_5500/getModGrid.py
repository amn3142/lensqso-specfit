import numpy,pylab
from scipy import interpolate as I
import pickle
inDir = 'FeII_rel_int'

mods = ['G','S','P','IZw1','F']

def makeGauss(lams,lamo,amp,sig):
	oamps = amp/(2*numpy.pi*sig**2)**0.5*numpy.exp(-1*(lams-lamo)**2/(2*sig**2))
	return oamps



lams = numpy.arange(4000,5500,1)

for mod in mods:
	d = numpy.loadtxt('%s/%s_rel_int.txt'%(inDir,mod))

	lamos = d[:,0]
	ampos = d[:,1]



	#sig = 721
	#sig = 1442

	velocities = numpy.arange(10,6000,10)
	feModDict= dict()
	for velocity in velocities:

		oamps = numpy.zeros(lams.size)
		for lamo,ampo in zip(lamos,ampos):
			sig = velocity*0.721
			dlam = sig/(3*10**5.)*lamo
			#print dlam	
	
			tamps = makeGauss(lams,lamo,ampo,dlam)
		
			oamps +=tamps
		feModDict[int(velocity)] = I.splrep(lams,oamps)

	pickle.dump(feModDict,open('%s_modDict_2.pickle'%mod,'wb'))

'''
mod = 'G'
dat = cPickle.load(open('%s_modDict.pickle'%mod,'rb'))




mod = dat[1100]
fes = I.splev(lams,mod)
#print lams.size
#print fes.size
#norm1 = fes[lams==4668]

#print fes[lams==4668]

pylab.plot(lams,fes)
#pylab.show()
norm1 = fes.max()

#pylab.plot(lams,oamps*54)

d2 = numpy.loadtxt('1000FeII/fe_g.txt')

#norm2 = d2[:,1][670]
#print norm2

norm2 = d2[:,1].max()
pylab.plot(d2[:,0],d2[:,1]*norm1/norm2)
pylab.show()
	

'''


