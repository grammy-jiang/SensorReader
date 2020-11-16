"""
setup.py for Sensor Reader
"""
from setuptools import find_packages, setup

import versioneer

setup(
    name="Sensor-Reader",
    cmdclass=versioneer.get_cmdclass(),
    version=versioneer.get_version(),
    description="Read the sensors data and send to backends",
    long_description="",
    url="",
    author="Grammy Jiang",
    author_email="grammy.jiang@gmail.com",
    classifiers=[],
    keywords="Raspberry Pi",
    project_urls={},
    packages=find_packages(),
    install_requires=[
        "aiofiles",
        "aiokafka",
        "apscheduler",
        "asyncpg",
        "cachetools",
        "motor",
        "sense-hat",
        "uvloop",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "sensor_reader=sensor_reader.cli:main",
        ],
    },
)
