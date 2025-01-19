from setuptools import setup, find_packages

setup(
    name="pankaj_102203410_topsis",
    version="0.1.0",
    author="Pankaj",
    author_email="pankajsheokand2005@gmail.com",
    description="A simple Python package which we can use  for TOPSIS analysis. This is created by Pankaj Sheokand student of thapar university ",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis=pankaj_102203410_topsis.cli:main",
        ],
    },
    python_requires=">=3.6",
)
