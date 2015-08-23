data {
  int<lower=0> N;     // sample size
  int<lower=0> M;
  int<lower=0> Y[N];  // response variable
}
parameters {
  simplex[M] p;
  real<lower=0.01> sigma;
}

model {
        sigma ~ normal(0.05, 100);
        for (i in 1:M) {
            p[i] ~ normal(0.05, sigma);
        }
        for (j in 1:N) {
            Y[j] ~ categorical(p);
        }
}
