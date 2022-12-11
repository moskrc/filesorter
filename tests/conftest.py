import pytest


@pytest.fixture
def files_list():
    return ["1.avi", "2.mov", "3.mp3"]


@pytest.fixture
def create_files(files_list, tmp_path):
    for f in files_list:
        tmp_path.joinpath(f).touch()

    yield tmp_path


@pytest.fixture
def files_list_with_subdirectories(files_list):
    return ["alfa/", "foo/2.txt", "bar/3.txt"] + files_list


@pytest.fixture
def create_files_with_subdirectories(files_list_with_subdirectories, tmp_path):
    for f in files_list_with_subdirectories:
        path = tmp_path.joinpath(f)
        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        else:
            path.mkdir(parents=True, exist_ok=True)

    yield tmp_path
