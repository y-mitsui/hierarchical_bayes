import sys
import numpy
import pystan
import random
import pandas as pd

num_sample = 200
num_category = 20
probability = [0.05,0.08,0.01,0.001,0.001,0.01,0.001,0.05,0.07,0.08,0.06,0.1,0.04,0.01,0.05,0.05,0.07,0.09,0.03]

if sum(probability) > 1. or len(probability)!=num_category-1:
    print "error probability"
    sys.exit(1)
    
probability.append(1.-sum(probability))
sample = []
for i in range(num_category):
    sample.extend([i+1]*int(probability[i]*num_sample))
for i in range(num_sample-len(sample)):
    sample.append(random.randint(1, num_category))

training_data = dict(N=num_sample,M=num_category, Y=sample)
fit = pystan.stan(file='hbayes.stan', data=training_data, iter=10000, chains=1)
print "------- hierarchical bayse estimate ------------"
print fit
# get posterior's mean
# fit.get_posterior_mean()

print "------- maximum likelihood estimate ------------"
df = pd.DataFrame(sample)
total = pd.value_counts(df[0])
prob = pd.Series(total,dtype=float)/ total.sum()
print prob.sort_index()
print numpy.std(prob)

# show posterior's
fit.plot().show()


