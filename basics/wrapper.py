from collections import defaultdict
#basic decorator
def basic_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
        
    return wrapper

@basic_decorator
def greet():
    print("hello")
    
    
# greet()
    
#authentication decorator
def authentication_decorator(func):
    def wrapper(**user_creds):
        if not (user_creds.get("name")=="madhu" and user_creds.get("password")=="hello@world"):
          return 'Authentication Fails Invalid Credentials'
        return func(**user_creds)
    return wrapper


@authentication_decorator
def login(**user_creds):
    print("Login  Successfull")
    return 'Welcome Buddy'
    
result=login(name="madhu",password="hello@world")
print(result)

d=defaultdict(int)
print(d['hello'])
print(d['world'])
print(d)
        
        