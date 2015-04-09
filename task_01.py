#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK10 synthesizing task 01."""


def sum_orders(customers, orders):
    """Correlating two related data sets similar to the functionality of
    a SQL database.

    Args:
        customers (dict): A dictionary of customers keyed by customer id.
        orders (dict): A dictionary of orders keyed by order id.

    Returns:
        (dict): Returns a new list comprised of the combined dictionaries.

    Examples:
    >>> pp.pprint(sum_orders(data.CUSTOMERS, data.ORDERS))
    {1: {'email': 'evorsoisson@komarr.net',
         'name': 'Ekaterin Vorsoisson',
         'orders': 3,
         'total': 1287},
     2: {'email': 'cordelia@beta.com',
         'name': 'Cordelia Naismith',
         'orders': 5,
         'total': 2778},
     3: {'email': 'iv398@barrayar.net',
         'name': 'Ivan Vorpatril',
         'orders': 3,
         'total': 358},

    """
    new_list = {}
    for val in orders.values():
        cust_id = val['customer_id']
        cust_name = customers[cust_id]['name']
        cust_email = customers[cust_id]['email']
        cust_orders = 1
        cust_total = val['total']
        if cust_id in new_list:
            cust_orders = cust_orders + new_list[cust_id]['orders']
            cust_total = cust_total + new_list[cust_id]['total']
        new_list.update({cust_id: dict(name=cust_name, email=cust_email,
                                       orders=cust_orders, total=cust_total)})
    return new_list
