class User:
    """Represents a user in the social network."""

    def __init__(self, name):
        self._name = name          # private attribute
        self._friends = []         # list of friend names

    def add_friend(self, friend):
        """Add a friend (to be implemented later)."""
        pass

    def remove_friend(self, friend):
        """Remove a friend (to be implemented later)."""
        pass

    def get_name(self):
        return self._name

    def get_friends(self):
        return self._friends

    def __str__(self):
        return self._name
