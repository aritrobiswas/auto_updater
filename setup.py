def setup_package():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup
	
	setup(
		name="BackupUtility",
		version="0.1.0",
		author="Aritro Biswas",
		author_email="aritro@celectengine.com",
		scripts=["backup/scripts/backuputil"],
		packages=[
			"backup"
		],
		include_package_data=True,
		license="LICENSE.txt",
		description=("automatically backs up specified directories to specified gcs buckets on specified times"),
		long_description=open("README.txt").read(),
		install_requires=[],
		)

if __name__ == "__main__":
	setup_package()