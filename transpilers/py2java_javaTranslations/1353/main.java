var n = int ( input ( ) );
while (n) {
    var p = int ( input ( ) );
    l = list ( map ( int , input ( ) . split ( ) ) );
    c = 0;
    s = sum ( l );
    if (s % p == 0) {
        for i in range ( p ) :
            if (l { i } > s // p) {
                c += 1;
            }
         System.out.println ( c );
    }
     else{
        System.out.println ( - 1 );
    }
    n -= 1;
}
 