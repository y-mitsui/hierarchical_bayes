import numpy
import matplotlib.pyplot as plt
import pystan

num_hit=numpy.array([3,5,1,10,15,7,6],dtype=float)
num_test=numpy.array([15,15,15,15,15,15,15],dtype=float)
#Y=num_hit/num_test
#plt.bar(range(len(Y)), Y)
#plt.show()
sample1=[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0] + [1,1,0,0,0,0,0,0,0,0] 
sample2=[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0] + [1,1,1,0,0,0,0,0,0,0] 
sample3=[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0] + [1,1,1,1,1,0,0,0,0,0] 
sample4=[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0] + [1,1,1,1,1,0,0,0,0,0] 
sample5=[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0] + [1,1,0,0,0,0,0,0,0,0] 
multi_sample = [sample1,sample2,sample3,sample4,sample5]
compiled_model = pystan.StanModel(file='test.stan')
training_data = dict(N=len(sample1),M=len(multi_sample), Y=multi_sample)
model = compiled_model.optimizing(training_data,iter=1500)
print model
