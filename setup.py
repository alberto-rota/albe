from setuptools import setup, find_packages

setup(
    name="albe",
    version="v0.0.2",
    packages=find_packages(),
    install_requires=[
        "numpy==2.2.2",
        "nvidia_ml_py==12.570.86",
        "nvitop==1.4.2",
        "platformdirs==4.3.6",
        "plotext==5.3.2",
        "psutil==6.1.1",
        "pynvml==11.5.3",
        "setuptools==75.1.0",
        "textual==1.0.0",

    ], 
    description="Albe's helpers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alberto-rota/albe",
    author="Alberto Rota",
    author_email="alberto1.rota@polimi.it",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
