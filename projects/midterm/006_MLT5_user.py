class User:
  def __init__(self, first_name, last_name, followers_count: int, friends_name: list):
    self.first_name = first_name
    self.last_name = last_name
    self.followers_count = followers_count
    self.friends_name = friends_name

  def introduce_self(self):
    print("\n------------------------------")
    print(f"Hi! I am {self.first_name} {self.last_name}")
    print("------------------------------")

  def view_full_profile(self):
    print("\n------------------------------")
    print(f"Profile Name is {self.first_name} {self.last_name} with {self.followers_count} followers.")
    print(f"Friends are: ")
    for friend in self.friends_name:
      print(f"{friend}")
    print("------------------------------")