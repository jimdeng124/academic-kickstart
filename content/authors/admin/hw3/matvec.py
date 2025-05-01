import multiprocessing
import numpy as np

from os import cpu_count


def worker(A, x, shared_y, start_idx, end_idx):
    # TODO 1: Add all necessary arguments to the function signature.
    # TODO 2: Complete the code below so that it computes A_{I, :} x
    #         for a submatrix A_{I,:} of A.
    # Sub-matrix multiply:
    partial_result = A[start_idx:end_idx] @ x
    # Write results into correct slice of shared array:
    shared_y[start_idx:end_idx] = partial_result


def parallel_matvec(A: np.ndarray, x: np.ndarray, nproc: int):
    """Compute the matrix-vector product A * x in parallel.

    Arguments
    ---------
    A : numpy.ndarray
        The input matrix.
    x : numpy.ndarray
        The input vector.
    nproc : int
        The number of parallel processes to use.

    Returns
    -------
    numpy.ndarray
        A vector holding the result of the operation `A * x`.

    Raises
    ------
    ValueError
        If the number of processes is not strictly positive.
    """
    if nproc <= 0:
        raise ValueError("Number of processes must be strictly positive")

    m = A.shape[0]

    # Determine the number of rows of A to give per process
    chunk_size = m // nproc

    # Initialize a shared array to write results to in subprocesses.
    shared_y = multiprocessing.Array('d', m, lock=False)
    processes = []
    
    start = 0
    for i in range(nproc):
        end = start + chunk_size
        # Last process gets any leftover rows
        if i == nproc - 1:
            end = m

        # Spawn a process that will handle rows [start, end)
        p = multiprocessing.Process(
            target=worker,
            args=(A, x, shared_y, start, end)
        )
        processes.append(p)
        p.start()
        start = end

    for proc in processes:
        proc.join()

    y = np.frombuffer(shared_y, dtype=np.float64)
    return y


if __name__ == "__main__":
    A = np.random.randn(100, 50)
    x = np.random.rand(50)
    y_numpy = A @ x
    nproc = cpu_count()
    if nproc:
        y_nonnumpy = parallel_matvec(A, x, 2 * nproc)
    else:
        y_nonnumpy = parallel_matvec(A, x, 1)
    print(np.linalg.norm(y_nonnumpy - y_numpy))
