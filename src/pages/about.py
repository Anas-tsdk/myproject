from dash import html

def about_page():
    return html.Div(
        children=[
            html.H1("À propos", style={"textAlign": "center"}),
            html.P("Ceci est la page À propos."),
        ],
        style={"padding": "20px"}
    )
