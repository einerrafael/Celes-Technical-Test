from unittest.mock import MagicMock

import pytest

from app.application.uses_cases.crud_employee import CRUDEmployee
from app.application.uses_cases.crud_product import CRUDProduct
from app.infrastructure.api.statuses import ResultsNotFound


def test_get_product_not_found(product_repository):

    product_repository.get_by_id = MagicMock(return_value=None)

    crud = CRUDProduct(
        product_repository=product_repository
    )

    with pytest.raises(ResultsNotFound):
        crud.get_by_id("ABC")


def test_get_products_found(product_repository, product_1, paginate_dto):
    product_repository.get_all = MagicMock(return_value=([product_1], 1))
    crud = CRUDEmployee(
        employee_repository=product_repository
    )

    result = crud.all_employees(paginate_dto)

    assert result.page == paginate_dto.page
    assert result.total_pages == 1
    assert result.results[0] == product_1
