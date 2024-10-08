class ContactBook:
    def _intit_(self) = {}
    self.contacts = {}

def add_contact(self,name, phone):
    if name in self.contacts:
        print(f"contact '{name}' already exists.")
    else:
        self.contacts[name] = phone
        print(f"contact '{name}' added.")

        def delete_contact(self,name):
            if name in self.contacts:
                del self.contacts[name]
                print(f"contact '{name}' deleted.")
            else:
                print(f"contact '{name}' not found")
                