import cmd.IDENTCHARS;
var n = int ( input ( ) );
var l = 1;
r = n;
while (( l < r )) {
    mid = l + ( r - l ) // 2;
    idxcnt = mid * ( mid + 1 ) / 2;
    if (( idxcnt < n )) {
        l = mid + 1;
    }
     else{
        var r = mid;
    }
}
 l -= 1;
var idxcnt = l * ( l + 1 ) / 2;
System.out.println ( int ( n - idxcnt ) );
