import numpy as np
import pandas as pd
from collections import Counter
import math


# ===============================
# Permutaciones
# ===============================

def getIdentityPermutation(size):
    """
    Create an identity permutation of given size.
    """
    return list(range(size))


def getRandomPermutation(size, seed=None):
    """
    Create a random permutation of given size.
    """
    if seed is not None:
        np.random.seed(seed)
    return list(np.random.permutation(size))


def getPermutationFromScores(scores, perm_type="ranking", decreasing=False):
    """
    Create a permutation from a score vector or a matrix of scores.

    Parameters
    ----------
    scores : list, numpy array, or 2D array
        Scores (1D vector or 2D matrix).
    perm_type : str
        "ranking" or "ordering".
    decreasing : bool
        If True, higher scores are considered better.
    """
    scores = np.array(scores)

    if scores.ndim == 2:
        return getPermutations(scores, perm_type, decreasing)
    else:
        if perm_type == "ranking":
            vals = -scores if not decreasing else scores
            # Ranking with random tie-breaking
            order = np.argsort(vals + 1e-9 * np.random.rand(len(vals)))
            ranks = np.empty_like(order)
            ranks[order] = np.arange(1, len(vals) + 1)
            return ranks.tolist()

        elif perm_type == "ordering":
            order = np.argsort(scores)[::-1] if decreasing else np.argsort(scores)
            return (order + 1).tolist()

        else:
            raise ValueError("El parámetro 'perm_type' solo puede ser 'ranking' u 'ordering'.")


def getPermutations(scores, perm_type="ranking", decreasing=False):
    """
    Create a list of permutations from a 2D array of scores.
    """
    return [getPermutationFromScores(row, perm_type, decreasing) for row in scores]


def getFirstOrderMarginals(permutations, smoothed=False):
    """
    Estimate first order marginals from a list of permutations.
    """
    perm_array = np.array(permutations)
    size = perm_array.shape[1]

    def getMarginal(vec):
        counts = [np.sum(vec == i) for i in range(1, size + 1)]
        if not smoothed:
            return np.array(counts) / np.sum(counts)
        else:
            return (np.array(counts) + 1) / (np.sum(counts) + size)

    return np.apply_along_axis(getMarginal, 0, perm_array)

def getIdentityPermutation(size):
    """Given an integer number, it creates a random permutation of that size with values from 0 to n-1."""
    return np.arange(0,size)
    
def getRandomPermutation(size):
    """Given an integer number, it creates a numpy array with a random permutation of that size with values from 0 to n-1."""
    return np.random.permutation(size)

def isPermutation(vector):
    """Given a vector of integers checks if it constitutes a permutation of integers from 0...n-1. """
    sortedVector=np.sort(vector)
    return np.array_equal(sortedVector,np.arange(len(vector)))

def __getPermutations(scores,perm_type="ordering",decreasing=False):
    """This function creates a permutation or a set of permutations based on one or more sets of scores or ratings."""
    indices=np.argsort(scores)
    size=len(indices)
    if decreasing:
        indices=indices[::-1][:size]
    if perm_type=="ordering":
        return indices
    elif perm_type=="ranking":
        variable=np.argsort(indices,1)
        return variable
    else:
        raise NameError('Provided arguments are not acceptable.')
    
def getFirstOrderMarginals(permutations, smoothing=False):
    """This function estimates, from a list of Permutations objects the first order marginals matrix"""

    size= len(permutations[0].perm)
    countM = np.zeros([size, size])
    for permu in permutations:
        for i,val in enumerate(permu.perm):
            countM[i][val]+=1

    probs=countM/len(permutations)
    return probs

# ===============================
# Discretización
# ===============================

import numpy as np
import pandas as pd

def _fmt_max2(v, d=2):
    """Devuelve el número con como máximo d decimales (sin ceros sobrantes)."""
    return f"{float(v):.{d}f}".rstrip('0').rstrip('.')

def discretizeEW(x, num_bins, decimals=2):
    """Equal-Width discretization."""
    x = np.asarray(x, dtype=float)
    xmin, xmax = np.min(x), np.max(x)
    if xmax <= xmin:
        raise ValueError("Todos los valores son iguales; no se puede discretizar.")
    width = (xmax - xmin) / num_bins
    edges = np.array([xmin + i * width for i in range(num_bins + 1)], dtype=float)
    
    # Fijar extremos exactos
    edges[0], edges[-1] = xmin, xmax  
    cut_points_rounded = [round(v, decimals) for v in edges[1:-1].tolist()]
    
    # Devolver categorías como números (0, 1, 2, ...)
    categorias = pd.cut(x, bins=edges, include_lowest=True, right=True, labels=False)
    
    return {"categorias": categorias, "puntos_corte": cut_points_rounded}

def discretizeEF(x, num_bins, decimals=2):
    """Equal-Frequency discretization."""
    x = np.asarray(x, dtype=float)
    qs = np.linspace(0, 1, num_bins + 1)
    edges = np.quantile(x, qs)
    edges = np.unique(edges)
    
    cut_points_rounded = [round(v, decimals) for v in edges[1:-1].tolist()]
    
    # Devolver categorías como números
    categorias = pd.cut(x, bins=edges, include_lowest=True, right=True, labels=False, duplicates='drop')
    
    return {"categorias": categorias, "puntos_corte": cut_points_rounded}

def discretize(x, cut_points, decimals=2):
    """Discretización con cortes personalizados."""
    x = np.asarray(x, dtype=float)
    cuts = np.asarray(cut_points, dtype=float)
    edges = np.sort(np.unique(np.concatenate(([x.min()], cuts, [x.max()]))))
    
    cut_points_rounded = [round(v, decimals) for v in edges[1:-1].tolist()]
    
    # Devolver categorías como números
    categorias = pd.cut(x, bins=edges, include_lowest=True, right=True, labels=False)
    
    return categorias

# ===============================
# Entropía
# ===============================

def entropy(x):
    """
    Calculate Shannon entropy of a categorical vector.
    """
    freqs = Counter(x)
    probs = np.array(list(freqs.values())) / len(x)
    H = -np.sum(probs * np.log2(probs))
    return float(H)


# ===============================
# Otros helpers
# ===============================

def sample_even(max_par=48, k=5, replace=True, seed=None):
    """
    Sample even numbers up to max_par.
    """
    if seed is not None:
        np.random.seed(seed)
    pool = np.arange(0, max_par + 1, 2)
    return np.random.choice(pool, size=k, replace=replace)


def symmetrize_mean_loop(A):
    """
    Symmetrize a square matrix by averaging with its transpose.
    """
    A = np.array(A)
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")
    n = A.shape[0]
    B = A.copy()
    for i in range(n):
        for j in range(n):
            m = np.mean([A[i, j], A[j, i]])
            B[i, j] = m
            B[j, i] = m
    return B

def normalize01(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))

def standardize(x):
    return (x - np.mean(x)) / np.std(x, ddof=0)