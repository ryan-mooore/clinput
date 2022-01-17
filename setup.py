import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="clinput",
    packages=["clinput"],
    version="0.0.1",
    license="MIT",
    author="Ryan Moore",
    description="Simple command line input validator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryan-mooore/clinput",
    keywords=["cli", "input", "validation"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pick", "python-dateutil"],
    include_package_data=True,
)
