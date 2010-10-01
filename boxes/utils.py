from html5lib import sanitizer, html5parser

# TODO this is domain-specific to anime/gg, rip it out and replace with generic processor hook
def sanitize_html(stream, extra_allowed=None):
    if extra_allowed is None:
        extra_allowed = []
    # allow embedding of videos for example (ideally we use oembed, but need 
    # to sort a bug first) this route is the *fastest* now
    allowed = ["object", "embed", "param"] + extra_allowed
    class HTMLSanitizer(sanitizer.HTMLSanitizer):
        allowed_elements = sanitizer.HTMLSanitizer.allowed_elements + allowed
    bits = []
    parser = html5parser.HTMLParser(tokenizer=HTMLSanitizer)
    for token in parser.parseFragment(stream).childNodes:
        bits.append(token.toxml())
    return "".join(bits)
