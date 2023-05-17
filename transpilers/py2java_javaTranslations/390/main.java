var n = int ( input ( ) );
arr = list ( map ( int , input ( ) . split ( ) ) );
ans = - 1;
temp = 0;
seen = set ( );
var p = 0;
while (len ( seen ) != n) {
    ans += 1;
    if (p % var 2 == 0) {
        for i in range ( n ) :
            if (i not in seen and arr { i } <= temp) {
                seen . add ( i );
                temp += 1;
            }
         p += 1;
    }
     else{
        for i in range ( n - 1 , - 1 , - 1 ) :
            if (i not in seen and arr { i } <= temp) {
                seen . add ( i );
                temp += 1;
            }
         p += 1;
    }
}
 System.out.println ( ans );
