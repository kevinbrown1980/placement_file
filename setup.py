from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in placement_file/__init__.py
from placement_file import __version__ as version

setup(
	name="placement_file",
	version=version,
	description="Digital Placement File",
	author="Kevin Brown",
	author_email="kevin.brown@infinics.co.uk",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
