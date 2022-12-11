import io
from pathlib import Path

import pytest

from simple_file_sorter import FileSorter, core


class TestFileSorter:
    def test_init_without_params(self):
        sorter = FileSorter()
        assert str(sorter.path) == "."
        assert str(sorter.dest_path) == core.DEFAULT_DEST_DIR

    @pytest.mark.parametrize("test_dir", ["test_dir", "../test_dir/test_dir"])
    def test_init_with_path(self, test_dir):
        sorter = FileSorter(path=test_dir)
        assert str(sorter.path) == test_dir
        assert str(sorter.dest_path) == str(
            Path(test_dir).joinpath(core.DEFAULT_DEST_DIR)
        )

    def test_init_with_dest_path(self):
        test_dest_dir = "test_dest_dir"
        sorter = FileSorter(dest_path=test_dest_dir)
        assert str(sorter.dest_path) == test_dest_dir

    def test_get_files(self, create_files, files_list):
        sorter = FileSorter(path=create_files)
        assert type(sorter._get_files()) == list
        assert len(sorter._get_files()) == len(files_list)
        assert all([x in [x.name for x in sorter._get_files()] for x in files_list])

    def test_get_files_with_subdirectories(
        self, create_files_with_subdirectories, files_list
    ):
        sorter = FileSorter(path=create_files_with_subdirectories)
        assert type(sorter._get_files()) == list
        assert len(sorter._get_files()) == len(files_list)
        assert all([x in [x.name for x in sorter._get_files()] for x in files_list])

    @pytest.mark.parametrize("file_name", ["test.abc", "test.123", "test.abc.123"])
    def test_get_folder_name_for_file(self, file_name, monkeypatch):
        file = Path(file_name)
        assert FileSorter.get_folder_name(file) == file_name.split(".")[-1]

    def test_sort(self, create_files, files_list, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "y")
        sorter = FileSorter(path=create_files)
        sorter.sort()
        assert all(
            [
                x.split(".")[-1] in [x.name for x in Path(sorter.dest_path).glob("*")]
                for x in files_list
            ]
        )
