from setuptools import setup, find_packages

setup(
    name='ConvertChemistry',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['chempy'],
    entry_points={
        'console_scripts': [
            'grams_to_moles = ConvertChemistry.converter:main'
        ]
    }
)
