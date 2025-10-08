from setuptools import setup, find_packages

with open("README.txt", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="permupack",
    version="0.1.0",
    author="Paula Azqueta",
    author_email="pazqueta002a@ikasle.ehu.eus",
    url="https://github.com/paulaazqueta/permupack",  
    license="MIT",
    description="Paquete didáctico on utilidades estadísticas (varianza, entropia, filtrado, etc.)",
    long_description=long_description,
    long_description_content_type="text/plain",
    include_package_data=True,  
    packages=find_packages(),  
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.17.2",
        "pandas>=0.25.1",
        "matplotlib>=3.1.1",
        "seaborn>=0.9.0",
        "scikit-learn>=0.22"  
    ],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)