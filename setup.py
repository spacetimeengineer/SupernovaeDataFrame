from setuptools import setup, find_packages

setup(
    name="cosmic_expansion_analyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "cosmoexp=supernovae_dataframe:main",  # Replace `main` with the actual entry point function
        ],
    },
)