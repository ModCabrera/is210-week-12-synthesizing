#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Created some classes from Exceptions and TypeError"""


class BaseError(Exception):
    """Error based from Exception.
    Attributes:
        None
    """
    pass


class StringError(BaseError, TypeError):
    """Error based from BaseError and Type Error.
    Attributes:
        None
    """
    pass


class NumberError(BaseError, TypeError):
    """Error based from BaseError and Type Error.
    Attributes:
        None
    """
    pass


class NonZeroError(NumberError):
    """Error based from NumberError.
    Attributes:
        None
    """
    pass
