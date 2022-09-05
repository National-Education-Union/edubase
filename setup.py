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

    packages=find_packages,
    install_requires=['pandas', 'os', 'datetime'],
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)