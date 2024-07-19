from unittest.mock import MagicMock

import pytest

from app.application.uses_cases.crud_product import CRUDProduct
from app.application.uses_cases.crud_stores import CRUDStores
from app.infrastructure.api.statuses import ResultsNotFound


def test_get_store_not_found(store_repository):

    store_repository.get_by_id = MagicMock(return_value=None)

    crud = CRUDStores(
        stores_repository=store_repository
    )

    with pytest.raises(ResultsNotFound):
        crud.get_by_id("0000")


def test_get_store_found(store_repository, store_1, paginate_dto):
    store_repository.get_all = MagicMock(return_value=([store_1], 1))
    crud = CRUDStores(
        stores_repository=store_repository
    )

    result = crud.all(paginate_dto)

    assert result.page == paginate_dto.page
    assert result.total_pages == 1
    assert result.results[0] == store_1
