import pytest
import toml


from updatesources.cli import main


def test_version():
    main(["--version"])

