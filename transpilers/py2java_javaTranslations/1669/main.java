var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
ma = max ( a );
var mai = a . index ( ma );
var mi = min ( a );
var mii = a . index ( mi );
var ans = {};
if (abs ( ma ) >= abs ( mi )) {
    for i in range ( n ) :
        a { i } += ma;
        ans . append ( ( mai + 1 , i + 1 ) );
    for i in range ( 1 , n ) :
        a { i } += a { i - 1 };
        ans . append ( ( i , i + 1 ) );
}
 else{
    for i in range ( n ) :
        a { i } += mi;
        ans . append ( ( mii + 1 , i + 1 ) );
    for i in range ( n - 2 , - 1 , - 1 ) :
        a { i } += a { i + 1 };
        ans . append ( ( i + 2 , i + 1 ) );
}
System.out.println ( len ( ans ) );
for i in ans : System.out.println ( * i );
