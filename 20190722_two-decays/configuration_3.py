from assess.algorithms.distances.startdistance import StartDistance
from assess.algorithms.incrementaldistancealgorithm import IncrementalDistanceAlgorithm
from assess.algorithms.signatures.pqgramsignature import PQGramSignature
from assess.algorithms.signatures.signatures import ParentChildByNameTopologySignature
from assess.decorators.distancematrixdecorator import DistanceMatrixDecorator


def build_decorator():
    decorator = DistanceMatrixDecorator()
    return decorator


def algorithm(**kwargs):
    return IncrementalDistanceAlgorithm(distance=StartDistance, **kwargs)


configurations = [{
    "signatures": [
        ParentChildByNameTopologySignature,
        PQGramSignature
    ],
    "algorithms": [algorithm],
    "decorator": build_decorator
}]
