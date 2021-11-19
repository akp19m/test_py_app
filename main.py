from models.User import User

def main():
    u = User("Daniele","Pellini",25,"dp@email.it","Pello11","my_pwd8")
    print(u.calcAge())

if __name__ == "__main__":
    main()