from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='skaki',  # Required
    version='0.1',  # Required
    description='visualizing chess ratings in a modern way',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/romerocesar/skaki',  # Optional
    author='Cesar Romero',  # Optional
    author_email='cesar@romero.ws',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python data analytics chess',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires='>=3.6',
    install_requires=['pandas', 'requests', 'jupyter', 'click'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'skaki=skaki.cli:main',
        ],
    },
    project_urls={  # Optional
        'Source': 'https://github.com/romerocesar/skaki/',
    },
)
