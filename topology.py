import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium", layout_file="layouts/topology.grid.json")


@app.cell
def _(TileUnit):
    unit_0 = TileUnit(tiling_type = "archi", code = "3.4.6.4")
    return (unit_0,)


@app.cell
def _(mo):
    mo.md("""
    ## The original tiling
    """)
    return


@app.cell
def _(unit_0):
    ax_0 = unit_0.plot(
        r = 1,
        r_alpha = 1,
        show_ids = False,
        show_prototile = False, 
        show_reg_prototile = False)
    ax_0.set_axis_off()
    ax_0
    return


@app.cell
def _(Topology, unit_0):
    topo_0 = Topology(unit_0)
    return (topo_0,)


@app.cell
def _(mo):
    mo.md("""
    ## Its topology
    Showing vertices and edges labelled by their topological position in the tiling. Identically labelled elements are topologically equivalent.
    """)
    return


@app.cell
def _(topo_0):
    topo_0.plot(
        show_edge_labels = True
    )
    return


@app.cell
def _(mo):
    transform = mo.ui.dropdown(["zigzag_edge", "rotate_edge", "scale_edge", "push_vertex", "nudge_vertex"])
    transform
    return (transform,)


@app.cell
def _(mo):
    mo.md("""
    ## The tiling transformed
    """)
    return


@app.cell
def _(topo_0, transform):
    if transform.value is None:
      topo_1 = topo_0
    else:
      topo_1 = topo_0.transform_geometry(True, True, "abcd", transform.value, smoothness = 5, h = 0.5)
    return (topo_1,)


@app.cell
def _(topo_1):
    ax_1 = topo_1.tileable.plot(
        r = 1,
        r_alpha = 1,
        show_ids = False,
        show_prototile = False, 
        show_reg_prototile = False)
    ax_1.set_axis_off()
    ax_1
    return


@app.cell
def _():
    from weavingspace import TileUnit
    from weavingspace import Topology

    return TileUnit, Topology


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
