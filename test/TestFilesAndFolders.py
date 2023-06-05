from pathlib import Path

from FilesAndFolders import FilesAndFolders
import unittest


def add(num, num2):
    total = num + num2
    return total


class TestFilesAndFolders(unittest.TestCase):
    # def test_create_folder(self):
    #     files = FilesAndFolders
    #     path = Path()
    #     result = files.create_folder(files, location="master")
    def test_add(self):
        result = add(4, 4)
        assert(8, result)