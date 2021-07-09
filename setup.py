from setuptools import setup


setup(
    name='ubelt',
    version='0.2',
    py_modules=['ubelt'],
    install_requires=[
        'Click',
        'dnspython',
        'future',
        'python-whois',
    ],
    entry_points='''
    [console_scripts]
    ubelt=ubelt:cli
    ''',
)
