from typing import List
from classes import Member, MemRequest


class LoyaltyManagement:
    '''
    This is a LoyaltyManagement class that manages members and their requests in a loyalty program.

    Attributes:
        members (List[Member]): A list to store Member objects.
        queue (List[MemRequest]): A list to store MemRequest objects.
        recordsPerRow (int): Number of records to display per row.

    Methods:
        populateData() -> None: Adds pre-defined Member objects to the system.
        showMembers(recordsPerRow: int = 1) -> None: Displays members' records.
        setRecordsPerRow(recordsPerRow): Sets the number of records to display per row.
        addMember(member: Member) -> None: Adds a new member to the system.
        sortByPoints(debug=False) -> None: Sorts the 'members' list by points in ascending order.
        sortByMemberId() -> None: Sorts members by Member ID using Insertion Sort.
        sortByTierAndPoints() -> None: Sorts members by Tier and Points using Merge Sort.
        addRequest(mem_request: MemRequest) -> None: Adds member request to the queue if the member exists.
        getQueueLength() -> int: Gets the number of requests in the queue.
        handleNextRequest() -> None: Handles the next request in the queue.
        insertion_sort_on_memberId(): Sorts the 'members' list by Member ID using Insertion Sort algorithm.
'''

    def __init__(self) -> None:
        self.members: List[Member] = []
        self.queue: List[MemRequest] = []
        self.recordsPerRow: int = 1
    
    def addMember(self, member: Member) -> None:
        '''
        Add a new member to the system.

        Args:
            member (Member): An instance of the 'Member' class representing the member to be added to the system.

        Returns:
            None

        Description:
            This method adds a new member to the system by appending the received member to the 'members' list attribute of the instance of the class that the method belongs to.
        '''
        self.members.append(member)

    def showMembers(self) -> None:
        '''Display members' records in a formatted manner.

        This method iterates through the list of members in the system and prints their records.
        Each member's ID, name, email, tier, and points are displayed.
        The records are printed in rows, with the number of records per row determined by the 'recordsPerRow' attribute of the class.

        Returns:
        None
        '''
        for i in range(0, len(self.members), self.recordsPerRow):
            for j in range(self.recordsPerRow):
                if i + j < len(self.members):
                    member = self.members[i + j]
                    print(f'MemID: {member.id}\n'
                          f'Name: {member.name}\nEmail: {member.email}\n'
                          f'Tier: {member.tier}\nPoints: {member.points}')
            print()

    def sortByPoints(self,debug=False) -> List[Member]:
        '''
        Sorts the member list of the 'LoyaltyManagement' class by points using bubble sort.

        Args:
            debug (bool, optional): Flag to enable or disable debug mode. Defaults to False.
        
        Complexity Analysis:
            - Time complexity: O(n^2)
            - Space complexity: O(1)
        '''
        data = self.members # Get the list of members
        dataLen = len(data)
        count = 0
        # Iterate through the list using two nested loops
        for i in range(dataLen - 1):
            for l in range(dataLen - i - 1):
                # Compare adjacent members' points and swap if needed
                if data[l].points > data[l + 1].points:
                    data[l], data[l + 1] = data[l + 1], data[l]
                    if debug: # Print debug information if enabled
                        count+=1
                        print(f'{"-" * 40}\nPass: {count}\n{"-" * 40}'+''.join(f'\nID: {show.id}' for show in data))
                
        return data

    def sortByMemberId(self, debug=False) -> List[Member]:
        '''
        Sort members by their ID using the Insertion Sort algorithm.

        Args:
            debug (bool, optional): Flag to enable or disable debug mode. Defaults to False.

        Returns:
            A sorted list of Member objects based on the member ID

        Complexity Analysis:
            - Time complexity: O(n^2)
            - Space complexity: O(1)
        '''
        data = self.members  # Get the list of members
        count = 0
        # Iterate through members, starting from the second element
        for i, j in enumerate(data[1:], 1):
            k = i - 1
            # Shift elements to insert the current member at the correct position
            while k >= 0 and j.id < data[k].id:
                data[k + 1], k = data[k], k - 1
                if debug: # Print debug information if enabled
                    count+=1
                    print(f'{"-" * 40}\nPass: {count}\n{"-" * 40}'+''.join(f'\nID: {show.id}' for show in data))
            data[k + 1] = j # Insert the current member
        print('-' * 40)
        return data

    def sortByTierAndPoints(data: List[Member]) -> List[Member]:
        '''
        Sorts a list of Member objects based on their tier and points.

        Args:
            data: A list of Member objects to be sorted.

        Returns:
            A sorted list of Member objects based on their tier and points.
        
        Complexity Analysis:
            - Time complexity: O(n log n)
            - Space complexity: O(n)
        '''
        self.populateData()
        def merge(left: List[Member], right: List[Member]) -> List[Member]:
            '''
            Merges two sorted lists based on tier and points.

            Args:
                left: The left sorted list.
                right: The right sorted list.

            Returns:
                The merged sorted list.
            '''
            result = []; i = j = 0 # Initialize
            # Compare elements from both lists and add smaller one to the result
            while i < len(left) and j < len(right):
                if left[i].tier < right[j].tier or (left[i].tier == right[j].tier and left[i].points < right[j].points):
                    result.append(left[i]); i += 1 # Add element from left list & increment
                else: result.append(right[j]); j += 1 # Add element from right list & increment
            # Add any remaining elements from left and right lists
            result.extend(left[i:]); result.extend(right[j:])
            return result
        if len(data) <= 1: return data # If only one element or empty list, return data
        mid = len(data) // 2; right = data[mid:] # Divide the data into two halves
        merged = merge(self.sortByTierAndPoints(data[:mid]), self.sortByTierAndPoints(right))
        # Print merged list after a new list is created
        output = '\n'.join([f'ID: {m.id}' for m in merged])
        print(f'New List:\n{"-" * 40}\n{output}\n{"-" * 40}')
        return merged

    def populateData(self) -> None:
        '''
        Populates the data for the current instance of the class.

        This function creates a list of Member objects with predefined values and adds them to the current instance of the class.
        '''

        data = [
            Member('M002', 'steve', 'steve@mail.com', 'C', 2000),
            Member('M007', 'strange', 'strange@mail.com', 'A', 1000),
            Member('M001', 'peter', 'peter@mail.com', 'C', 1000),
            Member('M005', 'tony', 'tony@mail.com', 'A', 6500),
            Member('M004', 'banner', 'banner@mail.com', 'B', 3500),
            Member('M006', 'clark', 'clark@mail.com', 'B', 5000),
            Member('M003', 'bruce', 'bruce@mail.com', 'B', 3000),
        ]
        for member in data:
            self.addMember(member)
    
    def setRecordsPerRow(self, recordsPerRow):
        self.recordsPerRow = recordsPerRow

    def addRequest(self, mem_request: MemRequest) -> None:
        '''Add member request to the queue if the member exists.'''
        member_set = {member.memberId for member in self.members}
        if mem_request.memberId in member_set:
            self.queue.append(mem_request)
            print('Request added to the queue.')
        else:
            print('Invalid member ID. Request not added to the queue.')

    def getQueueLength(self) -> int:
        '''Get the number of requests in the queue.'''
        return len(self.queue)

    def handleNextRequest(self) -> None:
        '''Handle the next request in the queue.'''
        if not self.queue:
            print('No requests in the queue.')
            return

        next_request = self.queue.popleft('Handling Request:'
                                          f'\nMember ID: {next_request.memberId}'
                                          f'\nRequest: {next_request.request}'
                                          f'\nRemaining requests in the queue: {len(self.queue)}')