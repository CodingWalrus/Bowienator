from setuptools import setup,find_packages

setup(
	name='bowienator',
	version='1.0.0',
	description='A program that detects faces in photos and places a picture of David Bowie over top.',
	author = 'James Wash',
	author_email = 'jamescwash2@hotmail.com',
	url = 'https://github.com/CodingWalrus/Bowienator',
	packages=setuptools.find_packages(),
	include_package_data=True,
	license='MIT',
	long_description=read('README.md')
	long_description_content_type="text/markdown"
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Topic :: Games/Entertainment",
		"Topic :: Multimedia :: Graphics"
	),
)