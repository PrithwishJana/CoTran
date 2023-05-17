public void calculateSum ( n ) {
    var sum = 0;
    sum = 1 << n ;;
    return ( sum - 1 );
}
var n = 10;
System.out.println ( "Sum of all elements:" , calculateSum ( n ) );
