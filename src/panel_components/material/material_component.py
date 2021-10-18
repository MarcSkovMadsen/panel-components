"""Basic Functionality for working with Material UI components

See https://mui.com/
"""
from panel_components.shared.component import ReactComponentGenerator

class MaterialComponent: # pylint: disable=too-few-public-methods
    """The MaterialWidget and MaterialLayout should inherit from this"""
    __javascript__ = [
        *ReactComponentGenerator.__javascript__,
        "https://unpkg.com/@material-ui/core@4.12.3/umd/material-ui.development.js",
    ]

    __css__ = [
        "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap",
        "https://fonts.googleapis.com/icon?family=Material+Icons",
    ]
