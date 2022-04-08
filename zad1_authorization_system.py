import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(username+password)
        self.is_logged = False

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self._encrypt_password(password) == self.password


class AuthenticException(Exception):
    def __init__(self, username=None, user=None) -> None:
        self.username = username
        self.user = user

    def __str__(self):
        return "Błędny login lub hasło"


class PermissionError(Exception):
    pass


class IncorectPassword(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class NotPermitted(PermissionError):
    pass


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if len(password) < 8:
            raise PasswordTooShort(username)
        if username in self.users:
            raise UsernameAlreadyExists(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        if username not in self.users:
            raise IncorrectUsername(username)
        if not self.users[username].check_password(password):
            raise IncorectPassword(username, self.users[username])
        self.users[username].is_logged = True

    def is_logged(self, username):
        if username not in self.users:
            raise IncorrectUsername(username)
        return self.users[username].is_logged


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        if perm_name in self.permissions:
            raise PermissionError("Permission exists")
        self.permissions[perm_name] = set()

    def permit_user(self, perm_name, username):
        if perm_name not in self.permissions:
            raise PermissionError("Permission does not exist")
        if username not in self.authenticator.users:
            raise IncorrectUsername(username)
        self.permissions[perm_name].add(username)

    def check_permission(self, perm_name, username):

        if perm_name not in self.permissions:
            raise PermissionError("Permission does not exist")
        if username not in self.authenticator.users:
            raise IncorrectUsername(username)
        return username in self.permissions[perm_name]
