from pytest import fixture, raises

from pyapp.files import TemperatureFile


@fixture
def temperature_file():
    file = TemperatureFile()
    file.load("tests/fixtures/data.csv")

    return file


def test_temperature_file_rows(temperature_file):
    assert temperature_file.rows == 20


def test_temperature_file_avg(temperature_file):
    assert 20 < temperature_file.avg < 30


def test_temperature_file_not_loaded():
    file = TemperatureFile()

    with raises(TypeError):
        file.rows

    with raises(TypeError):
        file.avg
