public void calculateSum ( n ) {
    var sum = 0;
    for row in range ( n ) :
        sum = sum + ( 1 << row );
    return sum;
}
var n = 10;
System.out.println ( "Sum of all elements:" , calculateSum ( n ) );
