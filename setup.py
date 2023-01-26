from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in adabox/__init__.py
from adabox import __version__ as version

setup(
	name="adabox",
	version=version,
	description="Service app for Computer Service",
	author="Pablo Heredia",
	author_email="pablo@salvatumac.com.ar",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
