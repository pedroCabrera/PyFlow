import random

from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core.Common import *


class RandomLib(FunctionLibraryBase):
    """doc string for RandomLib"""

    def __init__(self, packageName):
        super(RandomLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, meta={'Category': 'Math|random', 'Keywords': [], "CacheEnabled": False})
    # Return a random integer N such that a <= N <= b
    def randint(start=('IntPin', 0), end=('IntPin', 10), Result=("Reference", ('IntPin', 0))):
        """Return a random integer N such that a <= N <= b."""
        Result(random.randint(start, end))

    @staticmethod
    @IMPLEMENT_NODE(returns=None, meta={'Category': 'Math|random', 'Keywords': []})
    # Shuffle the sequence x in place
    def shuffle(seq=('AnyPin', [],{"constraint": "1"}), Result=("Reference", ('AnyPin', [],{"constraint": "1"}))):
        """Shuffle the sequence x in place."""
        random.shuffle(seq)
        Result(seq)
