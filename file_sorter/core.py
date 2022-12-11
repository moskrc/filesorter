import pathlib
from typing import Iterable

DEFAULT_DEST_DIR = "sorted"


class FileSorter:
    def __init__(self, path: str = ".", dest_path: str = None) -> None:
        self.path = pathlib.Path(path)
        self.files = self._get_files()
        self.dest_path = (
            self.path.joinpath(DEFAULT_DEST_DIR)
            if not dest_path
            else pathlib.Path(dest_path)
        )

    def _get_files(self) -> Iterable[pathlib.Path]:
        files = []
        for item in pathlib.Path(self.path).glob("*"):
            if item.is_file():
                files.append(item)
        return files

    @staticmethod
    def get_folder_name(file: pathlib.Path) -> str:
        return file.suffix.lower()[1:]

    def sort(self) -> None:
        answer = input(
            f"Sort {len(self.files)} files in {self.path.absolute()} to "
            f"{self.dest_path.absolute()}? [y/n] "
        )

        if answer.lower() != "y":
            return

        for file in self.files:
            if file.suffix:
                dest_folder = self.dest_path.joinpath(self.get_folder_name(file))
                dest_folder.mkdir(exist_ok=True, parents=True)
                file.rename(dest_folder.joinpath(file.name))


def sort():
    FileSorter().sort()
