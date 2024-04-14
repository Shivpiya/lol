import numpy as np

def mle_for_binomial(data, m):
    """
    Compute the MLE for the theta parameter of the binomial distribution B(m, theta).

    Parameters:
    data (list or np.array): Sample data, each element represents the number of successes in m trials.
    m (int): Number of trials (known).

    Returns:
    float: MLE for theta.
    """
    total_successes = np.sum(data)
    total_trials = m * len(data)
    theta_mle = total_successes / total_trials
    return theta_mle

# Generate random data for a binomial distribution B(m, theta)
np.random.seed(42)  # Seed for reproducibility
m = 10               # Number of trials
theta_true = 0.5     # True probability of success
n = 20               # Sample size

# Generating random data from the binomial distribution
data = np.random.binomial(n=m, p=theta_true, size=n)

# Compute the MLE for theta
theta_estimate = mle_for_binomial(data, m)
print("Randomly generated data:", data)
print("MLE for theta:", theta_estimate)
