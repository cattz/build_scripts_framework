from setuptools import setup, find_packages

setup(
    name='bsf',
    version='0.0.0',
    packages=find_packages('.'),
    package_dir={'bsf': 'bsf'},
    include_package_data=True,
    url='',
    license='',
    author='xabier davila',
    author_email='',
    description='Build scripts framework',
    install_requires=[
        'pyyaml==3.11'
    ],
    entry_points={
        'console_scripts': [
            'bsf = bsf.bin.bs:main',
        ],
    },
)


