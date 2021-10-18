"""Basic Functionality for working with Bootstrap React components

See https://react-bootstrap.github.io/
"""
from panel_components.shared.component import ReactComponentGenerator


class BootstrapComponent:  # pylint: disable=too-few-public-methods
    """The BootstrapWidget and BootstrapLayout should inherit from this"""

    __javascript__ = [
        *ReactComponentGenerator.__javascript__,
        "https://unpkg.com/react-bootstrap@2.0.0-rc.1/dist/react-bootstrap.min.js",
    ]

    __css__ = ["https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"]
