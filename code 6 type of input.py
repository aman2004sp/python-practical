print("Check the type of Input\n")


a = input("Enter any input: ")
if a.isdigit():
    print("The input is in Number.")
elif a.isalpha():
    print("The input is in Letter.")

elif a.isalnum():
    print("The input is in Alpha-Numeric.")
    
else:
    print("The input is in Special Character.")
def int_to_word(character):
  character = str(character) if type(character)!=str else None
  conversion_dict = {
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE'
  }
  return conversion_dict[character] if character.isnumeric() else 'Character not numeric'
#enter your digit here
int_to_word()
