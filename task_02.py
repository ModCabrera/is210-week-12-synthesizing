#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains Custom Exception Class"""


class CustomError(Exception):
    """
    Attributes:
        None
    """

    def __init__(self, message, cause):
        """Custom Error that stores error reason.
        Args:
            cause (str): Reason for error.
            message (str): User input.

        Returns:
            None

        Examples:
        >>> myerr = CustomError('Whoah!', cause='Messed up!')
        >>> print myerr.cause
        Messed up!
        """
        self.cause = cause
        self.message = message
        Exception.__init__(self)
