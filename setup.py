from setuptools import find_packages, setup

package_name = 'dexhand_usb_serial'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','pyserial'],
    zip_safe=True,
    maintainer='Trent Shumay',
    maintainer_email='trent@iotdesignshop.com',
    description='ROS 2 Package for Connecting to DexHand Firmware Serial Interface via USB ',
    license='CC BY-NC-SA 4.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'usb_serial = dexhand_usb_serial.usb_serial:main',
        ],
    },
)
