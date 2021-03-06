#!usr/bin/python
from setuptools import setup , find_packages
setup (
	name = 'GitMiner',
	description = 'An application getting Git stats',
	version = '0.10',
	packages = find_packages(), # list of all packages
    	install_requires = ['colorama'],
    	python_requires='>=3.6', # any python greater than 3.7
	test_suite="tests", # where to find tests
	entry_points = {
		'console_scripts': [
			'gitstat=gitstat.__main__:main',
			'gitstar-performer=gitlog_committer.__main__:main'
			]
		}
	)

