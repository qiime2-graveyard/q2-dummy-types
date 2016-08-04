# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pkg_resources
import unittest
import uuid

from q2_dummy_types import IntSequence1, IntSequence2
from qiime.sdk import Artifact


class TestIntSequence(unittest.TestCase):
    def test_data_layout_import(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/int-sequence.txt')

        for type in IntSequence1, IntSequence2:
            # `Artifact.import_data` invokes the data layout importer.
            artifact = Artifact.import_data(type, fp)

            self.assertEqual(artifact.type, type)
            self.assertIn('importing data', artifact.provenance)
            self.assertIsInstance(artifact.uuid, uuid.UUID)
            self.assertEqual(artifact.view(list), [42, -1, 9, 10, 0, 999, 0])

    def test_data_layout_reader(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/int-sequence.txt')

        for type in IntSequence1, IntSequence2:
            artifact = Artifact.import_data(type, fp)
            # `Artifact.view` invokes the data layout reader.
            self.assertEqual(artifact.view(list), [42, -1, 9, 10, 0, 999, 0])

    def test_data_layout_writer(self):
        for type in IntSequence1, IntSequence2:
            # `Artifact._from_view` invokes the data layout writer.
            artifact = Artifact._from_view([1, 2, 42, -999, 42, 0], type, None)
            # Test that the data layout can be read again.
            self.assertEqual(artifact.view(list), [1, 2, 42, -999, 42, 0])


if __name__ == "__main__":
    unittest.main()
