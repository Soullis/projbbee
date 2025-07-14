from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'pacote_cap'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriel',
    maintainer_email='g.solis.gabriel@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'objc_detector_pub = pacote_cap.objc_detector_pub:main',
        'objc_detector_sub = pacote_cap.objc_detector_sub:main'
        ],
    },
)
