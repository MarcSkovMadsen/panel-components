from ..component import Component
import param

class Widget(Component):
    disabled = param.Boolean(default=False)
    tooltip = param.String()