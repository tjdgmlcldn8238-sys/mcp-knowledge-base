"""
Simple Echo MCP Server Example
"""

from fastmcp import FastMCP, Context
from typing import Dict, Any

mcp = FastMCP(
    "echo-example",
    description="Simple echo MCP server for testing"
)

@mcp.tool()
async def echo(message: str, context: Context = None) -> Dict[str, Any]:
    """Echo back the message"""
    return {
        "original": message,
        "echoed": message,
        "length": len(message)
    }

@mcp.tool()
async def reverse(text: str, context: Context = None) -> Dict[str, Any]:
    """Reverse the text"""
    return {
        "original": text,
        "reversed": text[::-1]
    }

if __name__ == "__main__":
    mcp.run()
