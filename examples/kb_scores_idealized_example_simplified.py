import pyensdam as ens
import numpy as np

# EnsDAM functions aliases
#crps_score = ensdam.ensscores.crps_score
#rcrv_score = ensdam.ensscores.rcrv_score
#compute_ranks = ensdam.ensscores.compute_ranks

# Parameters of the example
m = 20       # Size of the ensemble
n = 1000     # Size of the state vector

mu = 0.0     # Ensemble mean
sigma = 1.0  # Error standard deviation

# Sample prior ensemble from N(0,I) distribution
prior_ensemble = np.random.normal(mu, sigma,(n,m))

# Sample reference truth from the same distribution
reference_truth = np.random.normal(mu, sigma,n)

#KB ens.anam.ana_obs()

# Compute CRPS score, using reference truth as verification data
crps,crps_reliability,crps_resolution = ens.score.crps_score_global(prior_ensemble,reference_truth)
print ('CRPS:                                     ',crps)
print ('Prior CRPS reliability and resolution:    ',crps_reliability,crps_resolution)

# Compute RCRV score, using reference truth as verification data
rcrv_bias,rcrv_spread = ens.score.rcrv_score_global(prior_ensemble,reference_truth)
print ('Prior RCRV bias and spread:    ',rcrv_bias,rcrv_spread)

# Compute rank histogram
ranks = ens.score.compute_ranks(prior_ensemble,reference_truth)
print ('Prior ranks :',ranks[0:15],'.....')

ranks,rank_histogram = ens.score.compute_ranks(prior_ensemble,reference_truth, histogram=True)
print ('Prior rank histogram:',rank_histogram)
