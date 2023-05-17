public void sortSquare ( arr , n ) {
    for i in range ( n ) :
        arr { i } = arr { i } * arr { i };
    arr . sort ( );
}
var arr = { - 6 , - 3 , - 1 , 2 , 4 , 5 };
var n = len ( arr );
System.out.println ( "Before sort" );
for i in range ( n ) :
    System.out.println ( arr { i } , var end = " " );
System.out.println ( "" );
sortSquare ( arr , n );
System.out.println ( "After sort" );
for i in range ( n ) :
    System.out.println ( arr { i } , end = " " );
