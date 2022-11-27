from setuptools import setup, find_packages

setup(
    name = 'teasharp',
    version = '1.5.0',
    packages = find_packages(),
    install_requires = [
        'click',
        'colorama'
    ],
    entry_points = '''
    [console_scripts]
    teasharp=cli:main
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
  ],
)