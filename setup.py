import sys
from setuptools import setup


def description_text():
    return 'Composite beam design to AS/NZS2327-2017.'


def readme():
    with open('README.md') as f:
        return f.read()


if (sys.version_info[0] < 3 or
        sys.version_info[0] == 3 and sys.version_info[1] < 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

install_requires = ['numpy', 'matplotlib']

setup(name='compbeam',
      version='0.0.1',
      description=description_text(),
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Scientific/Engineering',
      ],
      url='https://github.com/robbievanleeuwen/compbeam',
      author='Robbie van Leeuwen',
      author_email='robbie.vanleeuwen@gmail.com',
      license='MIT',
      packages=['compbeam'],
      install_requires=install_requires,
      include_package_data=True,
      zip_safe=False)
