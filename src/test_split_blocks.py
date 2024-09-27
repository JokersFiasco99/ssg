import unittest
from split_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "This is a single block."
        expected = ["This is a single block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "First block.\n\nSecond block.\n\nThird block."
        expected = ["First block.", "Second block.", "Third block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_whitespace_only(self):
        markdown = "  \n\n  \n  \n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_mixed_content(self):
        markdown = "Block 1.\n\n  \n\nBlock 2.\n\n\n\nBlock 3."
        expected = ["Block 1.", "Block 2.", "Block 3."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("## Heading 2"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), "code")
        self.assertEqual(block_to_block_type("```python\nprint('Hello')\n```"), "code")

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Multi-line\n> quote"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), "ordered_list")
        self.assertEqual(block_to_block_type("1. First item\n2. Second item\n3. Third item"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), "paragraph")
        self.assertEqual(block_to_block_type("This is a\nmulti-line paragraph."), "paragraph")

    def test_mixed_content(self):
        self.assertEqual(block_to_block_type("Not a list:\n1. Item"), "paragraph")
        self.assertEqual(block_to_block_type("Not a heading:\n# Title"), "paragraph")

if __name__ == '__main__':
    unittest.main()