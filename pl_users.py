users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name": "Yeti"}]

def pl(users):
    pl_users = [user.get('name', 'secret') for user in users if user.get('country') == 'Poland']
    return pl_users