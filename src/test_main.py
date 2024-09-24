import unittest
from main import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "Here's an image ![Alt text](image.jpg) and another ![Second image](path/to/image.png)"
        expected = [("Alt text", "image.jpg"), ("Second image", "path/to/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_match(self):
        text = "This text contains no images"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links(self):
        text = "Here's a [link](https://example.com) and [another one](http://test.org)"
        expected = [("link", "https://example.com"), ("another one", "http://test.org")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_match(self):
        text = "This text contains no links"
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_ignore_images(self):
        text = "A ![image](image.jpg) and a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == '__main__':
    unittest.main()