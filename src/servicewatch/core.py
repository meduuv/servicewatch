from collections.abc import Mapping

def changed(previous: Mapping[str, str], current: Mapping[str, str]) -> dict[str, list[str]]:
    """Find service states that were added, removed, or changed."""
    old,new=set(previous),set(current)
    return {"added":sorted(new-old),"removed":sorted(old-new),"changed":sorted(k for k in old&new if previous[k]!=current[k])}
