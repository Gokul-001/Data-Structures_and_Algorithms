class Taxi:
    def __init__(self, id):
        self.taxi_id = id
        self.current_station = "A"
        self.earning = 0


class booking:
    def __init__(self):
        self.taxilist = {}
        self.min_earned_taxi = 0
        self.stationlist = {"A": [], "B": [],
                            "C": [], "D": [], "E": [], "F": []}

    def createTaxi(self, inp):
        for i in range(1, inp+1):
            taxi = Taxi(i)
            self.taxilist[i] = taxi
            self.stationlist[taxi.current_station].append(i)

    def stationdetails(self):
        return self.stationlist

    def find_nearest_taxi(self, pick):
        min_earnings = 0
        # all taxi at pick
        available_taxi = [
            taxi for taxi in self.taxilist.values() if taxi.current_station == pick]

        # if not taxi at pick
        if available_taxi == None:
            available_taxi = [
                taxi for taxi in self.taxilist.values() if taxi.current_station != pick]

        # assign taxi with min earnings3
        for taxi in available_taxi:
            if taxi.earning <= min_earnings:
                min_earnings = taxi.earning
                self.min_earned_taxi = taxi
        return self.min_earned_taxi

    def bookTaxi(self, pick, drop):
        alloted_taxi = self.find_nearest_taxi(pick)
        if alloted_taxi:
            alloted_taxi_id = alloted_taxi.taxi_id
            dist = abs(ord(drop)-ord(pick)) * 15  # diff * 15 = distance
            price = max(100+(dist-5)+10, 100)
            self.stationlist[alloted_taxi.current_station].remove(
                alloted_taxi.taxi_id)
            alloted_taxi.current_station = drop
            alloted_taxi.earning += price
            self.stationlist[alloted_taxi.current_station].append(
                alloted_taxi.taxi_id)
            print(
                f"Taxi id - {alloted_taxi_id} booked from {pick} to {drop} with fare : {price:.2f}")
        else:
            print("No cab available")

    def taxidetails(self):
        taxidetaillist = []
        for taxi in self.taxilist.values():
            taxidetaillist.append(taxi.taxi_id)
        return taxidetaillist

    def taxiearningdeatils(self):
        earninglist = []
        for taxi in self.taxilist.values():
            earninglist.append(taxi.earning)
        return earninglist


if __name__ == "__main__":

    try:
        print("Welcome to Cab booking system !")
        inp = int(input("Enter the no of taxi's :"))
        if inp <= 0:
            raise Exception("No cab intialised ")
        else:
            book = booking()
            book.createTaxi(inp)

    except Exception as e:
        print(e)

    print('Taxi details :    ', book.taxidetails())
    print('Taxi earnings :   ', book.taxiearningdeatils())
    print('Station details :   ', book.stationdetails())

    print("-------------------------------------------------------------")


# user choice

    try:
        loop = True
        while loop:
            print()
            print(
                'Enter a choice\n1 - Show Taxi details \n2 - Taxi earning details\n3 - Book a taxi\n4 - Station Vs Cab Details\n5 - Exit   ')
            print("-------------------------------------------------------------")
            choice = int(input("Enter your choice :"))
            print()
            if choice == 1:
                print('Taxi details :    ', book.taxidetails())
            elif choice == 2:
                print('Earning details : ', book.taxiearningdeatils())
            elif choice == 3:
                try:
                    station = ["A", "B", "C", "D", "E", "F"]
                    print("Available Stations :", station)
                    pick = input("Enter pick-up station :").upper()
                    drop = input("Enter drop station :").upper()
                    if (pick not in station) or (drop not in station):
                        raise Exception("Wrong station")
                    book.bookTaxi(pick, drop)
                except Exception as e:
                    print(e)
            elif choice == 4:
                print('Station details :   ', book.stationdetails())
            elif choice == 5:
                print("Thank you , Have a good day ")
                loop = False
            else:
                print("Choose a vaild option")
    except Exception as e:
        print(e)
