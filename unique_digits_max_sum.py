'''
ROADIES (100 Marks)
The last season of Roadies was very much criticised by the people as the contestants were dumb.Rannvijay got fed up with people showing only muscles and are without brain.

Rannvijay Singha wants some smart people in this season of Roadies. So, he has decided to give a task. The people who will successfully solve the task will be selected for the final round of Roadies. Rannvijay is a great fan of Mathematics and always want to score maximum.

He has an interesting task to be solved which will require observation and knowledge. 

Rannvijay explains the task to you - "There are N boxes placed in a horizontal line infront of you with each box having a positive integer written on it. You have to tell me the maximum sum which can be formed by choosing the subset of boxes. Simple. But it is Roadies, so it can't be that simple. You have to tell me the maximum sum but the subset of boxes should not have any digit in common. 

Let me give you an example, Suppose there are 5 boxes with positive integers as 14, 12, 23, 45, 39.
14 and 12 cannot be taken in the subset as 1 is common in both. Similarly {12, 23}, {23, 39}, {14, 45} cannot be included in the same subset.
So the subset which forms the maximum sum is {12, 45, 39}. The maximum sum such formed is 96. 
I hope everything is clear. So show your skills and meet me in the final round. Good Luck!."

Input Format
The first line of the input consists of the number of test cases, T. 
The first line of input consists of the number of Boxes, N
The second line of each test case consists of N space separated boxes with positive integers on them.

Constraints
1<= T <=5
1 <= N <= 100
1 <= array elements <= 10^5

Output Format
Print the maximum sum which can be formed for each test case in a separate line.

Sample TestCase 1
Input
3
4
3 5 7 2
5
121 23 3 333 4
7
32 42 52 62 72 82 92

Output
17
458
92

Explanation
Test Case 1: {3, 5, 7, 2} = 17
Test Case 2: {121, 333, 4} = 458
Test Case 3: {92} = 92
'''

def get_list_sum(max_sum_list):
    sum = 0
    for box in max_sum_list:
        sum = sum + box
        
    return sum

    
digits_of_boxes = {}
def get_digits(box_number):
    if box_number in digits_of_boxes:
        return digits_of_boxes[box_number]
        
    digits = []
    for digit in str(box_number):
        digits.append(int(digit))
        
    digits_of_boxes[box_number] = digits
    
    print("Box Number - ", box_number)
    print("digits - ", digits)
    
    return digits
    

def can_box_be_added_to_list(box_number, used_digits_list):
    digits = get_digits(box_number)
    print("can_box_be_added_to_list::box_number- ", box_number)
    print("can_box_be_added_to_list::digits- ", digits)
    print("can_box_be_added_to_list::used_digits_list- ", used_digits_list)
    
    for digit in digits:
        if digit in used_digits_list:
            return False
            
    return True
    
    
def add_box(boxes_list, no_of_boxes, max_sum_list, used_digits_list, current_box_index):
    print("Box Number - ", current_box_index)
    if current_box_index == no_of_boxes:
        return get_list_sum(max_sum_list)

    print("Used digits - ", used_digits_list)
    include_list = list(max_sum_list)
    include_used_digits_list = list(used_digits_list)
    include_sum = 0
    if can_box_be_added_to_list(boxes_list[current_box_index], used_digits_list):
        include_list.append(boxes_list[current_box_index])
        current_box_digits = get_digits(boxes_list[current_box_index])
        include_used_digits_list.extend(current_box_digits)
        include_sum = add_box(boxes_list, no_of_boxes, include_list, include_used_digits_list, current_box_index+1)
        
    exclude_sum = add_box(boxes_list, no_of_boxes, max_sum_list, used_digits_list, current_box_index+1)
    
    if include_sum > exclude_sum:
        return include_sum
    else:
        return exclude_sum
    
    

def process(no_of_boxes, boxes_list):
    boxes_list.sort()
    
    max_sum = add_box(boxes_list, no_of_boxes, [], [], 0)
    print(max_sum)

    
def main():
    no_of_test_cases = int(raw_input("No of test cases- "))
    
    for tc in range(0, no_of_test_cases):
        no_of_boxes = int(raw_input("No of boxes- "))
        boxes_list = map(int, raw_input("Boxes string- ").split())
        print(boxes_list)
        process(no_of_boxes, boxes_list)
    
    return
    

main()