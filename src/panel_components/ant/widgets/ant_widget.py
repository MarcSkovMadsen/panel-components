from ...shared.component import ReactComponentGenerator
from ..ant_component import AntComponent


class AntWidget(AntComponent):
    pass


class AntWidgetGenerator(ReactComponentGenerator):
    _tooltip_element = """element=React.createElement(antd.Tooltip,{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},element);"""
