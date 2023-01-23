# ExtSorter - A simple file sorter

## What is it?

Sometimes you have a folder with a lot of files, and you want
to sort them into folders. This is where ExtSorter comes in.
It will sort your files into folders based on the file extension.

## How to install

```bash
$ pip install extsorter
```

## How to use
```bash
usage: extsorter [-h] [-s SRC] [-d DST]

Sort files by extension

options:
  -h, --help         show this help message and exit
  -s SRC, --src SRC  Source dir
  -d DST, --dst DST  Destination dir
```

## Example

Sort files in `~/Downloads` into `~/Downloads/sorted`:
```bash
$ extsorter -s ~/Downloads
```

# Development

## Tests

```bash
$ poetry run make test
```

## Linters

```bash
$ poetry run make format
```
