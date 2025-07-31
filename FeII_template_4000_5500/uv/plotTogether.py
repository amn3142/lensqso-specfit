import numpy,pylab

d1 = numpy.loadtxt('IzwI/Izw1_10.dat')
log_x_wave = numpy.log(3500)+(d1[:,0]-1)*numpy.log(7500.0/3500.0)/(4500-1)
wfe=numpy.exp(log_x_wave)

amps1 = d1[:,1]*1e14

d2 = numpy.loadtxt('Mejia2015_2200-3646')


pylab.plot(wfe,amps1)
pylab.plot(d2[:,0],d2[:,1])
pylab.show()
