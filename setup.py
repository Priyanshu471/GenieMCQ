from setuptools import find_packages,setup

setup(
    name='Genie-mcq',
    version='0.0.1',
    author='Priyanshu Mishra',
    author_email='mishrapriyanshu2003@gmail.com',
    install_requires=["openai","langchain","Flask","json","python-dotenv","PyPDF2"],
    packages=find_packages()
)
