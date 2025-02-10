import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

import yaml

__version__ = "0.1.1"

BADGE_PATTERN = r"\[badge(?::(\w+))?([^\]]*?)\]"

class BadgesInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md, config):
        super().__init__(pattern, md)
        self.config = config

    def handleMatch(self, m, data):
        _type = m.group(1)
        badge_config = self.config['types'].get(_type, {})

        _text = [badge_config['text']] if 'text' in badge_config else []
        if m.group(2):
            _text += m.group(2).strip().split("|")
        _icon = badge_config.get('icon', None)
        _title = badge_config.get('title', None)


        c_class = self.config['class']
        _class = f'{c_class} {c_class}--{_type}' if _type else c_class
        el = etree.Element('span', {'class': _class})

        if _icon:
            icon_el = etree.SubElement(el, 'span', {'class': f'{c_class}__icon'})
            if _title:
                icon_el.set('title', _title)
            icon_el.text = f':{_icon}:'

        for t in _text:
             text_el = etree.SubElement(el, 'span', {'class': f'{c_class}__text'})
             text_el.text = t

        return el, m.start(0), m.end(0)


class BadgesExtension(Extension):
    """Badges Extension."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        self.config = {
            'class': ['mdx-badge', 'Class to add to the badge elements - Default: "mdx-badge"'],
            'types': [{}, 'Types of badges to add - Default: {}']
        }

        super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        config = self.getConfigs()
        # Priority is just below EscapePattern and ReferencePattern
        md.inlinePatterns.register(BadgesInlineProcessor(BADGE_PATTERN, md, config), 'badges', 165)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return BadgesExtension(*args, **kwargs)
