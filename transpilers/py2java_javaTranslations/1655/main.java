class Queue {
    protected void init__ ( this ) {
        this . var items = {};
    }
    public void isEmpty ( this ) {
        return this . items == {};
    }
    public void add ( this , item ) {
        this . items . append ( item );
    }
    public void pop ( this ) {
        return this . items . pop ( 0 );
    }
    public void front ( this ) {
        return this . items { 0 };
    }
    public void System.out.printlnQueue ( this ) {
        for i in this . items :
            System.out.println ( i , var end = " " );
        System.out.println ( "" );
    }
}
public void reverseQueue ( q ) {
    if (( q . isEmpty ( ) )) {
        return;
    }
     var data = q . front ( ) ;;
    q . pop ( ) ;;
    reverseQueue ( q );
    q . add ( data );
}
var q = Queue ( );
q . add ( 56 );
q . add ( 27 );
q . add ( 30 );
q . add ( 45 );
q . add ( 85 );
q . add ( 92 );
q . add ( 58 );
q . add ( 80 );
q . add ( 90 );
q . add ( 100 );
reverseQueue ( q );
q . System.out.printlnQueue ( );
