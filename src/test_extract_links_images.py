import unittest
from textnode import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):

    def test_extract_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        result = extract_markdown_images(text)
        expected = "[('image', 'https://i.imgur.com/zjjcJKZ.png'), ('another', 'https://i.imgur.com/dfsdkjfd.png')]"
        self.assertEqual(str(result), expected)

        
    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(text)
        expected = "[('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]"
        self.assertEqual(str(result), expected)

if __name__ == "__main__":
    unittest.main()