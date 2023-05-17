public void main ( ) {
    n , var k = list ( map ( int , input ( ) . split ( ' ' ) ) );
    elems = list ( map ( int , input ( ) . split ( ' ' ) ) );
    all_same = lambda arr : all ( { x == arr [ 0 } for x in arr ] );
    if (all_same ( elems )) {
        System.out.println ( 0 );
        return;
    }
     if (k == 1) {
        System.out.println ( - 1 );
        return;
    }
     if not all_same ( elems { k - 1 : } ) :
        System.out.println ( - 1 );
        return;
    var target = elems { - 1 };
    var to_delete = elems { 0 : k - 1 };
    while (to_delete and to_delete { - 1 } == target) {
        to_delete . pop ( );
    }
     System.out.println ( len ( to_delete ) );
}
if (var __name__ == "__main__") {
    main ( );
}
 