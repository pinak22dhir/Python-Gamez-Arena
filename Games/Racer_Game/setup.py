import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='asciiracer',
    version='1.0.3',
    python_requires='>=3.6.0',
    author='Ahmed Gado',
    author_email='ahmedehabg@gmail.com',
    description='A racing game that runs in terminal',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pinak22dhir/Python-Gamez-Arena',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'asciiracer = asciiracer.__main__:main'
        ]
    },
    install_requires=[
        'windows-curses >= 2.0;platform_system=="Windows"'
    ]
)
