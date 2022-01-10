from typing import Any, TypeVar

from torchvision.prototype import features
from torchvision.prototype.transforms import Transform


T = TypeVar("T", bound=features.Feature)


class Identity(Transform):
    def _dispatch(self, feature: T, **params: Any) -> T:
        return feature
