from setuptools import setup, find_packages


setup(
    name='python_demo',
    version='0.1',
    description='代码质量控制demo',
    author='xxc',
    packages=find_packages("src"),
    package_dir={
        '': 'src'
    },
    package_data={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[

    ],
    entry_points={
    }
)
