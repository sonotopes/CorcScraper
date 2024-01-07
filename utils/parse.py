from selectolax.parser import Node

def parse_raw_attributes(node: Node, selectors: list):
    """Parses attributes according to config"""
    parsed_attrs = {}

    for node_attributes in selectors:
        name = node_attributes.get("name")
        selector = node_attributes.get("selector")
        secondary_selector = node_attributes.get("secondary_selector")
        _text = node_attributes.get("text")
        required = node_attributes.get("required")

        # Required attribute is one that appears on all listings. If not required, then the attribute is optional.
        if required:
            matched = node.css_first(selector)

            if _text:
                parsed_attrs[name] = matched.text()

            elif not _text:
                parsed_attrs[name] = matched.attributes.get("src")

        elif not required:
            matched = node.css_first(selector)

            if matched and _text:
                parsed_attrs[name] = matched.child.text()

            elif matched and not _text:
                parsed_attrs[name] = matched.attributes.get("src")

            # Site organizes divs using two different selectors. As such, this is in case the first selector can't be
            # found.
            elif not matched and secondary_selector:
                matched = node.css_first(secondary_selector)
                if matched:
                    parsed_attrs[name] = matched.text()
                else:
                    parsed_attrs[name] = "Not listed"

            else:
                parsed_attrs[name] = "Not listed"

    return parsed_attrs

