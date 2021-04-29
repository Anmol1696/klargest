import setuptools

with open("README.md", "r") as infile:
    long_description = infile.read()

with open("requirements.txt", "r") as infile:
    requirements = infile.read()

setuptools.setup(
    name="klargest",
    version="0.1",
    author="Anmol",
    author_email="anmol1696@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_namespace_packages(
        include=[
            "klargest",
            "klargest.*",
            "klargest.tests",
            "klargest.tests.*",
        ]
    ),
    python_requires='>=3.7',
    install_requires=requirements
)
