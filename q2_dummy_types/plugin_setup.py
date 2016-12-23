# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime2.plugin

import q2_dummy_types

plugin = qiime2.plugin.Plugin(
    name='dummy-types',
    version=q2_dummy_types.__version__,
    website='https://github.com/qiime2/q2-dummy-types',
    package='q2_dummy_types'
)

# It is important that any modules registering functionality onto the
# `qiime2.plugin.Plugin` object are imported so the registrations take place.
# When the QIIME 2 framework discovers plugin objects, it only imports the
# module where the plugin is defined, so any modules that register
# functionality onto this object must also be imported. If registrations happen
# in the same module as the plugin object this step is not necessary.
importlib.import_module('q2_dummy_types._int_sequence')
importlib.import_module('q2_dummy_types._mapping')
