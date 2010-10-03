class AddressCard:
    
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.surname, self.phone_number)

class AddressBook:
    
    card_list = []
    
    def add_card(self, *args):
        for card in args:
            self.card_list.append(card)
    
    def lookup(self, search_string):
        for card in self.card_list:
            for value in card.__dict__.values():
                if search_string.lower() in value.lower():
                    print(card)
    
    def print_book(self):
        for card in self.card_list:
            print(card)

if __name__ == '__main__':
    
    account0 = AddressCard('Mike', 'Black', '272-235-235')
    account1 = AddressCard('John', 'Smith', '342-234-523')
    account2 = AddressCard('Jackie', 'Chan', '634-234-546')
    
    this_book = AddressBook()
    this_book.add_card(account0, account1, account2)
    this_book.print_book()
    print('\n')
    this_book.lookup('chan')
        
            
            
            
        