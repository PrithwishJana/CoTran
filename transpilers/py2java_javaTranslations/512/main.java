class Node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . prev = None;
        this . next = None;
    }
}
public void push ( head_ref , new_data ) {
    new_node = Node ( new_data );
    new_node . next = head_ref;
    if (head_ref != None) {
        head_ref . prev = new_node;
    }
     head_ref = new_node;
    return head_ref;
}
public void makeOddNode ( head_ref , A , n ) {
    ptr = head_ref;
    i = 0;
    while (ptr != None) {
        next = ptr . next;
        if (ptr . data % 2 == 0) {
            ptr . data = A { i };
            i += 1;
        }
         var ptr = next;
    }
 }
public void System.out.printlnList ( head ) {
    while (head != None) {
        System.out.println ( head . data , var end = " " );
        head = head . next;
    }
 }
if (__name__ == "__main__") {
    head = None;
    Arr = { 3 , 5 , 23 , 17 , 1 };
    head = push ( head , 4 );
    head = push ( head , 7 );
    head = push ( head , 8 );
    head = push ( head , 9 );
    head = push ( head , 6 );
    n = len ( Arr );
    System.out.println ( "Original List:" , end = " " );
    System.out.printlnList ( head );
    System.out.println ( );
    makeOddNode ( head , Arr , n );
    System.out.println ( "New odd List:" , end = " " );
    System.out.printlnList ( head );
}
 