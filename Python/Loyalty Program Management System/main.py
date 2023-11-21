from typing import List
from classes import Member, MemRequest
from sys import exit
from loyaltyMgmt import LoyaltyManagement


def main():
    loyaltyProg = LoyaltyManagement()

    while True:
        print("\nMain Page:"
              "\n1. Enter new Members"
              "\n2. Display all Members"
              "\n3. Sort members via Bubble sort on points"
              "\n4. Sort members via Selection sort on tier"
              "\n5. Sort members via Insertion sort on Member's id"
              "\n6. Sort members via Merge sort on tier follow by Member points in ascending order"
              "\n7. Enter Members' request"
              "\n8. Set number of records per row to display"
              "\n9. Populate data"
              "\n0. Exit program")

        choice = int(input("Please select one: "))
        match choice:
            case 0:
                print("Exiting the program.")
                exit()
            case 1:
                loyaltyProg.addMember(Member(input("Enter Member ID: "), input("Enter Member Name: "),
                                             input("Enter Member Email: "), input("Enter Member Tier: "),
                                             int(input("Enter Member Points: "))))
                print("Member added.")
            case 2:
                loyaltyProg.showMembers()
            case 3:
                output = ''.join(f'\nID: {mem.id}\nName: {mem.name}\nEmail: {mem.email}\nTier: {mem.tier}\n'
                f'Points: {mem.points}\n{"-"*40}' for mem in loyaltyProg.sortByPoints(True))
                print(f'\nMembers List:\n{"-"*40}{output}')
            case 4:
                continue
                # loyaltyProg.sortByTier()
            case 5:
                output = ''.join(f'\nID: {mem.id}\nName: {mem.name}\nEmail: {mem.email}\nTier: {mem.tier}\n'
                f'Points: {mem.points}\n{"-"*40}' for mem in loyaltyProg.sortByMemberId(True))
                print(f'\nMembers List:\n{"-"*40}{output}')
            case 6:
                output = ''.join(f'\nID: {mem.id}\nName: {mem.name}\nEmail: {mem.email}\nTier: {mem.tier}\n'
                f'Points: {mem.points}\n{"-"*40}' for mem in loyaltyProg.sortByTierAndPoints(loyaltyProg.members))
                print(f'\nMembers List:\n{"-"*40}{output}')
            case 7:
                # member_id = input("Enter Member ID: ")
                # request = input("Enter Member Request: ")
                # mem_request = MemRequest(member_id, request)
                # loyaltyProg.queueRequest(mem_request)
                continue
            case 8:
                recordsPerRow = int(input("Enter the number of records per row: "))
                loyaltyProg.setRecordsPerRow(recordsPerRow)
                print(f"Number of records per row set to {recordsPerRow}.")
            case 9:
                loyaltyProg.populateData()
                print("Data populated.")
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
