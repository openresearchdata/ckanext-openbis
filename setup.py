from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-openbis',
    version=version,
    description="OpenBis/OAI-PMH  Harvester for CKAN",
    long_description="",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openbis'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'ckanext-oaipmh'
    ],
    entry_points=\
    """
    [ckan.plugins]
    openbis_harvester=ckanext.openbis.harvester:OpenbisHarvester
    [paste.paster_command]
    harvester=ckanext.openbis.command:OpenbisHarvesterCommand
    """,
)
