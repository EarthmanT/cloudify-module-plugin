
from setuptools import setup


setup(

    # Do not use underscores in the plugin name.
    name='example-module-plugin',

    version='0.1',
    author='earthmant',

    packages=['module_plugin'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        "cloudify-plugins-common>=3.3.1"
    ]
)
