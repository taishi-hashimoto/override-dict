from setuptools import setup
from setuptools import find_packages


package_dir = "src"

setup(
    name='overridedict',
    version="v1.0.0",
    description="Recursively update a dict by another.",
    package_dir={
        "": package_dir
    },
    packages=find_packages(package_dir),
    package_data={},
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
        ]
    },
    author="Taishi Hashimoto",
    author_email="hashimoto.taishi@outlook.com")
