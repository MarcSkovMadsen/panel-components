"""Basic Functionality for working with Ant Design components

See https://ant.design/
"""
from panel_components.shared.component import ReactComponentGenerator

class AntComponent: # pylint: disable=too-few-public-methods
    """The AntWidget and AntLayout should inherit from this"""
    __javascript__ = [
        *ReactComponentGenerator.__javascript__,
        "https://unpkg.com/antd@4.16.13/dist/antd.min.js",
    ]

    __css__ = [
        "https://unpkg.com/antd@4.16.13/dist/antd.css",
    ]
