from setuptools import setup, find_packages

setup(
    name='intermine_boot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'gitpython',
        'xdg',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        intermine_boot=intermine_boot:cli
    ''',
)
