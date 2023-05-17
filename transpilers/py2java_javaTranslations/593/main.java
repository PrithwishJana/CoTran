class node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . next = None;
    }
}
public void add ( data ) {
    newnode = node ( 0 );
    newnode . data = data;
    newnode . var next = None;
    return newnode;
}
public void System.out.printlnArr ( a , n ) {
    i = 0;
    while (( i < n )) {
        System.out.println ( a { i } , end = " " );
        i = i + 1;
    }
 }
public void findlength ( head ) {
    curr = head;
    cnt = 0;
    while (( curr != None )) {
        cnt = cnt + 1;
        curr = curr . next;
    }
     return cnt;
}
public void convertArr ( head ) {
    len1 = findlength ( head );
    arr = {};
    index = 0;
    curr = head;
    while (( curr != None )) {
        arr . append ( curr . data );
        curr = curr . next;
    }
     System.out.printlnArr ( arr , len1 );
}
head = node ( 0 );
head = add ( 1 );
head . next = add ( 2 );
head . next . next = add ( 3 );
head . next . next . next = add ( 4 );
head . next . next . next . next = add ( 5 );
convertArr ( head );
