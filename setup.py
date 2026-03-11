from setuptools import find_packages, setup

setup(
    name="efootprint",
    version="17.0.0",
    description="Digital service environmental footprint model",
    packages=find_packages(include=["efootprint", "efootprint.*"]),
    include_package_data=True,
    package_data={
        "efootprint": [
            "constants/custom_units.txt",
            "constants/countries_computations/*.csv",
        ],
    },
    install_requires=[
        "pint>=0.25",
        "matplotlib>=3.10",
        "pytz==2024.1",
        "pyvis==0.3.2",
        "plotly==5.19",
        "pandas>=2",
        "requests>=2.31",
        "ecologits>=0.9.2",
        "boaviztapi>=2",
        "orjson>=3.11",
        "zstandard>=0.23",
        "ciso8601>=2.3",
    ],
)