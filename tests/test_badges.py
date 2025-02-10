import markdown
import textwrap

def test_generic_untyped_badge_single_text():
    extensions = ['badges']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = '[badge Text]'

    expected_html = R'''
    <span class="mdx-badge">
    <span class="mdx-badge__text">Text</span>
    </span>
    '''

    expected_html = "".join(textwrap.dedent(expected_html).strip().split("\n"))
    expected_html = f"<p>{expected_html}</p>"

    html = md.convert(markdown_text)
    assert html == expected_html

def test_generic_untyped_badge_multiple_text():
    extensions = ['badges']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = '[badge Text1 with spaces|Text2 with spaces]'

    expected_html = R'''
    <span class="mdx-badge">
    <span class="mdx-badge__text">Text1 with spaces</span>
    <span class="mdx-badge__text">Text2 with spaces</span>
    </span>
    '''

    expected_html = "".join(textwrap.dedent(expected_html).strip().split("\n"))
    expected_html = f"<p>{expected_html}</p>"

    html = md.convert(markdown_text)
    assert html == expected_html

def test_generic_typed_badge():
    extensions = ['badges']
    extension_configs = {}
    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

    markdown_text = '[badge:type Text]'

    expected_html = R'''
    <span class="mdx-badge mdx-badge--type">
    <span class="mdx-badge__text">Text</span>
    </span>
    '''

    expected_html = "".join(textwrap.dedent(expected_html).strip().split("\n"))
    expected_html = f"<p>{expected_html}</p>"

    html = md.convert(markdown_text)
    assert html == expected_html
