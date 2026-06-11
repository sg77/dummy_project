from setuptools import setup, find_packages

setup(
    name='format_cli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'format-cli=format_cli.cli:main'
        ]
    }
)
