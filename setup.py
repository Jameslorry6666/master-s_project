from setuptools import setup, find_packages

setup(
    name="my-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
    ],
    author="James Ilori ",
    author_email="oluwasegunjamesilori@gmail.com.com",
    description="Predicting dementia from Magnetic Resonance Imaging dataset features using machine learning tools"
)
