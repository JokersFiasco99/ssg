import unittest
from main import extract_markdown_images, extract_markdown_links, extract_title

class TestMarkdownExtraction(unittest.TestCase):
    """Test suite for Markdown extraction functions."""

    def test_extract_markdown_images(self):
        """Test extraction of image information from Markdown text."""
        text = "Here's an image ![Alt text](image.jpg) and another ![Second image](path/to/image.png)"
        expected = [("Alt text", "image.jpg"), ("Second image", "path/to/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_match(self):
        """Test image extraction when no images are present in the text."""
        text = "This text contains no images"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links(self):
        """Test extraction of link information from Markdown text."""
        text = "Here's a [link](https://example.com) and [another one](http://test.org)"
        expected = [("link", "https://example.com"), ("another one", "http://test.org")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_match(self):
        """Test link extraction when no links are present in the text."""
        text = "This text contains no links"
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_ignore_images(self):
        """Test that link extraction ignores image syntax."""
        text = "A ![image](image.jpg) and a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_title_valid(self):
        """Test extraction of title from valid Markdown text."""
        markdown = "# This is a title\nSome content here."
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_extract_title_multiple_headers(self):
        """Test extraction of title when multiple headers are present."""
        markdown = "# Main Title\n## Subtitle\n### Another header"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_no_h1(self):
        """Test that an exception is raised when no h1 header is found."""
        markdown = "## This is not an h1\nSome content."
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_empty_markdown(self):
        """Test that an exception is raised for empty Markdown."""
        with self.assertRaises(Exception):
            extract_title("")

if __name__ == '__main__':
    unittest.main()