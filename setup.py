from setuptools import setup, find_packages

setup(
    name='ubelt',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'Click',
        'dnspython',
        'future',
        'python-whois',
        'passlib',
        'diceware',
        'flask',
    ],
    entry_points='''
    [console_scripts]
    ubelt=ubelt.commands:cli
    ''',
)
