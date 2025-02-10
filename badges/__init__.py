import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

import yaml

__version__ = "0.1.1"

BADGE_PATTERN = r"\[badge(?::(\w+))?(.*?)\]"

class BadgesInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        _type = m.group(1)
        _text = m.group(2).strip().split("|")

        _class = f'mdx-badge mdx-badge--{_type}' if _type else 'mdx-badge'
        el = etree.Element('span', {'class': _class})
        for t in _text:
             text_el = etree.SubElement(el, 'span', {'class': 'mdx-badge__text'})
             text_el.text = t

        return el, m.start(0), m.end(0)


class BadgesExtension(Extension):
    """Badges Extension."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        self.config = {'class': ['mdx-badge', 'Class to add to the badge elements - Default: "mdx-badge"']}

        super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.inlinePatterns.register(BadgesInlineProcessor(BADGE_PATTERN, md), 'badges', 999)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return BadgesExtension(*args, **kwargs)
