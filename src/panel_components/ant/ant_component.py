from panel_components.shared.component import ReactComponentGenerator


class AntComponent:
    __javascript__ = [
        *ReactComponentGenerator.__javascript__,
        "https://unpkg.com/antd@4.16.13/dist/antd.min.js",
    ]

    __css__ = [
        "https://unpkg.com/antd@4.16.13/dist/antd.css",
    ]
