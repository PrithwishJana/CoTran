var n = int ( input ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
l , var r = - 1 , - 1;
for i in range ( n ) :
    if (arr { i } != i + 1) {
        l = i;
        break;
    }
 for i in range ( n - 1 , - 1 , - 1 ) :
    if (arr { i } != i + 1) {
        r = i;
        break;
    }
 var s = r + 1;
for i in range ( l , s ) :
    if (arr { i } == s) {
        s -= 1;
        continue;
    }
     else{
        System.out.println ( 0 , 0 );
        exit ( 0 );
    }
System.out.println ( l + 1 , r + 1 );
