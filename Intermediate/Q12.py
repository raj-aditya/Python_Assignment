def login_user():

    user_name = input("Enter Username: ")
    attempt = 3
    while(attempt>0):
      password = input("Enter Password:")
      re_password = input("Re-Enter Password:")
      if (password == re_password):
          return "Login Successful"
      else:
          attempt -= 1
    return "Sorry"


result = login_user()
print(result)