from typing import Mapping, Callable, Tuple


def overridedict(
    d: dict, by: dict,
    replace_if: Callable[[dict], bool] = None,
):
    """Recursively update a dict by another in-place.

    Parameters
    ----------
    d: `dict`
        The `dict` to be updated.
    by: `dict`
        The `dict` that overrides `d`.
    replace_if: `Callable[[dict], bool]`
        If specified, replace the sub-`dict` if this predicate returned `True`.
    """
    for k, v in by.items():
        if (
            isinstance(v, Mapping) and k in d and (
                replace_if is None or
                not replace_if(d[k])
            )
        ):
            overridedict(d[k], v, replace_if)
        else:
            d[k] = v


class keys_all_in:
    "Predicate factory if all keys of a dict is in the specified list."
    def __init__(self, keys: Tuple[str]):
        self._keys = keys

    def __call__(self, d: dict) -> bool:
        return all(k in self._keys for k in d.keys())


is_timedelta = keys_all_in(
    ("days", "hours", "minutes", "seconds", "microseconds")
)
"Predicate to test if a dict is a parameter set for `timedelta`."
