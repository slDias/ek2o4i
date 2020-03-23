# -*- encoding: utf-8 -*-


class ServerIsFull(Exception):
    """Raised when trying to add a new user to a full server"""
