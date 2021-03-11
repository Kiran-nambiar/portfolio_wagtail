from wagtail.core import blocks

class HeadingAndParagraphBlock(blocks.StructBlock):
     heading = blocks.CharBlock(default="", help_text="Add your title")
     paragraph = blocks.RichTextBlock(default="", help_text="Add your content")

class TechnologyDivisionBlock(blocks.StructBlock):
     heading = blocks.CharBlock(default="", help_text="Add your title")
     paragraph = blocks.RichTextBlock(default="", help_text="Add your content")