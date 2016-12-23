# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pkg_resources
import unittest
import uuid

import qiime2.core.archive as archive
from qiime2.sdk import Artifact

from q2_dummy_types import IntSequence1, IntSequence2


class TestIntSequence(unittest.TestCase):
    def test_data_import(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/int-sequence.txt')

        for type in IntSequence1, IntSequence2:
            # `Artifact.import_data` copies `int-sequence.txt` into the
            # artifact after peforming validation on the file.
            artifact = Artifact.import_data(type, fp)

            self.assertEqual(artifact.type, type)
            self.assertIsInstance(artifact.uuid, uuid.UUID)

    def test_reader_transformer(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/int-sequence.txt')

        for type in IntSequence1, IntSequence2:
            artifact = Artifact.import_data(type, fp)
            # `Artifact.view` invokes the transformer that handles
            # the `SingleIntFormat` -> `list` transformation.
            self.assertEqual(artifact.view(list), [42, -1, 9, 10, 0, 999, 0])

    def test_writer_transformer(self):
        for type in IntSequence1, IntSequence2:
            # `Artifact._from_view` invokes transformer that handles `list` ->
            # `SingleIntFormat`, because the `SingleIntDirectoryFormat` has
            # been registered as the directory format for the semantic type.
            # We didn't define a `SingleIntDirectoryFormat` ->
            # `SingleIntFormat` tranformer because
            # `model.SingleFileDirectoryFormat` handles that transformation for
            # us.
            artifact = Artifact._from_view(type, [1, 2, 42, -999, 42, 0], list,
                                           archive.ImportProvenanceCapture())
            # Test that the directory and file format can be read again.
            self.assertEqual(artifact.view(list), [1, 2, 42, -999, 42, 0])


if __name__ == "__main__":
    unittest.main()
