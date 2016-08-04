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

Mapping = qiime.plugin.SemanticType('Mapping')

plugin.register_semantic_type(Mapping)


###############################################################################
#
# mapping:
#
#     A mapping of keys to values stored in a single TSV file. Since this is a
#     mapping, key-value pairs do not have an order and duplicate keys are
#     disallowed.
#
###############################################################################

class MappingFormat(qiime.plugin.FileFormat):
    name = 'mapping'

    @classmethod
    def sniff(cls, filepath):
        with open(filepath, 'r') as fh:
            for line, _ in zip(fh, range(5)):
                cells = line.rstrip('\n').split('\t')
                if len(cells) != 2:
                    return False
            return True

mapping_data_layout = qiime.plugin.DataLayout('mapping', 1)
mapping_data_layout.register_file('mapping.tsv', MappingFormat)

plugin.register_data_layout(mapping_data_layout)
plugin.register_type_to_data_layout(Mapping, 'mapping', 1)


def mapping_to_dict(data_dir):
    with open(os.path.join(data_dir, 'mapping.tsv'), 'r') as fh:
        view = {}
        for line in fh:
            key, value = line.rstrip('\n').split('\t')
            if key in view:
                raise ValueError(
                    "mapping.txt file must have unique keys. Key %r was "
                    "observed more than once." % key)
            view[key] = value
        return view


def dict_to_mapping(view, data_dir):
    with open(os.path.join(data_dir, 'mapping.tsv'), 'w') as fh:
        for key, value in view.items():
            fh.write('%s\t%s\n' % (key, value))

plugin.register_data_layout_reader('mapping', 1, dict, mapping_to_dict)
plugin.register_data_layout_writer('mapping', 1, dict, dict_to_mapping)
