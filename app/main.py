"""base file for the application."""

from typing import Any, Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
def read_items(
    item_id: Annotated[
        int, Path(description="The ID of the item to get", gt=5, le=10)
    ],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    """path param validation

    Args:
    ----
        item (Item): data for item

    Returns:
    -------
        created item
    """
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
