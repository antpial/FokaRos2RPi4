from setuptools import find_packages, setup

package_name = 'thruster_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
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
            'thruster_driver = thruster_driver.thruster_driver:main',
            'keyboard_controller = thruster_driver.keyboard_controller:main',
        ],
    },
)
