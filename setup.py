from setuptools import setup


requirements = ['click', 'Telethon']

setup(
    name='steve-cli',
    version='0.0.1',
    install_requires=requirements,
    entry_points={
        'console_scripts': ['steve-cli = cli:steve_cli']
    },
)