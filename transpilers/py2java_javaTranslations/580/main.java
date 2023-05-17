var n = int ( input ( ) );
l = { int ( i ) for i in input ( ) . split ( ) };
if (( n == 1 )) {
    System.out.println ( '1' );
}
 else{
    while (( n > 1 )) {
        if (( var l == sorted ( l , reverse = true ) )) {
            System.out.println ( '1' );
            break;
        }
         else if (( l == sorted ( l ) )){
            System.out.println ( n );
            break;
        }
        elif ( l { : n // 2 } != sorted ( l { : n // 2 } ) ) :
            l = l { n // 2 : };
            n //= 2;
        else{
            l = l { : n // 2 };
            n //= 2;
        }
    }
}
 