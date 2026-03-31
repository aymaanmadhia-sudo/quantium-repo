from improved_dash_app import app
from dash import html, dcc


def test_layout_exists():
    assert app.layout is not None


def test_header_present():
    layout = app.layout
    header = layout.children[0].children[0]

    assert isinstance(header, html.H2)
    assert "Sales Dashboard" in header.children


def test_radio_present():
    layout = app.layout
    radio = layout.children[0].children[1]

    assert isinstance(radio, dcc.RadioItems)
    assert radio.id == "region"
    assert len(radio.options) == 5


def test_graph_present():
    layout = app.layout
    graph = layout.children[0].children[2]

    assert isinstance(graph, dcc.Graph)
    assert graph.id == "graph"