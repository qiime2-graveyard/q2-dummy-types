# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-dummy-types",
    # TODO stop duplicating version string
    version="0.0.1",
    packages=find_packages(),
    install_requires=['qiime >= 2.0.0'],
    author="Jai Ram Rideout",
    author_email="jai.rideout@gmail.com",
    description="Dummy QIIME 2 types to serve as examples for plugin "
                "developers.",
    license='BSD-3-Clause',
    url="https://github.com/qiime2/q2-dummy-types",
    entry_points={
        'qiime.plugins':
        ['q2-dummy-types=q2_dummy_types.plugin_setup:plugin']
    },
    package_data={
        'q2_dummy_types.tests': ['data/*']
    }
)
