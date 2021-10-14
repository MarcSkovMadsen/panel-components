from ..component import Component
import param

class Widget(Component):
    name = param.String(default='')
    tooltip = param.String()
    css_names = param.List([])
    disabled = param.Boolean(default=False, doc="""
       Whether the widget is disabled.""")
    autofocus = param.Boolean(
        default=False,
        doc="""The autofocus attribute. Defaults to `False`""",
    )
    margin = param.Parameter(default=(5, 10), doc="""
        Allows to create additional space around the component. May
        be specified as a two-tuple of the form (vertical, horizontal)
        or a four-tuple (top, right, bottom, left).""")
    _css_names = param.String("")
    _scripts = {
        "render": "component.disabled=data.disabled;component.title=data.tooltip;component.autofocus=data.autofocus;component.className=data._css_names",
        "disabled": "component.disabled=data.disabled",
        "tooltip": "component.title=data.tooltip",
        "autofocus": "component.autofocus=data.autofocus",
        "_css_names": "component.className=data._css_names",
    }