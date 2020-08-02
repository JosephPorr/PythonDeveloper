# Before we can export the information about the system's users, 
# we'll need to get the information from the system's password database
# in a format that we can easily work with. 
# We'll rely on the pwd package to do this. 

import pwd  # https://docs.python.org/3/library/pwd.html

def fetch_users():
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:   # home, is the home directory
            users.append({
              'name': user.pw_name,
              'id': user.pw_uid,
              'home': user.pw_dir,
              'shell': user.pw_shell,
            })
    return users