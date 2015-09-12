from setuptools import setup, find_packages

setup(
    name='pjdby',
    version='0.0.0',
    packages=find_packages('.'),
    package_dir={'pjdby': 'pjdby'},
    include_package_data=True,
    url='',
    license='',
    author='xabier davila',
    author_email='',
    description='Python jobs driven by yaml config file',
    install_requires=[
        'pyyaml==3.11'
    ],
    entry_points={
        'console_scripts': [
            'pyb = pjdby.bin.pyb:main',
        ],
    },
)


