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
$ extsorter -h

usage: extsorter [-h] [-d DST] [src]

Sort files by extension

positional arguments:
  src                source dir

options:
  -h, --help         show this help message and exit
  -d DST, --dst DST  destination dir
```

## Example

Sort files in current directory to a folder called `sorted` (name by default):

```bash
$ extsorter
```

Sort files in `~/Downloads` to `~/Downloads/old`:

```bash
$ extsorter ~/Downloads -d ~/Downloads/old
```

# Development

## Install

```bash
$ poetry install
```

## Tests

```bash
$ poetry run make test
```

## Linters

```bash
$ poetry run make format
```
