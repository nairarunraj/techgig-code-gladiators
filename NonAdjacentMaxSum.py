'''
In the XYZ society, the neighbours hate each other for their attitude. Various activities are organized in the society for Welcoming the New Year. The tickets were provided to each house with an integer written on it. Some got tickets with positive integers and some got tickets with negative integers. In the evening, people had to carry their tickets to the club house where the eligible ones will get the exciting gifts. The eligibility of winning the gift depends on the maximum sum which can be formed from the tickets numbers keeping in mind that neighbours hate each other. Since the neighbours hate each other, the two cannot be together in the list of maximum sum.

The President of the society, Mr. Singh, is a wise man and know that neighbours in society don't like each other. Also, he don't wish to become bad in front of people. So, he came up with an idea to design a program which will provide the list of integers forming maximum sum and thus all the members of the list will be given the gifts. The only problem with this idea is that he don't know programming so he is asking you to provide the correct list of integers. The people may be annoying but are smart and will fight if the list provided by you doesn't form the maximum sum.

Note: The integer written on ticket of individuals may or may not be unique. In case, when there are two list with equal maximum sum, the list with first greater element would be considered. For better understanding, look at the explanation of Test case 4 in Sample Test Case. The tickets with integer 0 are not considered for winning the gifts.

Input Format
The first line of input consist of number of test cases, T.
The first line of each test case consist of the number of houses (tickets distributed) in society, N.
The second line of each test case consist of N space separated tickets with integer written on them.

Constraints
1<= T <=10
1<= N <=10000
-1000<= Integer_on_Ticket <=1000

Output Format
For each test case, print the ticket numbers in a single line forming the maximum sum in the format similar to Sample Test Case.

Sample TestCase 1
Input
5
5
-1 7 8 -5 4 
4
3 2 1 -1 
4
11 12 -2 -1 
4
4 5 4 3 
4
5 10 4 -1
Output
48
13
12
44
10
Explanation
Test Case 1: Maximum sum which can be formed is 12. Element considered 8, 4. Note that Output is printed from the reverse side of the array which is TRUE for all the test cases without the space. So, the output is 48.
Test Case 2: Maximum sum which can be formed is 4. Element considered 3, 1. Output = 13.
Test Case 3: Maximum sum which can be formed is 12 as by taking any other element value of maximum sum decreases.
Test Case 4: Maximum sum which can be formed is 8 by taking 3, 5 or 4, 4. But the output is 4, 4 as 3 is smaller than 4.
Test Case 5: Maximum sum which can be formed is 10.

Time Limit(X):
0.70 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
    
def find_max_sum_at_each_house(no_of_houses, tickets):
    sum_list = [0] * no_of_houses
    winners_list = [[]] * no_of_houses

    # Start at the tail of the list
    # Work your way till the head finding the max sum for each house
    for house_number in range(no_of_houses-1, -1, -1):
        include_add = 0
        if house_number + 2 < no_of_houses:
            # Get the max ticket sum for the closest non-neighbour
            include_add = sum_list[house_number+2]
        
        # Get the sum of ticket numbers if 
        # we include the current house to the 
        # list of the closest non-neighbour
        include = tickets[house_number] + include_add
        
        exclude = 0
        if house_number + 1 < no_of_houses:
            # Get the max ticket sum of the neighbour
            exclude = sum_list[house_number+1]
            
        if include > exclude:
            # Ticket sum of the closest non-neighbour is higher
            # than the ticket sum of the neighbour
            sum_list[house_number] = include
            winners_list[house_number] = []
            
            # Add the current house number to the winners list
            if house_number + 2 < no_of_houses:
                winners_list[house_number] = list(winners_list[house_number+2])
            winners_list[house_number].append(house_number)
        elif include < exclude:
            # Ticket sum of the closest non-neighbour is lower
            # than the ticket sum of the neighbour
            sum_list[house_number] = exclude 
            winners_list[house_number] = []
            
            # Do not include the current house in the winners list
            # Assign the winners list of the neighbour to the current house
            if house_number + 1 < no_of_houses:
                winners_list[house_number] = list(winners_list[house_number+1])
        else:
            # Ticket sum of the closest non-neighbour is equal to
            # the ticket sum of the neighbour
            
            # Choose the list which starts with the highest ticket number
            # Assign the chosen winners list to the current house
            sum_list[house_number] = include
            include_max_sum_list = []
            if house_number + 2 < no_of_houses:
                include_max_sum_list = list(winners_list[house_number+2])
            include_max_sum_list.append(house_number)
            neighbor_max_sum_list = []
            if house_number + 1 < no_of_houses:
                neighbor_max_sum_list = list(winners_list[house_number+1])
                
            shortest_list_length = len(include_max_sum_list) if len(include_max_sum_list) < len(neighbor_max_sum_list) else len(neighbor_max_sum_list)
            for index in range(0, shortest_list_length):
                if tickets[include_max_sum_list[index]] > tickets[neighbor_max_sum_list[index]]:
                    winners_list[house_number] = list(include_max_sum_list)
                    break
                if tickets[include_max_sum_list[index]] < tickets[neighbor_max_sum_list[index]]:
                    winners_list[house_number] = list(neighbor_max_sum_list)
                    break
            else:
                if shortest_list_length == len(include_max_sum_list):
                    winners_list[house_number] = list(include_max_sum_list)
                
                if shortest_list_length == len(neighbor_max_sum_list):
                    winners_list[house_number] = list(neighbor_max_sum_list)
                
    return (sum_list[0], winners_list[0])
    
    
def negative_tickets_check(no_of_houses, tickets):
    highest_negative_number = -99999
    for ticket in tickets:
        if ticket > 0:
            return False
            
        if ticket < 0 and ticket > highest_negative_number:
            highest_negative_number = ticket
            
    return highest_negative_number


def find_winners(no_of_houses, tickets):
    least_negative_ticket = negative_tickets_check(no_of_houses, tickets)
    
    if least_negative_ticket:
        print(least_negative_ticket)
        return
        
    (sum_list, winners_list) = find_max_sum_at_each_house(no_of_houses, tickets)
    print(''.join(map(lambda k: str(tickets[k]), winners_list)))
    
    
def main():
    no_of_test_cases = int(raw_input())
    
    for tc in range(0, no_of_test_cases):
        no_of_houses = int(raw_input())
        tickets = map(int, raw_input().split())
        
        find_winners(no_of_houses, tickets)
        

main()
