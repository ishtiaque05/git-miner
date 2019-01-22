#!usr/bin/python
from setuptools import setup , find_packages
setup (
	name = 'git-miner',
	description = 'Cli to show all the git status',
	version = '0.10',
	packages = find_packages(), # list of all packages
    	install_requires =  ['colorama'],
    	python_requires='>=2.7', # any python greater than 2.7
	test_suite="tests", # where to find tests
	entry_points = {
		'console_scripts': [
			'git-stat = git-stat.__main__:main'
			]
		}
	)
