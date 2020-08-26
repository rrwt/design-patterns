"""
Observer Design Pattern
-------------------------------------------------------------
A behavioral design pattern that lets you define subscription
mechanism to notify multiple objects about any event that
happen to the object they are observing

1. Pull Model:
    The publisher notifies the observers that something has
    happened, then the observers query the subject to get
    the information they require.

2. Push Model:
    The publisher sends all the data required by observers
    along with the notification. The observers do not need
    to query the publisher for information.
"""
