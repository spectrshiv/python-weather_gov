import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="weather_gov",
    version="0.2",
    #scripts=["weather_gov"],
    author="TJ Courier",
    author_email="pycepticus@gmail.com",
    description="A Python wrapper for the National Weather Service's Weather.gov API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spectrshiv/python-weather_gov",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    py_modules=["urllib", "json"],
    
)