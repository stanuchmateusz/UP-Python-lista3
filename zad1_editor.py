import zad1_authorization_system


auth = zad1_authorization_system.Authenticator()

auth.add_user("admin", "12345678")
auth.add_user("user", "87654321")

authorizor = zad1_authorization_system.Authorizor(auth)
authorizor.add_permission("change")
authorizor.add_permission("test")

authorizor.permit_user("test", "admin",)
authorizor.permit_user("change", "admin")
authorizor.permit_user("test", "user")


class Editor:
    def __init__(self):
        self.username = None
        self.options = {"a": self.login, "b": self.test,
                        "c": self.change, "d": self.quit}

    def login(self):
        try:
            username = input("Podaj login: ")
            password = input("Podaj haslo: ")
            auth.login(username, password)
            self.username = username
        except zad1_authorization_system.AuthenticException as e:
            print(e)

    def is_permitted(self, permission):
        try:
            authorizor.check_permission(self.username, permission)
        except zad1_authorization_system.NotLoggedError as e:
            print(e)
        except zad1_authorization_system.NotPermitted as e:
            print(e)

    def test(self):
        self.is_permitted("test")
        print("test")

    def change(self):
        self.is_permitted("change")
        print("change")

    def quit(self):
        print("quit")
        exit()

    def run(self):
        while True:
            print("a - logowanie")
            print("b - test")
            print("c - zmiana")
            print("d - wyjscie")
            option = input("Podaj opcje: ")
            self.options[option]()
