"""base file for the application."""

from typing import Any, List, Union

from fastapi import FastAPI
from fastapi.params import Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items")
def read_items(
    q: Annotated[Union[str, None], Query(max_length=20, min_length=5)] = None,
):
    """query param validation

    Args:
    ----
        item (Item): data for item

    Returns:
    -------
        created item
    """
    results: dict[str, Any] = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
    }
    if q:
        results.update({"q": q})
    return results


@app.get("/items/list")
async def read_items_list(q: Annotated[Union[List[str], None], Query()] = None):
    """query parameter list/multiple values

    Args:
    ----
        q: list of values

    Returns:
    -------
        items list
    """
    query_items = q
    return query_items


@app.get("/items/meta")
async def read_items_meta(
    q: Annotated[
        Union[List[str], None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            deprecated=True,
        ),
    ] = None,
    hidden_query: Annotated[
        Union[str, None], Query(include_in_schema=False)
    ] = None,
):
    """example with metadata in Query

    Args:
    ----
        q: list of values

    Returns:
    -------
        items list
    """
    _ = hidden_query
    query_items = q
    return query_items
