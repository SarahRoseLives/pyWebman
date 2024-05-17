from setuptools import setup, find_packages

setup(
    name='pyWebman',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'pywebman = pyWebman.main:main'
        ]
    },
    author='Sarah Rose',
    author_email='sarahroselives@protonmail.com',
    description='A package for interacting with Webman on PS3',
    url='https://github.com/sarahroselives/pyWebman',
    keywords='PS3 Webman package',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
