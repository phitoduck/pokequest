from setuptools import setup, find_packages
from typing import Dict, List

def get_install_requires() -> List[str]:
    """At minimum, will install these dependencies

    Returns:
        List[str]: minimum dependencies and versions
    """
    return [
        
    ]

def get_extras_require() -> Dict[str, List[str]]:
    """Enables a streamlined install of pythoncore based on the application consuming it.

    Returns:
        Dict[str, str]: individual dependencies for each pythoncore functionality
    """
    extras = {
        "testing": [
            "pytest==6.1.2",
            "pytest-cov==2.10.1",
        ],
        "linting": [
            "pylint==2.6.0",
            "flake8==3.8.4",
            "black>=20.8b1",
            "darglint==1.5.5",
            "mypy==0.790",
            # "data-science-types>=0.2.20",  # pandas, numpy, matplotlib
        ],
    }
    extras["all"] = [item for group in extras.values() for item in group]
    return extras

setup(
    name = "pokequest",
    version = "1.0.0",
    author = "Eric",
    # author_email = "andrewjcarter@gmail.com",
    # description = ("An demonstration of how to create, document, and publish "
                                #    "to the cheese shop a5 pypi.org."),
    # license = "BSD",
    # keywords = "example documentation tutorial",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    install_requires=get_install_requires(),
    extras_require=get_extras_require()
    # long_description=read('README'),
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)



