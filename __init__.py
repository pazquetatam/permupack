"""
permupack: A package for permutation utilities, discretization, entropy, and visualization.
"""

__version__ = "0.1.0"
__author__ = "Tu Nombre"

# Imports from Permutation (class and helpers)
from .Permutation import Permutation

from .perm_utils import (
    getIdentityPermutation,
    getRandomPermutation,
    getPermutationFromScores,
    getPermutations,
    getFirstOrderMarginals,
    isPermutation,
    discretizeEW,
    discretizeEF,
    discretize,
    entropy,
    sample_even,
    symmetrize_mean_loop,
)

from .perm_plotting import (
    plotFirstOrderMarginals,
    dibujar_roc,
    dibujar_entropias,
    dibujar_correlaciones,
)

__all__ = [
    "Permutation",
    "getIdentityPermutation",
    "getRandomPermutation",
    "getPermutationFromScores",
    "getPermutations",
    "getFirstOrderMarginals",
    "isPermutation",
    "discretizeEW",
    "discretizeEF",
    "discretize",
    "entropy",
    "sample_even",
    "symmetrize_mean_loop",
    "plotFirstOrderMarginals",
    "dibujar_roc",
    "dibujar_entropias",
    "dibujar_correlaciones",
]
