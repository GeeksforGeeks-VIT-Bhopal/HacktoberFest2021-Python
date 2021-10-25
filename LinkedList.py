from prettytable import PrettyTable

# ----------------------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self, node_id=None, data=None, next_node=None):
        self.node_id = node_id
        self.data = data
        self.next = next_node
# ----------------------------------------------------------------------------------------------------------------------


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = None
# ----------------------------------------------------------------------------------------------------------------------
    # this method adds node at the end of the linked list

    def add_node(self, node_id, data):
        new_node = Node(node_id, data)
        # checks if the linked list is empty or not
        if self.head.data is None:
            self.head = new_node
            print("assigned head")
        # seeker traverses through the list to find the final node of the list
        seeker = self.head
        # traversing through the list
        while seeker.next is not None:
            seeker = seeker.next
        # adding new node to the list
        seeker.next = new_node
        # setting the pointer to None/Null again
        new_node.next = None

# ----------------------------------------------------------------------------------------------------------------------
    # delete last node
    def del_final_node(self):
        prev_node = Node()
        seeker = self.head
        while seeker.next is not None:
            prev_node = seeker
            seeker = seeker.next
        prev_node.next = None
        print("Node Deleted Successfully")

# ----------------------------------------------------------------------------------------------------------------------
    # delete Node at target index
    def del_target_node(self, index):
        seeker = self.head
        prev_node = Node
        while seeker.node_id != index:
            prev_node = seeker
            seeker = seeker.next
            if seeker.next is None:
                print("deleted via if statement")
                print("Deleted Node Successfully")
                break
        prev_node.next = seeker.next
        print("Node '" + str(seeker.node_id) + "' Deleted Successfully")

# ----------------------------------------------------------------------------------------------------------------------
    # this method will take a target value and add a new node there pushing all the nodes forward
    def add_target_node(self, index, node_id, data):
        new_node = Node(node_id, data)
        seeker = self.head
        prev_node = Node
        while seeker.node_id != index:
            prev_node = seeker
            seeker = seeker.next
        prev_node.next = new_node
        new_node.next = seeker
        print("Node '" + str(seeker.node_id) + "' added Successfully at index '" + str(index) + "'")
        while seeker.next is not None:
            seeker.node_id = seeker.node_id + 1
            seeker = seeker.next
        seeker.node_id = seeker.node_id + 1

# ----------------------------------------------------------------------------------------------------------------------
    # this method will display the linked list
    def show_list(self):
        seeker = self.head
        while seeker.next is not None:
            table.add_row([seeker.node_id, seeker.data])
            seeker = seeker.next
        print(table)


# ----------------------------------------------------------------------------------------------------------------------
# main menu of the program where user will select functions that he want to perform
def main_menu():
    choice = int(input("1: Create LikedList\n2: Add Nodes to the end\n3: Delete Nodes from the end\n4: Add Nodes at target Position\n5: Delete Nodes from target position(s)\n6: Display LinkedList\n7: Quit\nchoose between 1 to 7: "))
    if choice == 1:
        def dec():
            decision = int(input("1: Let AI create a LinkedLis for you automatically \n2: Create a LinkedList Manually:\n\t\t\t\t: "))
            if decision == 1:
                length = int(input("How many nodes will your list contain?\n"))
                node_id = int(input("Enter starting ID of the list: "))
                x = int(input("Data starting Point: "))
                while node_id <= length:
                    ListA.add_node(node_id, x)
                    print("VALUE " + str(x) + " added to " + str(node_id) + " node")
                    node_id = node_id + 1
                    x = x + 15
                main_menu()
            elif decision == 2:
                length = int(input("How many nodes will your list contain?\n"))
                node_id = int(input("Enter starting ID of the list: "))
                while node_id <= length:
                    x = int(input("Node ID " + str(node_id) + " Data: "))
                    ListA.add_node(node_id, x)
                    print("VALUE " + str(x) + " added to " + str(node_id) + " node")
                    node_id = node_id + 1
                main_menu()
            else:
                print("You Entered Wrong Pointer choose again")
                final_choice = int(input("Press 1 to go back to Decision menu\n\t\t\t\tOR\nPress 0 if you want to go to main menu\n\t\t\t\t:"))
                if final_choice == 1:
                    dec()
                elif final_choice == 0:
                    main_menu()
                else:
                    print("'You are so DUMB (ノへ￣、) ReRun the code now")
        dec()
    elif choice == 2:
        data = int(input("Enter Data that is to be added: "))
        node_index = int(input("Enter the index of the Node: "))
        ListA.add_node(node_index, data)
        ListA.add_node(1, data)
        ListA.show_list()
        table.clear()
        main_menu()
    elif choice == 3:
        decision = int(input("Are you sure you want to delete Node from the end of this LinkedList? 1= YES 0= NO\n:  "))
        if decision == 1:
            ListA.del_final_node()
            ListA.show_list()
            table.clear()
        elif decision == 0:
            main_menu()
        else:
            print("Wrong choice")
            main_menu()
    elif choice == 4:
        target = int(input("Enter the index of the target node: "))
        data = int(input("What data is it that you want to add to the Node: "))
        ListA.add_node(target, data)
        main_menu()
    elif choice == 5:
        target = int(input("Enter the index of the node that you want deleted"))
        decision = int(input("Are you sure you want to delete this Node? 1= YES 0= NO\n:  "))
        if decision == 1:
            ListA.del_target_node(target)
            ListA.show_list()
            table.clear()
        elif decision == 0:
            main_menu()
        else:
            print("Wrong choice")
            main_menu()
    elif choice == 6:
        ListA.show_list()
        table.clear()
        main_menu()
    elif choice == 7:
        quit()


if __name__ == '__main__':
    table = PrettyTable(["Node_ID", "Data"])
    ListA = LinkedList()
    main_menu()
