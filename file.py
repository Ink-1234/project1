'''**********************single linked list******************'''
'''class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
        print("node created")
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_lst(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next==None:
                current=current.next
            current.next=nn
        print("node inserted")
    def insert_begin(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
    def del_begin(slef):
        if self.head==None:
            print("list is empty")
        else:
            
            nn=self.head
    def insert_before(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            self.head.next==None
            nn.next=self.head
            self.head=nn
    def insert_end(self,target,ele):
        nn=Node(ele)
        current=self.head
        while current and current.data!=target:
            current=current.next
        if current:
            nn.next=current.next
            current.next=nn
        else:
            pritn("node with data",target,"not found")
    def reverse(self):
        current=self.head
        prev=None
        while current:
            next_Node=current.next
            current.next=prev
            prev=current
            current=next_Node
        self.head=prev
        
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            current=self.head

            while current:
                print(current.data,end=" ")
                current=current.next
            print()
list=linkedlist()
while True:
    
    print("1.insert at last 2.insert at begin 3.del_begin  4.insert_before  5.insert_end 6.reverse 7.display 8.exit")
    ch=int(input("enter choice:"))
    
        
    if ch==1:
        ele=int(input("enter ele in list"))
        list.insert_lst(ele)
    elif ch==2:
        ele=int(input("enter ele in list"))
        list.insert_begin(ele)
    elif ch==3:
        list.del_begin()
    elif ch==4:
        ele=int(input("enter ele in list"))
        list.insert_before(ele)
    elif ch==5:
        ele=int(input("enter ele in list"))
        list.insert_end(ele)
    elif ch==6:
        list.reverse()
    
    elif ch==7:
        list.display()
    elif ch==8:
        break'''
    
'''***************************examplle for dll**********************'''

'''class Node:
    def __init__(self,ele):
        self.prev=None
        self.data=ele
        self.next=None
        
        
n1=Node(1)
n2=Node(200)
n3=Node(300)

n1.next=n2
n2.prev=n1
n2.next=n3

n3.prev=n2

start=n1

while start:
    print(start.data,end=' ')
    start=start.next

print()

start=n3
while start:
    print(start.data,end=' ')
    start=start.prev'''


'''****************************double linkedlist****************'''
                      
'''class Node:
    def __init__(self,ele):
        self.prev=None
        self.data=ele
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_lst(self,ele):
        nn=Node(ele)

        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=nn
            nn.prev=current
    def insert_before(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            self.head.next==None
            nn.next=self.head
            self.head=nn


    
    def display(self):
        if self.head==None:
            print("list is emp")
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
    def rev_display(self):
        if self.head==None:
            print("list is emp")
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            while current:
                print(current.data,end=' ')
                current=current.prev
                    

dll=Linkedlist()
while True:
    print("1.insert 2.insert befor 3.display 4.reverse 5.exit")
    ch=int(input("enter choice"))
    if ch==1:
        ele=int(input("enter ele"))
        dll.insert_lst(ele)
    elif ch==2:
        ele=int(input("enter ele"))
        dll.insert_before(ele)
    elif ch==3:
        dll.display()
    elif ch==4:
        dll.rev_display()
    elif ch==5:
        break'''
        
'''***************************stack without class using append*******************'''
            
'''top=-1
st=[]
size=5

    
def push(ele):
    global top
    global size
    
    if top==size-1:
        print("stack is overflow")
    else:
        top +=1
        st.append(ele)
        print("ele is",ele)
        print("ele is pushed ")
def pop():                                      def pop():
                                                        if len(st)==0:
                                                            print("underflow")
                                                        else:
                                                            print(st.pop(),"is poped")
global top                                  def peek():
                                                        if len(st)==0:
                                                            print("empty")
                                                        else:
                                                            print(st[-1])

        if top==-1:
        print("stack is underflow")
    else:
        ele=st[top]
        st.pop()
        top==-1
            
        print("ele is popedS",ele)
def peek():
    if top==-1:
        print("stack is empty")
    else:
        for i in st[top::-1]:
            print(i)
while True:
     print("1.push 2.pop 3.peek ")
     ch=int(input("enter choice"))
     if ch==1:
         ele=int(input("enter ele"))
         push(ele)
     elif ch==2:
         pop()
     elif ch==3:
         peek()'''

'''**************************satck using linked list************'''
                          
'''class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def push_ele(self):
        ele=int(input("enter ele"))
        nn=Node(ele)
        if self.top==None:
            self.top=nn
        else:
            nn.next=self.top
            self.top==nn
    def peek_ele(self):
        if self.top==None:
            print("stack is empty")
        else:
            print(self.top.data,"is top of stack")
    def pop_ele(self):
        if self.top==None:
            print("overflow")
        else:
            print(self.top.data,"is poped")
            self.top=self.top.next



st=Stack()
while True:
    print("1.push 2.pop 3.peek")
    ch=int(input("eter choice"))
    if ch==1:
        st.push_ele()
    elif ch==2:
        st.pop_ele()
    elif ch==3:
        st.peek_ele()
    '''    
'''**************************Queue***************************'''
                        
'''que=[]
frnt=rr=-1
sz=int(input("enter size of q"))
def en_que():
    global frnt,rr
    if rr==sz-1:
        print("overflow")
    else:
        element=int(input("enter ele"))
        if rr==-1:
            frnt=0
        rr=rr+1
        que.append(element)
        print(que)
def de_que():
    global frnt,rr
    if frnt==-1 or frnt>rr:
        print("underflow")
    else:
        element=que[frnt]
        frnt=frnt+1
        print("element")
def peek():
    global frnt,rr
    if frnt==-1 or frnt>rr:
        print("empty")
    else:
        for i in range(frnt,rr+1):
            print(que[i],end=' ')
        print()


while True:
    print("1.push 2.pop 3.peek")
    ch=int(input("eter choice"))
    if ch==1:
        en_que()
    elif ch==2:
        de_que()
    elif ch==3:
        peek()'''
'''****************************Queue using linked list***************************'''

                         
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enq(self,ele):
        ele=int(input("enter ele"))
        nn=Node(ele)

        if self.rear==None:
            self.front=self.rear=nn
        else:
            self.rear.next=nn
            self.rear=nn
    def deq(self):
        if self.front is None:
            print("underflow")
        else:
            ele=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            print(ele,"deleted from queue")
    def dsply(self):
        if self.front is None:
            print("queue empty")
        else:
            current=self.front
            while current:
                print(current.data,end=' ')
                current=current.next
            print()

    def peek(self):
        if self.front is None:
            print("empty")
        else:
            print(self.front.data,end=' ')
que=Queue
while True:
    print("1.push 2.pop 3.dsply  4.peek")
    ch=int(input("eter choice"))
    if ch==1:
        ele=int(input("enter ele"))
        que.enq(ele)
    elif ch==2:
        que.deq()
    elif ch==3:
        que.dsply()
    elif ch==4:
        que.peek()
'''

'''***********************circular Queue implementation using linkedlist**************'''
            
'''class Node:        
    def __init__(self,val):
        self.data=val
        self.next=None
class CircularQueue:
    def __init__(self,size):
        self.front=None
        self.rear=None
        self.size=size
        self.count=0
    def is_full(self):
        return self.count==self.size
    def is_empty(self):
        return self.count==0
    def enqueue(self,data):
        if self.is_full():
            print("queue is overflow")
            return
        new_node=Node(data)
        if self.is_empty():
            self.front=new_node
        else:
            self.rear.next=new_node
        self.rear=new_node
        self.rear.next=self.front
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            print("queue is underflow")
        else:
            data=self.front.data
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
                self.rear.next=self.front
            self.count-=1
            print(data,"deleted")
    def peek(self):
        if self.is_empty():
            print("empty")
        else:
            print("peek of ele ",self.front.data)
    def display(self):
        if self.is_empty():
            print("empty")
        else:
            temp=self.front
            while True:
                print(temp.data,end=' ')
                temp=temp.next
                if temp==self.front:
                    break
            print()
size=int(input("enter size"))
que=CircularQueue(size)
while True:
    print("1.push 2.pop 3.dsply  4.peek")
    ch=int(input("eter choice"))
    if ch==1:
        ele=int(input("enter ele"))
        que.enqueue(ele)
    elif ch==2:
        que.dequeue()
    elif ch==3:
        que.display()
    elif ch==4:
        que.peek()'''

'''**********************************priority Queue implementation using linked list***********************'''
                               
'''class Node:
    def __init__(self,val,prity):
        self.data=val
        self.priority=prity
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data,priority):
        nn=Node(data,priority)
        if self.is_empty()or priority >self.front.priority:
            nn.next=self.front
            self.front=nn
        else:
            current=self.front
            while current.next and current.next.priority> priority:
                current=current.next
            nn.next=current.next
            current.next=nn
    def dequeue(self):
        if self.is_empty():
            print("queue is underflow")
            return None
        data=self.front.data
        self.front=self.front.next
        return data
    def peek(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("peek of ele",self.front.data)
    def display(self):
        if self.is_empty():
            print("empty")
        else:
            current=self.front
            while current:
                print(f"({current.data},{current.priority})",end=' ')
                current=current.next
            print()

pq=PriorityQueue()
while True:
    print("1.push 2.pop 3.dsply  4.peek")
    ch=int(input("eter choice"))
    if ch==1:
        ele=int(input("enter ele"))
        priority=int(input("enter priotity"))
        pq.enqueue(ele,priority)
    elif ch==2:
        pq.dequeue()
    elif ch==3:
        pq.display()
    elif ch==4:
        pq.peek()'''


import datetime

class SoftwareComplianceTracker:
    def _init_(self):
        self.software_data = {}
    print("Welcome to software compilance tracker")

    def create_software(self, software_id, name, license_type, validity_days):
        expiry_date = (datetime.date.today() + datetime.timedelta(days=validity_days)).strftime("%Y-%m-%d")
        self.software_data[software_id] = {
            'name': name,
            'license_type': license_type,
            'expiry_date': expiry_date,
            'compliance_status': 'Compliant'
        }
        return f"{license_type} software {name} created successfully with expiry date: {expiry_date}."

    def read_software_validity(self, software_id):
        if software_id in self.software_data:
            software_info = self.software_data[software_id]
            expiry_date = datetime.datetime.strptime(software_info['expiry_date'], "%Y-%m-%d").date()
            current_date = datetime.date.today()

            if expiry_date >= current_date:
                days_until_expiry = (expiry_date - current_date).days
                return f"{software_info}\nLicense is valid for {days_until_expiry} days."
            else:
                days_since_expiry = (current_date - expiry_date).days
                return f"{software_info}\nSoftware has expired! Days since expiry: {days_since_expiry}"
        else:
            return f"Software with ID {software_id} not found."

    def update_software(self, software_id, name):
        if software_id in self.software_data:
            software_info = self.software_data[software_id]
            license_type = software_info['license_type']
            expiry_date = datetime.datetime.strptime(software_info['expiry_date'], "%Y-%m-%d").date()

            if license_type == 'Mobile Validity':
                amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 250 rupees for 28 days\n2. 600 rupees for 3 months\n")
                try:
                    amount = int(amount)
                except ValueError:
                    return "Invalid amount. Please enter a valid integer."

                if amount == 1:
                    days_to_extend = 28
                elif amount == 2:
                    days_to_extend = 90
                else:
                    return "Invalid amount. Unable to extend the expiry date."

            elif license_type == 'Antivirus Update':
                amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 800 rupees for 180 days\n2. 1500 rupees for 365 days\n")
                try:
                    amount = int(amount)
                except ValueError:
                    return "Invalid amount. Please enter a valid integer."

                if amount == 1:
                    days_to_extend = 180
                elif amount == 2:
                    days_to_extend = 365
                else:
                    return "Invalid amount. Unable to extend the expiry date."

            elif license_type == 'Health License':
                amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 5000 rupees for 2 years\n2. 7000 rupees for 5 years\n")
                try:
                    amount = int(amount)
                except ValueError:
                    return "Invalid amount. Please enter a valid integer."

                if amount == 1:
                    days_to_extend = 730  # 2 years
                elif amount == 2:
                    days_to_extend = 1825  # 5 years
                else:
                    return "Invalid amount. Unable to extend the expiry date."

            new_expiry_date = (expiry_date + datetime.timedelta(days=days_to_extend)).strftime("%Y-%m-%d")

            self.software_data[software_id] = {
                'name': name,
                'license_type': license_type,
                'expiry_date': new_expiry_date,
                'compliance_status': 'Compliant'
            }
            return f"Software with ID {software_id} updated successfully. New expiry date: {new_expiry_date}"
        else:
            return f"Software with ID {software_id} not found."

    def delete_software(self, software_id):
        if software_id in self.software_data:
            del self.software_data[software_id]
            return f"Software with ID {software_id} deleted successfully."
        else:
            return f"Software with ID {software_id} not found."

tracker = SoftwareComplianceTracker()

while True:
    print("\n1. Create Mobile Validity Software\n2. Create Antivirus Update Software\n3. Create Health License Software\n4. Read Software Validity\n5. Update Software\n6. Delete Software\n7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        software_id = input("Enter mobile software ID: ")
        name = input("Enter mobile software name: ")
        validity_days = 28
        print(tracker.create_software(software_id, name, 'Mobile Validity', validity_days))
    elif choice == '2':
        software_id = input("Enter antivirus software ID: ")
        name = input("Enter antivirus software name: ")
        validity_days = 90
        print(tracker.create_software(software_id, name, 'Antivirus Update', validity_days))
    elif choice == '3':
        software_id = input("Enter health license software ID: ")
        name = input("Enter health license software name: ")
        validity_days = 365
        print(tracker.create_software(software_id, name, 'Health License', validity_days))
    elif choice == '4':
        software_id = input("Enter software ID to read: ")
        print(tracker.read_software_validity(software_id))
    elif choice == '5':
        software_id = input("Enter software ID to update: ")
        name = input("Enter updated software name: ")
        print(tracker.update_software(software_id, name))
    elif choice == '6':
        software_id = input("Enter software ID to delete: ")
        print(tracker.delete_software(software_id))
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
    continue_choice = input("Do you want to continue with other software trackers? (yes/no): ")
    if continue_choice.lower() != 'yes':
        break














