import re

def phone_number():
  
  with open ('./assets/potential_contacts.txt', 'r') as file:
    file = file.read()

    phone_numbers = re.findall(r'(\w{3}-\w{3}-\w{4})', file)

  with open ('phone_numbers.txt', 'w+') as file:
    for phones in phone_numbers:
      file.write(f"{str(phones)}\n")
  return phone_numbers


def emails():
  with open('./assets/potential_contacts.txt', 'r') as file:
    file = file.read()

    email_address = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', file)

    with open ('emails.txt', 'w+') as file:
      for emale in email_address:
        file.write(f'{str(emale)}\n')
    return email_address


if __name__ == '__main__':

  print(phone_number())
  # print(emails())

