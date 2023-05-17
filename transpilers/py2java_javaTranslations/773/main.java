import math;
class Node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . next = None;
    }
}
public void push ( head_ref , new_data ) {
    new_node = Node ( new_data );
    new_node . data = new_data;
    new_node . var next = head_ref;
    head_ref = new_node;
    return head_ref;
}
public void isPrime ( n ) {
    if (( n <= 1 )) {
        return false;
    }
     if (( n <= 3 )) {
        return true;
    }
     if (( n % 2 == 0 or n % 3 == 0 )) {
        return false;
    }
     for i in range ( 5 , n + 1 , 6 ) :
        if (( i * i < n + 2 and ( n % i == 0 or n % ( i + 2 ) == 0 ) )) {
            return false;
        }
     return true;
}
public void deleteNonPrimeNodes ( head_ref ) {
    ptr = head_ref;
    while (( ptr != None and isPrime ( ptr . data ) != true )) {
        temp = ptr;
        ptr = ptr . next;
    }
     head_ref = ptr;
    if (( ptr == None )) {
        return None;
    }
     curr = ptr . next;
    while (( curr != None )) {
        if (( isPrime ( curr . data ) != true )) {
            ptr . next = curr . next;
            var curr = ptr . next;
        }
         else{
            ptr = curr;
            curr = curr . next;
        }
        return head_ref;
    }
 }
public void System.out.printlnList ( head ) {
    while (( head != None )) {
        System.out.println ( head . data , var end = " " );
        var head = head . next;
    }
 }
if (__name__ == '__main__') {
    head = None;
    head = push ( head , 17 );
    head = push ( head , 7 );
    head = push ( head , 6 );
    head = push ( head , 16 );
    head = push ( head , 15 );
    System.out.println ( "Original List: " );
    System.out.printlnList ( head );
    head = deleteNonPrimeNodes ( head );
    System.out.println ( "\nModified List: " );
    System.out.printlnList ( head );
}
 