from panel_components.shared.component import ReactComponent

class MaterialUIComponent():
    __javascript__ = [
        *ReactComponent.__javascript__,
        "https://unpkg.com/@material-ui/core@4.12.3/umd/material-ui.development.js",
    ]

    __css__ = [
        "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap",
        "https://fonts.googleapis.com/icon?family=Material+Icons"
    ]