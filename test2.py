import numpy
import matplotlib.pyplot as plt
import pystan
import sys
import random
import pandas as pd
N = 200
M = 20
probability = [0.05,0.08,0.01,0.001,0.001,0.01,0.001,0.05,0.07,0.08,0.06,0.1,0.04,0.01,0.05,0.05,0.07,0.09,0.03]
if sum(probability) > 1. or len(probability)!=M-1:
    print "error probability"
    sys.exit(1)
probability.append(1.-sum(probability))
sample = []
for i in range(M):
    sample.extend([i+1]*int(probability[i]*N))
for i in range(N-len(sample)):
    sample.append(random.randint(1, M))

training_data = dict(N=N,M=M, Y=sample)
fit = pystan.stan(file='test2.stan', data=training_data, iter=10000, chains=1)
print fit
fit.plot()
plt.show()
print fit.get_posterior_mean()
#compiled_model = pystan.StanModel(file='test2.stan')
#model = compiled_model.optimizing(training_data,seed=12345,iter=1500)
#print {"p": map(lambda x:max(x,1e-4),model["p"]) ,"sigma":model["sigma"]}
df = pd.DataFrame(sample)
total = pd.value_counts(df[0])
prob = pd.Series(total,dtype=float)/ total.sum()
print numpy.std(prob)
print prob.sort_index()
