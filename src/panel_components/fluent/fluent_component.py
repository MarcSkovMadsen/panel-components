"""Basic Functionality for working with Microsoft Fluent Web components

See https://github.com/microsoft/fluentui/tree/master/packages/web-components
"""


class FluentComponent:  # pylint: disable=too-few-public-methods
    """The FluentWidget and FluentLayout should inherit from this"""

    __javascript_modules__ = ["https://unpkg.com/@fluentui/web-components@1.6.2"]