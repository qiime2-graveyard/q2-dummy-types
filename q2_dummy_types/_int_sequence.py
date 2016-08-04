# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os.path

import qiime.plugin

from .plugin_setup import plugin

# Define semantic types.
IntSequence1 = qiime.plugin.SemanticType('IntSequence1')
IntSequence2 = qiime.plugin.SemanticType('IntSequence2')

# Register semantic types on the plugin.
plugin.register_semantic_type(IntSequence1)
plugin.register_semantic_type(IntSequence2)


###############################################################################
#
# int-sequence:
#
#     A sequence of integers stored in a single file. Since this is a sequence,
#     the integers have an order and repetition of elements is allowed.
#
###############################################################################

# Define a file format for use in the data layout defined below.
class IntSequenceFormat(qiime.plugin.FileFormat):
    name = 'int-sequence'

    # Sniffers are used when importing data into a data layout. A sniffer
    # determines whether a file appears to conform to its file format. Sniffers
    # should only read a small piece of the file to determine membership and
    # should not rely on file extension.
    @classmethod
    def sniff(cls, filepath):
        with open(filepath, 'r') as fh:
            for line, _ in zip(fh, range(5)):
                try:
                    int(line.rstrip('\n'))
                except (TypeError, ValueError):
                    return False
            return True

# Define a data layout with name 'int-sequence' and version 1. A data layout is
# a directory structure composed of one or more files (nested directories are
# also supported). Each file has a specific file format associated with it.
# This data layout only has a single file, ints.txt, with file format
# `IntSequenceFormat`.
int_sequence_data_layout = qiime.plugin.DataLayout('int-sequence', 1)
int_sequence_data_layout.register_file('ints.txt', IntSequenceFormat)

# Register the data layout on the plugin.
plugin.register_data_layout(int_sequence_data_layout)

# Register the data layout with the semantic types defined above. A data layout
# can be registered to multiple semantic types. Currently, a semantic type can
# only have a single data layout associated with it.
plugin.register_type_to_data_layout(IntSequence1, 'int-sequence', 1)
plugin.register_type_to_data_layout(IntSequence2, 'int-sequence', 1)


# Define a data layout reader for reading the data layout into a view type
# (`list` in this case). Any function name can be used but the convention is
# `<data-layout-name>_to_<view-type>`.
def int_sequence_to_list(data_dir):
    with open(os.path.join(data_dir, 'ints.txt'), 'r') as fh:
        view = []
        for line in fh:
            view.append(int(line.rstrip('\n')))
        return view


# Define a data layout writer for writing a view type into the data layout
# (`list` in this case). Any function name can be used but the convention is
# `<view-type>_to_<data-layout-name>`.
def list_to_int_sequence(view, data_dir):
    with open(os.path.join(data_dir, 'ints.txt'), 'w') as fh:
        for int_ in view:
            fh.write('%d\n' % int_)

# Register the data layout reader and writer with the data layout, specifying
# the associated view type for each. A data layout can have multiple readers
# and writers associated with it for different view types.
plugin.register_data_layout_reader('int-sequence', 1, list,
                                   int_sequence_to_list)

plugin.register_data_layout_writer('int-sequence', 1, list,
                                   list_to_int_sequence)
