import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name = "TraceManager",
  version = "0.0.1",
  author = "Azmi ŞAHİN",
  author_email = "azmisahin@outlook.com",
  description = "The code architecture allows a simple method to be monitored with python.",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/azmisahin/azmisahin-software-web-component-trace-manager-python",
  packages = setuptools.find_packages(),
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
  )
