import math;
class Node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . var next = None;
    }
}
public void prList ( head ) {
    if (( head == None )) {
        return;
    }
     temp = head;
    System.out.println ( temp . data , end = "->" );
    temp = temp . next;
    while (( temp != head )) {
        System.out.println ( temp . data , end = "->" );
        temp = temp . next;
    }
     System.out.println ( head . data );
}
public void deleteK ( head_ref , k ) {
    head = head_ref;
    if (( head == None )) {
        return;
    }
     curr = head;
    prev = None;
    while (true) {
        if (( curr . next == head and curr == head )) {
            break;
        }
         prList ( head );
        for i in range ( k ) :
            prev = curr;
            curr = curr . next;
        if (( curr == head )) {
            prev = head;
            while (( prev . next != head )) {
                prev = prev . next;
            }
             head = curr . next;
            prev . next = head;
            head_ref = head;
        }
         else if (( curr . next == head )){
            prev . next = head;
        }
        else{
            prev . next = curr . next;
        }
    }
 }
public void insertNode ( head_ref , x ) {
    head = head_ref;
    temp = Node ( x );
    if (( head == None )) {
        temp . next = temp;
        head_ref = temp;
        return head_ref;
    }
     else{
        temp1 = head;
        while (( temp1 . next != head )) {
            temp1 = temp1 . next;
        }
         temp1 . next = temp;
        temp . next = head;
    }
    return head;
}
if (var __name__ == '__main__') {
    var head = None;
    head = insertNode ( head , 1 );
    head = insertNode ( head , 2 );
    head = insertNode ( head , 3 );
    head = insertNode ( head , 4 );
    head = insertNode ( head , 5 );
    head = insertNode ( head , 6 );
    head = insertNode ( head , 7 );
    head = insertNode ( head , 8 );
    head = insertNode ( head , 9 );
    var k = 4;
    deleteK ( head , k );
}
 