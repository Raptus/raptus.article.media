from setuptools import setup, find_packages
import os

version = '2.0b7'

setup(name='raptus.article.media',
      version=version,
      description="Provides audio and video support for articles.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "MANUAL.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://raptus.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.flowplayer',
          'Products.ContentTypeValidator',
          'raptus.article.core',
          'plone.app.imaging',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
