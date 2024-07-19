from unittest.mock import MagicMock

import pytest

from app.application.uses_cases.crud_employee import CRUDEmployee
from app.infrastructure.api.statuses import ResultsNotFound


def test_get_employee_not_found(employee_repository):

    employee_repository.get_by_id = MagicMock(return_value=None)

    crud = CRUDEmployee(
        employee_repository=employee_repository
    )

    with pytest.raises(ResultsNotFound):
        employee = crud.get_by_id("123456")


def test_get_employee_found(employee_repository, employee_1, paginate_dto):
    employee_repository.get_all = MagicMock(return_value=([employee_1], 1))
    crud = CRUDEmployee(
        employee_repository=employee_repository
    )

    result = crud.all_employees(paginate_dto)

    assert result.page == paginate_dto.page
    assert len(result.results) <= paginate_dto.limit
    assert result.results[0] == employee_1
