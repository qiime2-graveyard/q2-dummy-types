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
IntSequence1 = qiime.plugin.SemanticType('IntSequence1')
IntSequence2 = qiime.plugin.SemanticType('IntSequence2')

# Register semantic types on the plugin.
plugin.register_semantic_types(IntSequence1, IntSequence2)


###############################################################################
#
# int-sequence:
#
#     A sequence of integers stored in a single file. Since this is a sequence,
#     the integers have an order and repetition of elements is allowed.
#
###############################################################################

# Define a file format for use in the directory format defined below.
class IntSequenceFormat(model.TextFileFormat):
    # Sniffers are used when reading and writing data from a file. A sniffer
    # determines whether a file appears to conform to its file format. Sniffers
    # should only read a small piece of the file to determine membership and
    # should not rely on file extension.
    def sniff(self):
        with self.open() as fh:
            for line, _ in zip(fh, range(5)):
                try:
                    int(line.rstrip('\n'))
                except (TypeError, ValueError):
                    return False
            return True

# Define a directory format. A directory format is a directory structure
# composed of one or more files (nested directories are also supported). Each
# file has a specific file format associated with it.  This directory format
# only has a single file, ints.txt, with file format `IntSequenceFormat`.
IntSequenceDirectoryFormat = model.SingleFileDirectoryFormat(
    'IntSequenceDirectoryFormat', 'ints.txt', IntSequenceFormat)

# Register the formats defined above. Formats must be unique across all
# plugins installed on a users system.
plugin.register_formats(IntSequenceFormat, IntSequenceDirectoryFormat)

# Register the directory format with the semantic types defined above. A
# directory format can be registered to multiple semantic types. Currently, a
# semantic type can only have a single directory format associated with it.
plugin.register_semantic_type_to_format(
    IntSequence1,
    artifact_format=IntSequenceDirectoryFormat)
plugin.register_semantic_type_to_format(
    IntSequence2,
    artifact_format=IntSequenceDirectoryFormat)


# Define a transformer for converting a file format (`IntSequenceFormat`) into
# a view type (`list` in this case). To indicate that only the QIIME 2
# Framework should interact with a transformer, a non-meaningful name is used.
# The convention is `_<int counter>`, but anything is acceptable. The aim is to
# draw the reader to the function annotations, which convey precisely what the
# transformer is responsible for.
@plugin.register_transformer
def _1(ff: IntSequenceFormat) -> list:
    with ff.open() as fh:
        data = []
        for line in fh:
            data.append(int(line.rstrip('\n')))
        return data


# Define a transformer for converting a view type (`list` in this case) to the
# file format (`IntSequenceFormat`). To indicate that only the QIIME 2
# Framework should interact with a transformer, a non-meaningful name is used.
# The convention is `_<int counter>`, but anything is acceptable. The aim is to
# draw the reader to the function annotations, which convey precisely what the
# transformer is responsible for.
@plugin.register_transformer
def _2(data: list) -> IntSequenceFormat:
    ff = IntSequenceFormat()
    with ff.open() as fh:
        for int_ in data:
            fh.write('%d\n' % int_)
    return ff
