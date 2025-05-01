import multiprocessing

from math import ceil
from os import cpu_count
from random import uniform

def trial(m):
    """Approximate pi using a Monte-Carlo method.

    This function generates `m` random samples on the unit square and counts
    how many of said samples ended up inside the unit circle.

    Arguments
    ---------
    m : int
        The number of random samples to generate.

    Returns
    -------
    int
        The number of samples that fell inside the unit circle.

    Raises
    ------
    ValueError
        If the number m is not strictly positive.
    """
    # TODO: Add your code here
    if m <= 0:
        raise ValueError("Number of samples must be positive.")
    count_inside = 0
    for _ in range(m):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x*x + y*y <= 1:
            count_inside += 1
    return count_inside

def approx_pi(N):
    """Approximate pi using multiple processes and N samples total.

    The number of processes generated should be equal to the number of CPU
    cores available to the user.

    Arguments
    ---------
    N : int
        The total number of samples to use.

    Returns
    -------
    float
        The computed estimate for pi.

    Raises
    ------
    ValueError
        If the number of samples `N` is not positive.
    """
    # TODO: Add your code here.
    if N <= 0:
        raise ValueError("Number of samples must be positive.")

    num_procs = cpu_count()
    
    # Distribute N 
    base = N // num_procs
    remainder = N % num_procs
    
    # Create a list of sample counts 
    tasks = [base + 1 if i < remainder else base for i in range(num_procs)]
    
    with multiprocessing.Pool(num_procs) as pool:
        results = pool.map(trial, tasks)

    total_inside = sum(results)
    pi_estimate = 4.0 * total_inside / N
    return pi_estimate

def approx_pi_bonus(*number_of_samples):
    """Approximate pi using multiple processes.

    The number of processes generated must be equal to the number of arguments
    passed to this function. Each argument must be a positive integer that
    specifies how many samples the corresponding process should use.

    Arguments
    ---------
    number_of_samples : array-like
        A variable-length array of sample counts.

    Returns
    -------
    float
        The computed estimate for pi.

    Raises
    ------
    ValueError
        If any of the arguments is not positive or if no arguments have been
        provided.
    """
    # TODO: Your code here (bonus 10%).
    if len(number_of_samples) == 0:
        raise ValueError("No sample counts provided.")
    if any(n <= 0 for n in number_of_samples):
        raise ValueError("All sample counts must be positive.")

    k = len(number_of_samples)
    with multiprocessing.Pool(k) as pool:
        results = pool.map(trial, number_of_samples)

    total_inside = sum(results)
    total_samples = sum(number_of_samples)
    pi_estimate = 4.0 * total_inside / total_samples
    return pi_estimate

if __name__ == "__main__":
    pi_est_1 = approx_pi(1000)
    pi_est_2 = approx_pi_bonus(250, 250, 100, 300, 100)
    print(pi_est_1, pi_est_2)
