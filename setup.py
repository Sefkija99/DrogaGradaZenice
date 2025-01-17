"""
Upload to PyPI
python setup.py sdist
twine upload --repository pypitest dist/dutycalls_sdk-X.X.X.tar.gz
twine upload --repository pypi dist/dutycalls_sdk-X.X.X.tar.gz
"""
from setuptools import setup, find_packages
from dutycalls import __version__

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except IOError:
    long_description = '''
The DutyCalls.me SDK can be used to make API request to DutyCalls.me.
'''.strip()

setup(
    name='dutycalls_sdk',
    version=__version__,
    description='DutyCalls.me SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/transceptor-technology/python-dutycalls-sdk',
    author='Jeroen van der Heijden',
    author_email='jeroen@transceptor.technology',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are:
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'aiohttp',
        'deprecation'
    ],
    keywords='sdk connector',

    # You can just specify the packages manually here if your project is
    # simple. Or, you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
