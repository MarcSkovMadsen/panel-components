"""Basic Functionality for working with Bootstrap React Widgets

See https://react-bootstrap.github.io/
"""
from ..bootstrap_component import BootstrapComponent, ReactComponentGenerator

class BootstrapWidget(BootstrapComponent):
    """Bootstrap Widgets should inherit from this"""


class BootstrapWidgetGenerator(ReactComponentGenerator):
    """Bootstrap Widgets should use this to create _template and _scripts"""
    # pylint: disable=line-too-long
    _tooltip_element = (
        """tooltip=React.createElement(ReactBootstrap.Tooltip,null,data.tooltip);"""
        """overlay=React.createElement(ReactBootstrap.OverlayTrigger,{placement: data.tooltip_placement, overlay: tooltip},element);"""
        """element=React.createElement(React.Fragment,null,overlay);"""
    )
    # pylint: enable=line-too-long
