from setuptools import setup


setup(
    name='cryptopy',
    version='0.01',
    description='A sha256 based enc/dec tool',
    author='MYavuzYAGIS',
    zip_safe=False,
    author_email='m.yavuzyagis@gmail.com, myagis16@ku.edu.tr',
    py_modules=['cryptopy'],
    install_requires=['Click','Pycryptodome','Pyfiglet','Termcolor' ],
    entry_points='''
    [console_scripts]
    cryptopy=cryptopy:main
    ''')