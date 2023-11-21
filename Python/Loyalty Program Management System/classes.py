class MemRequest:
    """
    Class representing a member request.

    Attributes:
        id (int): An integer representing the ID of the member making the request.
        request (str): A string representing the request made by the member.
    """

    def __init__(self, memberId: int, request: str) -> None:
        """
        Initialize a MemRequest object.
        """
        self.id = id
        self.request = request


class Member:
    """
    Class representing a member.

    Attributes:
        id (int): The ID of the member.
        name (str): The name of the member.
        email (str): The email address of the member.
        tier (str): The membership tier of the member.
        points (int): The number of points the member has.
    """

    def __init__(self, id: int, name: str, email: str, tier: str, points: int) -> None:
        """
        Initialize a Member object.
        """
        self.id = id
        self.name = name
        self.email = email
        self.tier = tier
        self.points = points