# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

__version__ = "0.0.7.dev0"  # noqa

# Make the types defined in this plugin importable from the top-level package
# so they can be easily imported by other plugins relying on these types.
from ._int_sequence import IntSequence1, IntSequence2
from ._mapping import Mapping

__all__ = ['IntSequence1', 'IntSequence2', 'Mapping']
