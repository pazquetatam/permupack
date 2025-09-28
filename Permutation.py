import numpy as np
from .perm_utils import isPermutation, getRandomPermutation, getIdentityPermutation, __getPermutations


class Permutation:
    """The Permutation class enables the creation, management and operations 
    of permutation-coded integer vectors."""

    def __init__(self, *args):
        """Constructor function. """
        if len(args) == 1:
            if isinstance(args[0], (list, np.ndarray)):
                if isPermutation(args[0]):
                    self.perm = np.array(args[0])
                else:
                    raise NameError(
                        "The vector indicated does not comply with permutation condition. "
                        "Permutations need to be specified from 0 to n-1."
                    )
            elif isinstance(args[0], int):
                # create the identity permutation with the specified size
                self.perm = getIdentityPermutation(args[0])
        else:
            # creates a random permutation of size 10 by default.
            self.perm = getRandomPermutation(10)

    def printPerm(self):
        """Prints the permutation"""
        print("Permutation:", self.perm)

    def inverse(self):
        """Return a Permutation object with the inverse permutation."""
        permu = np.argsort(self.perm)
        return Permutation(permu)

    def composeWith(self, permutation2):
        """Return the composition with another Permutation object."""
        if isinstance(permutation2, Permutation) and len(permutation2.perm) == len(self.perm):
            return Permutation(self.perm[permutation2.perm])
        else:
            raise NameError(
                "The argument must be a Permutation object with the same size."
            )

    def setRandomPermutation(self, size):
        """Resets the current permutation with a new random one of the predefined size."""
        self.perm = getRandomPermutation(size)

    def apply_to(self, x):
        """Apply this permutation to a vector or matrix."""
        return perm_apply(x, self.perm)

    def swap(self, i, j):
        """Swap two positions of this permutation (in-place)."""
        self.perm = perm_swap(self.perm, i, j)
        return self

    def matrix(self):
        """Return the permutation matrix corresponding to this permutation."""
        return perm_matrix(self.perm)

    def parity(self):
        """Return the parity (even/odd) of this permutation."""
        return perm_parity(self.perm)

    def cycles(self):
        """Return the cycle decomposition of this permutation."""
        return perm_cycles(self.perm)


# ========================
# Utility functions
# ========================

def perm_apply(x, p):
    """Aplica una permutación p a un vector o matriz."""
    if isinstance(x, np.ndarray):
        if x.ndim == 1:
            if len(x) != len(p):
                raise ValueError("`p` debe tener longitud igual al vector")
            return x[p]
        elif x.ndim == 2:
            if x.shape[0] != len(p):
                raise ValueError("`p` debe tener longitud igual a nrows")
            return x[p, :]
        else:
            raise ValueError("Solo se soportan vectores o matrices 2D")
    else:
        x = np.array(x)
        return x[p]


def perm_swap(p, i, j):
    """Intercambia las posiciones i y j en la permutación p."""
    p = np.array(p).copy()
    p[i], p[j] = p[j], p[i]
    return p


def perm_matrix(p):
    """Construye la matriz de permutación P tal que P @ x = x[p]."""
    n = len(p)
    P = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[i, p[i]] = 1
    return P


def perm_parity(p):
    """Calcula la paridad de la permutación (even/odd)."""
    invs = 0
    n = len(p)
    for i in range(n - 1):
        invs += np.sum(p[i] > p[i + 1:])
    return {
        "inversions": int(invs),               # 🔹 añadido
        "parity": "even" if invs % 2 == 0 else "odd",
        "sign": 1 if invs % 2 == 0 else -1
    }



def perm_cycles_named(p, names):
    n = len(p)
    seen = [False]*n
    cycles = []
    for i in range(n):
        if not seen[i]:
            cycle = []
            j = i
            while not seen[j]:
                seen[j] = True
                cycle.append(names[j])
                j = p[j]
            if len(cycle) > 1:
                cycles.append(cycle)
    return cycles


def getPermutationsFromScores(scores, perm_type="ordering", decreasing=False):
    """Create Permutation objects from a list of scores."""
    perm_list = __getPermutations(scores, perm_type, decreasing)
    object_list = [Permutation(x) for x in perm_list]
    return object_list
