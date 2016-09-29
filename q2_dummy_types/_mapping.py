# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime.plugin
import qiime.plugin.model as model

from .plugin_setup import plugin

# Define semantic types.
Mapping = qiime.plugin.SemanticType('Mapping')

# Register semantic types on the plugin.
plugin.register_semantic_types(Mapping)


###############################################################################
#
# mapping:
#
#     A mapping of keys to values stored in a single TSV file. Since this is a
#     mapping, key-value pairs do not have an order and duplicate keys are
#     disallowed.
#
###############################################################################

# Define a file format for use in the directory format defined below.
class MappingFormat(model.TextFileFormat):
    # Sniffers are used when reading and writing data from a file. A sniffer
    # determines whether a file appears to conform to its file format. Sniffers
    # should only read a small piece of the file to determine membership and
    # should not rely on file extension.
    def sniff(self):
        with self.open() as fh:
            for line, _ in zip(fh, range(5)):
                cells = line.rstrip('\n').split('\t')
                if len(cells) != 2:
                    return False
            return True

# Define a directory format. A directory format is a directory structure
# composed of one or more files (nested directories are also supported). Each
# file has a specific file format associated with it.  This directory format
# only has a single file, ints.txt, with file format `IntSequenceFormat`.
MappingDirectoryFormat = model.SingleFileDirectoryFormat(
    'MappingDirectoryFormat', 'mapping.tsv', MappingFormat)

# Register the formats defined above. Formats must be unique across all
# plugins installed on a users system.
plugin.register_formats(MappingFormat, MappingDirectoryFormat)

# Register the directory format with the semantic types defined above. A
# directory format can be registered to multiple semantic types. Currently, a
# semantic type can only have a single directory format associated with it.
plugin.register_semantic_type_to_format(
    Mapping,
    artifact_format=MappingDirectoryFormat)


# Define a transformer for converting a file format (`MappingFormat`) into a
# view type (`dict` in this case). To indicate that only the QIIME 2 Framework
# should interact with a transformer, a non-meaningful name is used. The
# convention is `_<int counter>`, but anything is acceptable. The aim is to
# draw the reader to the function annotations, which convey precisely what the
# transformer is responsible for.
@plugin.register_transformer
def _1(ff: MappingFormat) -> dict:
    with ff.open() as fh:
        data = {}
        for line in fh:
            key, value = line.rstrip('\n').split('\t')
            if key in data:
                raise ValueError(
                    "mapping.txt file must have unique keys. Key %r was "
                    "observed more than once." % key)
            data[key] = value
        return data


# Define a transformer for converting a view type (`dict` in this case) to the
# file format (`MappingFormat`). To indicate that only the QIIME 2 Framework
# should interact with a transformer, a non-meaningful name is used.  The
# convention is `_<int counter>`, but anything is acceptable. The aim is to
# draw the reader to the function annotations, which convey precisely what the
# transformer is responsible for.
@plugin.register_transformer
def _2(data: dict) -> MappingFormat:
    ff = MappingFormat()
    with ff.open() as fh:
        for key, value in data.items():
            fh.write('%s\t%s\n' % (key, value))
    return ff
