"""
This is where we handle errors.
PS. 
  Of course, I could write 'exception: int = 400' 
  but we use numerator of an exception as int and this exception is not int (usually).
  Exception is int when we use url patterns like '404/' and so on.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def any_error(request: HttpRequest, exception, name: str) -> HttpResponse:
    """
    A generic function to display an error information page.
    """
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)


def error400(request: HttpRequest, exception=400) -> HttpResponse:
    """
    Error handler 400 ((Bad Request))
    """
    name = "Bad Request"
    return any_error(request, exception, name)


def error403(request: HttpRequest, exception=403) -> HttpResponse:
    """
    Error handler 403 ((Forbidden))
    """
    name = "Forbidden"
    return any_error(request, exception, name)


def error404(request: HttpRequest, exception=404) -> HttpResponse:
    """
    Error handler 404 ((Page Not Found))
    """
    name = "Page Not Found"
    return any_error(request, exception, name)


def error405(request: HttpRequest, exception=405) -> HttpResponse:
    """
    Error handler 405 ((Method Not Allowed))
    """
    name = "Method Not Allowed"
    return any_error(request, exception, name)


def error500(request: HttpRequest, exception=500) -> HttpResponse:
    """
    Error handler 500 ((Internal Server Error))
    """
    name = "Internal Server Error"
    return any_error(request, exception, name)