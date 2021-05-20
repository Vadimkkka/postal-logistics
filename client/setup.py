from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
        name="console_app", 
        version='0.0.1',
        author="Vadimkkka",
        author_email="vadimka.shlak@mail.tu",
        description='Postal logistics',
        long_description='My first Python package with a slightly longer description',
        packages=find_packages(),
        install_requires=requirements,
        license ='MIT',
        keywords=['python', 'mail', 'postal', 'logistics'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
        entry_points ={
            'console_scripts': [
                'aloe=console_app:hello'
            ]
        },
        zip_safe = False
)
