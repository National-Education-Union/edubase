from setuptools import setup, find_packages

setup(
    name='edubase',
    version='0.1',
    description='A Python moule to import CSVs from \
https://www.get-information-schools.service.gov.uk/. There is also a function \
to update school URNs to the latest value.',

    url='https://github.com/National-Education-Union/edubase',
    author='Andrew Baisley',
    author_email='andrew.baisley@neu.org.uk',

    install_requires=['pandas'],
    )