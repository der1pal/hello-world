def greet(name):
    """Return a greeting for the given name."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else ""
    print(greet(name))
