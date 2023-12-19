import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id ):
        self.hotel_id= hotel_id
        self.name=df.loc[df["id"] == self.hotel_id,"name"].squeeze()

    def available(self):
        """check if the hotel is  available """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """ book  a hotel  availability changed to no  """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content =f"""
        Thank you  for your reservation!
        here are your ticket Data:
        name:{self.customer_name}
        hotel:{self.hotel.name}
        """
        return content


print(df)

hotel_id = input("Enter the ID of hotel:")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("hotel is not free")
