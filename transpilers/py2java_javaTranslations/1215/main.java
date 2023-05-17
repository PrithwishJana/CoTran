import math;
class Node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . next = None;
    }
}
public void getNode ( data ) {
    newNode = Node ( data );
    newNode . data = data;
    return newNode;
}
public void insertEnd ( head , new_node ) {
    if (( var head == None )) {
        new_node . next = new_node;
        new_node . prev = new_node;
        head = new_node;
        return head;
    }
     last = head . prev;
    new_node . next = head;
    head . prev = new_node;
    new_node . prev = last;
    last . next = new_node;
    return head;
}
public void reverse ( head ) {
    if (( head == None )) {
        return None;
    }
     new_head = None;
    last = head . prev;
    curr = last;
    while (( curr . prev != last )) {
        prev = curr . prev;
        new_head = insertEnd ( new_head , curr );
        curr = prev;
    }
     new_head = insertEnd ( new_head , curr );
    return new_head;
}
public void display ( head ) {
    if (( head == None )) {
        return;
    }
     temp = head;
    System.out.println ( "Forward direction: " , end = "" );
    while (( temp . next != head )) {
        System.out.println ( temp . data , end = " " );
        temp = temp . next;
    }
     System.out.println ( temp . data );
    last = head . prev;
    temp = last;
    System.out.println ( "Backward direction: " , end = "" );
    while (( temp . prev != last )) {
        System.out.println ( temp . data , end = " " );
        temp = temp . prev;
    }
     System.out.println ( temp . data );
}
if (__name__ == '__main__') {
    head = None;
    head = insertEnd ( head , getNode ( 1 ) );
    head = insertEnd ( head , getNode ( 2 ) );
    head = insertEnd ( head , getNode ( 3 ) );
    head = insertEnd ( head , getNode ( 4 ) );
    head = insertEnd ( head , getNode ( 5 ) );
    System.out.println ( "Current list:" );
    display ( head );
    head = reverse ( head );
    System.out.println ( "\nReversed list:" );
    display ( head );
}
 