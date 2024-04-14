import numpy as np

def calculate_mle_estimates(data):
    """
    Calculate the maximum likelihood estimates for the mean and variance
    of a normally distributed dataset.

    Parameters:
    data (np.array): An array of data points assumed to be drawn from a normal distribution.

    Returns:
    float: Estimated mean (theta_1)
    float: Estimated variance (theta_2)
    """
    # Calculate the estimated mean (theta_1)
    theta_1_hat = np.mean(data)

    # Calculate the estimated variance (theta_2)
    theta_2_hat = np.var(data, ddof=0)  # ddof=0 for MLE; use ddof=1 for unbiased sample variance

    return theta_1_hat, theta_2_hat

# Example data
data = np
