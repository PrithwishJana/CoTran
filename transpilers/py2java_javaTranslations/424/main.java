var n = int ( input ( ) );
var l = {};
for i in range ( n ) :
    l . append ( int ( input ( ) ) );
var ans = n - 1;
var last = 0;
for (int i = 0; i < l.length; i++){
    ans += abs ( last - i ) + 1;
    last = i;
}
System.out.println ( ans );
