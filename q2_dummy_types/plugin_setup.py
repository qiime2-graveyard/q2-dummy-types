# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime.plugin

import q2_dummy_types

plugin = qiime.plugin.Plugin(
    name='dummy-types',
    version=q2_dummy_types.__version__,
    website='https://github.com/qiime2/q2-dummy-types',
    package='q2_dummy_types'
)

importlib.import_module('q2_dummy_types._int_sequence')
importlib.import_module('q2_dummy_types._mapping')
