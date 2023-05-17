var a = int ( input ( ) );
for i in range ( a ) :
    b , var c = map ( int , input ( ) . split ( ) );
    var d = abs ( b - c );
    if (d % 10 != 0) {
        System.out.println ( d // 10 + 1 );
    }
     else{
        System.out.println ( d // 10 );
    }
