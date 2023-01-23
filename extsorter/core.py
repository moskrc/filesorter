import argparse
import os
import pathlib

DEFAULT_DST_FOLDER = "sorted"


class FileSorter:
    def __init__(self, path: str, dest_path: str = "sorted") -> None:
        self.path = pathlib.Path(path)
        self.files = self._get_files()
        self.dest_path = pathlib.Path(dest_path)

    def _get_files(self) -> list[pathlib.Path]:
        files = []
        for item in pathlib.Path(self.path).glob("*"):
            if item.is_file():
                files.append(item)
        return files

    @staticmethod
    def get_folder_name(file: pathlib.Path) -> str:
        return file.suffix.lower()[1:]

    def sort(self) -> None:
        msg = (
            f"Sort {len(self.files)} files in {self.path.absolute()} "
            f"to {self.dest_path.absolute()}? [Y/n] "
        )
        try:
            if input(msg).lower() not in ["y", ""]:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            return

        for file in self.files:
            if file.suffix:
                dest_folder = self.dest_path.joinpath(self.get_folder_name(file))
                dest_folder.mkdir(exist_ok=True, parents=True)
                file.rename(dest_folder.joinpath(file.name))

        print("Done")


def sort():
    parser = argparse.ArgumentParser(prog='extsorter', description="Sort files by extension")
    parser.add_argument("src", nargs='?', help="source dir", default=os.getcwd())
    parser.add_argument("-d", "--dst", help="destination dir", default=DEFAULT_DST_FOLDER, required=False)
    args = parser.parse_args()

    FileSorter(args.src, args.dst).sort()
