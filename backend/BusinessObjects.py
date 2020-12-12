class Customer:
    def __init__(self, CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country

if __name__ == "__main__":
    print('this is business object package')