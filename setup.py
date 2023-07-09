import setuptools

setuptools.setup(
    name="notionPy",
    version="1.003",
    author="soft-machine-net",
    author_email="info@soft-machine.net",
    description="Common notion api package'",
    long_description="Common notion api package",
    long_description_content_type="text/markdown",
    url="https://github.com/cm-hirano-shigetoshi/python_sample_command",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.7',
)