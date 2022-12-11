# FileSorter - A simple file sorter

## What is it?

Sometimes you have a folder with a lot of files, and you want 
to sort them into folders. This is where FileSorter comes in. 
It will sort your files into folders based on the file extension.

## How to install

```bash
$ pip install simple_file_sorter
```

## How to use
```bash
usage: simple_file_sorter [-h] [-s SRC] [-d DST]

File sorter

options:
  -h, --help         show this help message and exit
  -s SRC, --src SRC  Source dir
  -d DST, --dst DST  Destination dir
```

## Example

```bash
$ simple_file_sorter -s ~/Downloads
```