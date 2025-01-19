import numpy as np

def topsis(data, weights, impacts):
    """
    Perform TOPSIS analysis.

    Parameters:
        data (numpy.ndarray): 2D array with alternatives and criteria.
        weights (list): Weights for each criterion.
        impacts (list): List of impacts for criteria, 1 for benefit and -1 for cost.

    Returns:
        numpy.ndarray: Scores for each alternative.
    """
    # Normalize the data
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Apply weights
    weighted_data = norm_data * weights

    # Determine ideal and anti-ideal solutions
    ideal = np.max(weighted_data * impacts, axis=0)
    anti_ideal = np.min(weighted_data * impacts, axis=0)

    # Calculate distances
    dist_ideal = np.sqrt(((weighted_data - ideal) ** 2).sum(axis=1))
    dist_anti_ideal = np.sqrt(((weighted_data - anti_ideal) ** 2).sum(axis=1))

    # Compute scores
    scores = dist_anti_ideal / (dist_ideal + dist_anti_ideal)
    return scores
