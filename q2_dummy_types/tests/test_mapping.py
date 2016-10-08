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
    def test_data_import(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/mapping.tsv')

        # `Artifact.import_data` copies `mapping.tsv` into the artifact after
        # performing validation on the file.
        artifact = Artifact.import_data(Mapping, fp)

        self.assertEqual(artifact.type, Mapping)
        self.assertIsInstance(artifact.uuid, uuid.UUID)

    def test_reader_transformer(self):
        fp = pkg_resources.resource_filename(
            'q2_dummy_types.tests', 'data/mapping.tsv')

        artifact = Artifact.import_data(Mapping, fp)
        # `Artifact.view` invokes the transformer that handles the
        # `MappingFormat` -> `dict` transformation.
        self.assertEqual(artifact.view(dict),
                         {'foo': 'abc', 'bar': 'def', 'bazz': 'ghijkl'})

    def test_writer_transformer(self):
        # `Artifact._from_view` invokes transformer that handles `dict` ->
        # `MappingFormat`, because the `MappingDirectoryFormat` has
        # been registered as the directory format for the semantic type.
        # We didn't define a `MappingDirectoryFormat` ->
        # `MappingFormat` tranformer because
        # `model.SingleFileDirectoryFormat` handles that transformation for
        # us.
        artifact = Artifact._from_view(Mapping, {'abc': 'cat', 'def': 'dog'},
                                       dict)
        # Test that the directory and file format can be read again.
        self.assertEqual(artifact.view(dict), {'abc': 'cat', 'def': 'dog'})


if __name__ == "__main__":
    unittest.main()
