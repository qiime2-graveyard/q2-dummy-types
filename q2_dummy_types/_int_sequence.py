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

IntSequence1 = qiime.plugin.SemanticType('IntSequence1')
IntSequence2 = qiime.plugin.SemanticType('IntSequence2')

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

class IntSequenceFormat(qiime.plugin.FileFormat):
    name = 'int-sequence'

    @classmethod
    def sniff(cls, filepath):
        with open(filepath, 'r') as fh:
            for line, _ in zip(fh, range(5)):
                try:
                    int(line.rstrip('\n'))
                except (TypeError, ValueError):
                    return False
            return True

int_sequence_data_layout = qiime.plugin.DataLayout('int-sequence', 1)
int_sequence_data_layout.register_file('ints.txt', IntSequenceFormat)

plugin.register_data_layout(int_sequence_data_layout)
plugin.register_type_to_data_layout(IntSequence1, 'int-sequence', 1)
plugin.register_type_to_data_layout(IntSequence2, 'int-sequence', 1)


def int_sequence_to_list(data_dir):
    with open(os.path.join(data_dir, 'ints.txt'), 'r') as fh:
        view = []
        for line in fh:
            view.append(int(line.rstrip('\n')))
        return view


def list_to_int_sequence(view, data_dir):
    with open(os.path.join(data_dir, 'ints.txt'), 'w') as fh:
        for int_ in view:
            fh.write('%d\n' % int_)


plugin.register_data_layout_reader('int-sequence', 1, list,
                                   int_sequence_to_list)

plugin.register_data_layout_writer('int-sequence', 1, list,
                                   list_to_int_sequence)
