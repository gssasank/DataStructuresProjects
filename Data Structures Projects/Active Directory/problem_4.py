class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_empty(self):
        if len(self.get_groups()) == 0:
            return True
        else:
            return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):

    if user in group.get_users():
        # Base case for recursion
        return True
    else:
        if group.is_empty():
            return False
        else:
            # Recursive Call
            for sub_user in group.get_groups():
                return is_user_in_group(user, sub_user)


print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(sub_child_user, sub_child))

