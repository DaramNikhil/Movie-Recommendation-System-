from setuptools import setup,find_packages


SRC_PATH = "src"
INSTALL_REQR = ["flask"]
setup(

    name = SRC_PATH,
    author = "NIKHIL",
    author_email = "nikhildaram51@gmail.com",
    packages= find_packages(),
    version = "0.0.1",
    install_requires = INSTALL_REQR,
    description= "content based movie recommendation system"  

)