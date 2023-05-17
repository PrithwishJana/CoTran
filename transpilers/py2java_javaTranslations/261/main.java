class newNode {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . var next = None;
    }
}
public void System.out.printlnList ( node ) {
    while (( node != None )) {
        System.out.println ( node . data , "->" , end = " " );
        node = node . next;
    }
     System.out.println ( "NULL" );
}
public void cntNodes ( node ) {
    if (( node == None )) {
        return 0;
    }
     return ( 1 + cntNodes ( node . next ) );
}
public void updateList ( head , m ) {
    cnt = cntNodes ( head );
    if (( cnt != m and m < cnt )) {
        skip = cnt - m;
        prev = None;
        curr = head;
        while (( skip > 0 )) {
            prev = curr;
            curr = curr . next;
            skip -= 1;
        }
         prev . next = None;
        tempHead = head;
        head = curr;
        while (( curr . next != None )) {
            curr = curr . next;
        }
         curr . next = tempHead;
    }
     System.out.printlnList ( head );
}
head = newNode ( 4 );
head . next = newNode ( 5 );
head . next . next = newNode ( 6 );
head . next . next . next = newNode ( 1 );
head . next . next . next . next = newNode ( 2 );
head . next . next . next . next . next = newNode ( 3 );
var m = 3;
updateList ( head , m );
