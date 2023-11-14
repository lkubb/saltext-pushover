"""
Salt execution module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "pushover"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The pushover execution module is not implemented yet")
    return __virtualname__


def example_function(text):
    """
    This example function should be replaced

    CLI Example:

    .. code-block:: bash

        salt '*' pushover.example_function text="foo bar"
    """
    return __salt__["test.echo"](text)
