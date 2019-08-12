from setuptools import setup

setup(
    name='family_tree',
    version='0.1.0',
    packages=['family_tree'],
    entry_points={
        'console_scripts': [
            'family_tree = family_tree.__main__:main'
        ]
    }, install_requires=['nameparser', 'PyQt5']
)