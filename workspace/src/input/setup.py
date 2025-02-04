from setuptools import find_packages, setup

package_name = 'input'

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
    maintainer='David',
    maintainer_email='deapen@wisc.edu',
    description='Input for merge_arrays',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'array1 = input.array1:main',
                'array2 = input.array2:main',
                'listener = input.merge_arrays_node:main',
        ],
    },
)
