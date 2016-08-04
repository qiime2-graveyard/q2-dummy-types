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

from q2_dummy_types import Mapping
from qiime.sdk import Artifact


class TestMapping(unittest.TestCase):
    def test_data_layout_import(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/mapping.tsv')

        # `Artifact.import_data` invokes the data layout importer.
        artifact = Artifact.import_data(Mapping, fp)

        self.assertEqual(artifact.type, Mapping)
        self.assertIn('importing data', artifact.provenance)
        self.assertIsInstance(artifact.uuid, uuid.UUID)
        self.assertEqual(artifact.view(dict),
                         {'foo': 'abc', 'bar': 'def', 'bazz': 'ghijkl'})

    def test_data_layout_reader(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/mapping.tsv')

        artifact = Artifact.import_data(Mapping, fp)
        # `Artifact.view` invokes the data layout reader.
        self.assertEqual(artifact.view(dict),
                         {'foo': 'abc', 'bar': 'def', 'bazz': 'ghijkl'})

    def test_data_layout_writer(self):
        # `Artifact._from_view` invokes the data layout writer.
        artifact = Artifact._from_view(
            {'abc': 'cat', 'def': 'dog'}, Mapping, None)
        # Test that the data layout can be read again.
        self.assertEqual(artifact.view(dict), {'abc': 'cat', 'def': 'dog'})


if __name__ == "__main__":
    unittest.main()
