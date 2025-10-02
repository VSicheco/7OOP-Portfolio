from user import User

def add_user():
  users = []
  total_users = 0

  choice = choice_adding_user()
  while choice == 'y':
    friend_list = []
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    followers = int(input("Followers: "))

    choice_friend = choice_adding_friend()
    while choice_friend == 'y':
      friends = input("Friend: ")
      friend_list.append(friends)
      choice_friend = choice_adding_friend()

    users.append(User(first_name, last_name, followers, friend_list))
    users[total_users].introduce_self()
    users[total_users].view_full_profile()
    total_users += 1

    choice = choice_adding_user()

def choice_adding_user():
  choice = input("Insert a Record?[y][n]: ").lower()
  return choice

def choice_adding_friend():
  choice = input("Add a friend?[y][n]: ").lower()
  return choice
    
def main():
  add_user()
  
if __name__ == '__main__':
  main()