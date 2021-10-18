"""Basic Functionality for working with Shoelace components

See https://shoelace.style/
"""


class ShoelaceComponent:  # pylint: disable=too-few-public-methods
    """The ShoelaceWidget and ShoelaceLayout should inherit from this"""

    __javascript_modules__ = [
        "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.57/dist/shoelace.js/+esm"
    ]

    __css__ = [
        "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.0.0-beta.57/dist/themes/light.css"
    ]
