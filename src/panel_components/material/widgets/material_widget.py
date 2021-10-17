from ...shared.component import ReactComponentGenerator
from ..material_component import MaterialComponent

class MaterialWidget(MaterialComponent):
    pass

class MaterialWidgetGenerator(ReactComponentGenerator):
    _tooltip_element = """element=React.createElement(MaterialUI.Tooltip,{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},element);"""
