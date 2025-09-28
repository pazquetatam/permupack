from setuptools import setup, find_packages

setup(
    name="permupack",
    version="0.1.0",
    description="A package for permutation utilities, discretization, entropy, and visualization",
    author="Tu Nombre",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn"
    ],
    python_requires=">=3.7",
)
