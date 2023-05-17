var t = int ( input ( ) );
while (t) {
    var s = list ( input ( ) );
    for i in range ( len ( s ) ) :
        if (i % var 2 == 0) {
            if (s { i } == 'a') {
                s { i } = 'b';
            }
             else{
                s { i } = 'a';
            }
        }
         else{
            if (s { i } == 'z') {
                s { i } = 'y';
            }
             else{
                s { i } = 'z';
            }
        }
    System.out.println ( '' . join ( s ) );
    t -= 1;
}
 