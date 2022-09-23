import pytest
import pathlib
import os
import filecmp

from cmaketools.updatesources import update_sources


class Arguments:
    pass


def test_update_sources(resources_path, generated_path):
    generated_output_folder = generated_path.joinpath("updatesources")
    generated_output_file = str(generated_output_folder.joinpath("generated_output"))

    os.makedirs(str(generated_output_folder), exist_ok=True)

    # GIVEN
    args = Arguments()
    args.path = str(resources_path.joinpath("updatesources"))
    args.input = "sample_input"
    args.output = generated_output_file

    # WHEN
    update_sources(args)

    # THEN
    sample_output_file = str(pathlib.Path(resources_path).joinpath("updatesources", "sample_output"))

    assert filecmp.cmp(sample_output_file, generated_output_file, False)
