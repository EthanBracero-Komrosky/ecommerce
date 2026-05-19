import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Test test; hooray!
    """)
    return


@app.cell
def _():
    print("Hello world!")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
