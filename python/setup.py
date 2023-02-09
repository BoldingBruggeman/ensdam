from setuptools import setup, find_packages

setup(
    name='pyensdam',
    version='0.1.1',
    author='Jean-Michel Brankart and Bolding-Bruggeman ApS',
    author_email='karsten@bolding-bruggeman.com',
    license='GPL',
    packages=['pyensdam'],
    package_data={'pyensdam': ['*.so', '*.dll', '*.dylib', '*.pyd']},
    zip_safe=False,
#    entry_points = {
#        'console_scripts': [
#            'pygetm-subdiv = pygetm.subdiv:main',
#            'pygetm-test-scaling = pygetm.parallel:test_scaling_command',
#            'pygetm-compare-nc = pygetm.util.compare_nc:compare_command',
#        ],
#    }
)

