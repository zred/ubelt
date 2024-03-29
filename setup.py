from setuptools import setup


setup(
    name='ubelt',
    version='0.3',
    py_modules=['ubelt'],
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
    ubelt=ubelt:cli
    ''',
)
