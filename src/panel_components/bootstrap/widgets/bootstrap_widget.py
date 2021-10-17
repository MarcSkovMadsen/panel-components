from ..bootstrap_component import BootstrapComponent, ReactComponentGenerator

class BootstrapWidget(BootstrapComponent):
    pass

class BootstrapWidgetGenerator(ReactComponentGenerator):
    _tooltip_element = (
        # return """element=React.createElement(MaterialUI.Tooltip,{{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration}},element);"""
        """tooltip=React.createElement(ReactBootstrap.Tooltip,null,data.tooltip);"""
        """overlay=React.createElement(ReactBootstrap.OverlayTrigger,{placement: data.tooltip_placement, overlay: tooltip},element);"""
        """element=React.createElement(React.Fragment,null,overlay);"""
    )