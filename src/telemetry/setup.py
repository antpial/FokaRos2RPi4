from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'telemetry'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=['telemetry', 'telemetry.*'], exclude=['test']),
    package_data={
        'telemetry': ['loralib.so'],
    },

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='foka',
    maintainer_email='275411@student.pwr.edu.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telemetry = telemetry.telemetry:main',
        ],
    },
)
