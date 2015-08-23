data {
  int<lower=0> N;     // sample size
  int<lower=0> M;
  int<lower=0> Y[M,N];  // response variable
}
parameters {
  real<lower=0.0,upper=1.0> p[M];
  real<lower=0.001> sigma;
}

model {
    sigma ~ normal(0,100);
    for (i in 1:M) {
        p[i] ~ normal(1.0/M, sigma);
        for (j in 1:N) {
            Y[i,j] ~ bernoulli(p[i]);
        }
    }
}
