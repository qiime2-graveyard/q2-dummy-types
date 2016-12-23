# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pkg_resources

# Skip flake8 validation to avoid import cycle.
__version__ = pkg_resources.get_distribution('q2-dummy-types').version  # noqa

# Make the types defined in this plugin importable from the top-level package
# so they can be easily imported by other plugins relying on these types.
from ._int_sequence import IntSequence1, IntSequence2
from ._mapping import Mapping

__all__ = ['IntSequence1', 'IntSequence2', 'Mapping']
