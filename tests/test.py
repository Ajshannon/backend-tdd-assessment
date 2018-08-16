
import unittest
import echo
import subprocess


class TestMe(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        # usage = "a"

        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '-u', 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "HELLO"

        self.assertEquals(stdout.strip('\n'), expected)

    def test_upper2(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '--upper', 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "HELLO"

        self.assertEquals(stdout.strip('\n'), expected)
    
    def test_lower(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '-l', 'Hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "hello"

        self.assertEquals(stdout.strip('\n'), expected)

    def test_lower2(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '--lower', 'Hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "hello"

        self.assertEquals(stdout.strip('\n'), expected)

    def test_title(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '-t', 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "Hello"

        self.assertEquals(stdout.strip('\n'), expected)

    def test_title2(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '--title', 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "Hello"

        self.assertEquals(stdout.strip('\n'), expected)
    
    def test_all(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '-tul', 'heLLo!'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "Hello!"

        self.assertEquals(stdout.strip('\n'), expected)
    
    def test_all2(self):
        process = subprocess.Popen(
            ["python", "./echo.py", '-ul', 'heLLo!'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "hello!"

        self.assertEquals(stdout.strip('\n'), expected)
    
    def test_none(self):
        process = subprocess.Popen(
            ["python", "./echo.py", 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = "hello"

        self.assertEquals(stdout.strip('\n'), expected)
    # def test_text(self):
    #     args = ['hello word']
    #     namespace = self.parser.parse_args(args)
    #     self.assertEqual(namespace.text, 'hello World')


if __name__ == '__main__':
    unittest.main()
