public void System.out.printlnMinIndexChar ( Str , patt ) {
    var minIndex = 10 ** 9;
    m = len ( Str );
    n = len ( patt );
    for i in range ( n ) :
        for j in range ( m ) :
            if (( patt { i } == Str { j } and j < minIndex )) {
                minIndex = j;
                break;
            }
     if (( minIndex != 10 ** 9 )) {
        System.out.println ( "Minimum Index var Character = " , Str { minIndex } );
    }
     else{
        System.out.println ( "No character present" );
    }
}
var Str = "geeksforgeeks";
var patt = "set";
System.out.printlnMinIndexChar ( Str , patt );
