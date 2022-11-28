from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("hello-world")
except PackageNotFoundError:
    # package is not installed
    pass
