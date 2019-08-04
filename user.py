""" Class: User"""

class User():
    """ User data """
    def __init__(self, first_name, middle_name, last_name, home_dir):
        self.first_name = first_name
        if middle_name:
            self.middle_name = middle_name
        else:
            self.middle_name = ""
        self.last_name = last_name
        self.home_dir = home_dir
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.middle_name)
        print(self.last_name)
        print(self.home_dir)
        print(self.login_attempts)
    
    def increment_login_attempts(self):
        """ Increments login attempts for 1 """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Reset login attempts to 0 """
        self.login_attempts = 0

    def great_user(self):
        if self.middle_name:
            print("\nWitaj " + str(self.first_name).title() + " " + str(self.middle_name).title() + " " + str(self.last_name).title() +"!")
        else:
            print("\nWitaj " + str(self.first_name).title() + " " + str(self.last_name).title() + "!")

        print("Twój katalog domowy to: " + str(self.home_dir))
        print("Zanotowano prób logoania: " + str(self.login_attempts))

