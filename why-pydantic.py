def insert_data(name: str, age: int):
    #type hinting -> only hints but no error if wrong data
    
    #validation but not scalabale
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted")
    else:
        raise TypeError("Incorrect data")
        
insert_data(23,'sda')


def update_data(name: str, age:int):
    
    if type(name) == str and type(age) == int:
        if( age< 0):
            raise ValueError("error")
    else:
        print(name)
        print(age)
        print("Updated")

#too much manual code for validation shit

