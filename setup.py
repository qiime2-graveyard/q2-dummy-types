# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-dummy-types",
    version='2017.2.0',
    license='BSD-3-Clause',
    url='https://qiime2.org',
    packages=find_packages(),
    install_requires=['qiime2 == 2017.2.*'],
    author="Jai Ram Rideout",
    author_email="jai.rideout@gmail.com",
    description="Dummy QIIME 2 types to serve as examples for plugin "
                "developers.",
    # Use the 'qiime2.plugins' entry point to make this plugin discoverable by
    # the QIIME 2 framework. The path after the equals sign (=) is the full
    # import path to a `qiime2.plugin.Plugin` object. This object can be
    # located anywhere within the package.
    entry_points={
        'qiime2.plugins':
        ['q2-dummy-types=q2_dummy_types.plugin_setup:plugin']
    },
    package_data={
        'q2_dummy_types.tests': ['data/*']
    }
)
