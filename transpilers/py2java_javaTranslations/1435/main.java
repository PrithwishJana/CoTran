var m = int ( input ( ) );
for i in range ( m ) :
    var n = int ( input ( ) );
    a = list ( map ( int , input ( ) . split ( ) ) );
    s = sum ( a );
    if (( s % n == 0 )) {
        if (( s // n in a )) {
            System.out.println ( 'YES' );
        }
         else{
            System.out.println ( 'NO' );
        }
    }
     else{
        System.out.println ( 'NO' );
    }
