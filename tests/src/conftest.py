import pytest
import pathlib


@pytest.fixture
def tests_path():
    return pathlib.Path(__file__).parent.parent.resolve()


@pytest.fixture
def resources_path(tests_path):
    return tests_path.joinpath("resources").resolve()


@pytest.fixture
def generated_path(tests_path):
    return tests_path.joinpath("generated").resolve()
