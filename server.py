from mcp.server.fastmcp import FastMCP

app = FastMCP("demo-mcp")


@app.tool()
def echo(text: str) -> str:
    """Return the same text"""
    return text

@app.tool()
def add(a: float, b:float) -> float:
    """Return a + b"""
    return a + b


if __name__ == "__main__":
    app.run()