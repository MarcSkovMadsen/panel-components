"""# Shared Widget Functionality

Provides Shared Widget Functionality
"""
from typing import Dict

import param

from ..component import Component


class Widget(Component):  # pylint: disable=too-few-public-methods, too-many-ancestors
    """Base Widget Class. You `panel_component` widgets should inherit from this"""

    name = param.String(default="", doc="Name of the widget")
    css_names = param.List([], doc="A list of css classes to be applied to the widget.")
    disabled = param.Boolean(
        default=False,
        doc="""
       Whether the widget is disabled.""",
    )
    autofocus = param.Boolean(
        default=False,
        doc="""The autofocus attribute. Defaults to `False`""",
    )
    margin = param.Parameter(
        default=(5, 10),
        doc="""
        Allows to create additional space around the component. May
        be specified as a two-tuple of the form (vertical, horizontal)
        or a four-tuple (top, right, bottom, left).""",
    )
    tooltip = param.String(doc="The tooltip string")

    # A string version of the `css_names` list
    _css_names = param.String("")

    _css_names_component = ["pnc-widget"]

    _scripts = {
        "render": (
            "component.disabled=data.disabled;"
            "component.title=data.tooltip;"
            "component.autofocus=data.autofocus;"
            "component.className=data._css_names"
        ),
        "disabled": "component.disabled=data.disabled",
        "tooltip": "component.title=data.tooltip",
        "autofocus": "component.autofocus=data.autofocus",
        "_css_names": "component.className=data._css_names",
    }
    _properties = {
        "disabled": "disabled",
        "title": "tooltip",
        "autofocus": "autofocus",
        "className": "_css_names",
    }
    _events: Dict[str, str] = {}

    def __init__(self, **params):
        super().__init__(**params)

        self.param.watch(self._handle_css_names_changed, "css_names")

        self._handle_css_names_changed()

    def _handle_css_names_changed(self, event=None):  # pylint: disable=unused-argument
        css_names = self._get_css_names()
        self._set_css_names(css_names)

    def _get_css_names(self):
        return list(set(self._css_names_component + self.css_names))

    def _set_css_names(self, css_names):
        with param.edit_constant(self):
            self._css_names = " ".join(css_names)

    @classmethod
    def example(cls):
        raise NotImplementedError()
