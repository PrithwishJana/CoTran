public void subArray ( arr , n ) {
    for i in range ( 0 , n ) :
        for j in range ( i , n ) :
            for k in range ( i , j + 1 ) :
                System.out.println ( arr { k } , var end = " " );
            System.out.println ( "\n" , end = "" );
}
var arr = { 1 , 2 , 3 , 4 };
var n = len ( arr );
System.out.println ( "All Non-empty Subarrays" );
subArray ( arr , n ) ;;
