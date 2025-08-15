from setuptools import setup, find_packages


setup(
    name='dundie',
    version='0.1.0',
    author='Walter Angolar',
    description='Rewards Point System for Dunder Mifflin.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dundie=dundie.__main__:main',
        ]
    }
)
