import seaborn as sns
from .perm_utils import getFirstOrderMarginals
import numpy as np
import matplotlib.pyplot as plt

def plotFirstOrderMarginals(permutations):
    """This function estimates from a list of permutations the first order marginals and visualizes them"""

    matrix=getFirstOrderMarginals(permutations)
    size=len(permutations[0].perm)
    # plot the heatmap
    sns.heatmap(matrix,
                xticklabels=np.arange(0,size),
                yticklabels=np.arange(0,size), annot=True)
    plt.xlabel("Items")
    plt.ylabel("Positions")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import seaborn as sns
import pandas as pd


# -----------------------------------------------------------
#   Visualización curva ROC
# -----------------------------------------------------------

def dibujar_roc(A, col_real=0, col_prob=1):
    """
    Dibujar la curva ROC y calcular el AUC.

    Parameters
    ----------
    A : pandas.DataFrame o numpy.ndarray
        Con dos columnas: valores reales (0/1) y probabilidades.
    col_real : int o str
        Índice o nombre de la columna de la variable real.
    col_prob : int o str
        Índice o nombre de la columna de probabilidades estimadas.

    Returns
    -------
    roc_info : dict con fpr, tpr y auc
    """
    if isinstance(A, pd.DataFrame):
        real = A.iloc[:, col_real] if isinstance(col_real, int) else A[col_real]
        prob = A.iloc[:, col_prob] if isinstance(col_prob, int) else A[col_prob]
    else:
        real = A[:, col_real]
        prob = A[:, col_prob]

    fpr, tpr, _ = roc_curve(real, prob)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, color="blue", lw=2,
             label=f"ROC curve (AUC = {roc_auc:.3f})")
    plt.plot([0, 1], [0, 1], color="red", lw=2, linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Curva ROC")
    plt.legend(loc="lower right")
    plt.show()

    return {"fpr": fpr, "tpr": tpr, "auc": roc_auc}


# -----------------------------------------------------------
#   Entropía normalizada por variable
# -----------------------------------------------------------

def entropia(x):
    """
    Calcular entropía de una variable categórica.
    """
    values, counts = np.unique(x, return_counts=True)
    p = counts / counts.sum()
    return -np.sum(p * np.log2(p))


def dibujar_entropias(df):
    """
    Dibujar entropía normalizada de todas las columnas categóricas.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    entropias_norm : pandas.Series
    """
    entropias = df.apply(entropia, axis=0)
    maximos = df.apply(lambda col: np.log2(len(np.unique(col))), axis=0)
    entropias_norm = entropias / maximos

    entropias_norm.plot(kind="bar", color="skyblue")
    plt.title("Entropía normalizada por variable")
    plt.ylabel("Entropía normalizada (0-1)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    return entropias_norm


# -----------------------------------------------------------
#   Visualización matriz de correlaciones
# -----------------------------------------------------------

def dibujar_correlaciones(df):
    """
    Dibujar matriz de correlaciones.

    Parameters
    ----------
    df : pandas.DataFrame con variables numéricas

    Returns
    -------
    M : pandas.DataFrame
        Matriz de correlaciones
    """
    M = df.corr(method="pearson")

    plt.figure(figsize=(8, 6))
    sns.heatmap(M, annot=True, cmap="coolwarm", center=0,
                square=True, cbar=True,
                xticklabels=True, yticklabels=True)
    plt.title("Matriz de correlaciones")
    plt.tight_layout()
    plt.show()

    return M
   