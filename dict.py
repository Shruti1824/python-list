dict={'MON':3,'TUE':23,'WED':12,'THU':4}
print("The given dictionary :",dict)
check_key=input("Enter key to check:")
check_value=input("Enter value to check:")
if check_key in dict:
    print(check_key,"Is present")
    dict.pop(check_key)
    dict[check_key]=check_value
    
else:
    print(check_key,"Is not present")
    dict[check_key]=check_value
    print("The updated dictionary :",dict)