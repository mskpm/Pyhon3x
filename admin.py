""" Clases Admin + Privileges """

import user

class Privileges():
    """ Class with atribute 'privileges'"""
    privileges = ["może coś więcej", "może ale nie musi", "patrzy w dobą stronę"]

    def show_privileges(self):
        """ Prints Admin privileges"""
        print("\nAdmin privileges: \n")
        for privilege in self.privileges:
            print("\t" + privilege + ", ")


class Admin(user.User):
    """ class inherits from User """
    def __init__(self, first_name, middle_name, last_name, home_dir):
        return super().__init__(first_name, middle_name, last_name, home_dir)
    #privileges = ["może coś więcej", "może ale nie musi", "patrzy w dobą stronę"]
    privileges = Privileges()