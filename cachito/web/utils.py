# SPDX-License-Identifier: GPL-3.0-or-later
from flask import request, url_for


def pagination_metadata(pagination_query, verbose):
    """
    Return a dictionary containing metadata about the paginated query.
    This must be run as part of a Flask request.

    :param pagination_query: flask_sqlalchemy.Pagination object
    :return: a dictionary containing metadata about the paginated query
    """

    pagination_data = {
        'first': url_for(
            request.endpoint, page=1, per_page=pagination_query.per_page,
            verbose=verbose, _external=True),
        'last': url_for(
            request.endpoint, page=pagination_query.pages, per_page=pagination_query.per_page,
            verbose=verbose, _external=True),
        'next': None,
        'page': pagination_query.page,
        'pages': pagination_query.pages,
        'per_page': pagination_query.per_page,
        'previous': None,
        'total': pagination_query.total,
    }

    if pagination_query.has_prev:
        pagination_data['previous'] = url_for(
            request.endpoint, page=pagination_query.prev_num,
            per_page=pagination_query.per_page, verbose=verbose, _external=True)
    if pagination_query.has_next:
        pagination_data['next'] = url_for(
            request.endpoint, page=pagination_query.next_num,
            per_page=pagination_query.per_page, verbose=verbose, _external=True)

    return pagination_data


def str_to_bool(item):
    """
    Convert a string to a boolean.

    :param str item: string to parse
    :return: a boolean equivalent
    :rtype: boolean
    """
    if isinstance(item, str):
        return item.lower() in ('true', '1')
    else:
        return False
