n , var k = map ( int , input ( ) . split ( ) );
s = input ( );
if (k == 0) {
    System.out.println ( s );
}
 else if (int ( s ) <= 9){
    System.out.println ( 0 );
}
else{
    var c = 0;
    condition = 0;
    ans = '';
    for i in range ( len ( s ) ) :
        if (i == 0 and condition == 0) {
            ans += '1';
            if (s { i } == '1') {
                c += 0;
            }
             else{
                c += 1;
            }
        }
         else if (condition == 0){
            ans += '0';
            if (s { i } == '0') {
                c += 0;
            }
             else{
                c += 1;
            }
        }
        if (c == k) {
            condition = 1;
            for j in range ( i + 1 , len ( s ) ) :
                ans += s { j };
                if (j == len ( s ) - 1) {
                    c = - 1;
                    break;
                }
         }
     System.out.println ( ans );
}
