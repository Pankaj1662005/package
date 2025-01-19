from setuptools import setup, find_packages

setup(
    name="pankaj_102203410_topsis",
    version="0.1.0",
    author="Pankaj",
    author_email="pankajsheokand2005@gmail.com",
    description="A simple Python package for performing TOPSIS analysis. Created by Pankaj Sheokand.",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_toolkit.cli:main",
        ],
    },
    python_requires=">=3.6",
)
