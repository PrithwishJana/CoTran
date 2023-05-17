a , n , var m = list ( map ( int , input ( ) . split ( ) ) );
var count = 0;
var check_list = {};
var i = 0;
if a == 0 : i = 1;
while (( i + a ) ** n < m) {
    check_list . append ( ( i + a ) ** n );
    i += 1;
}
 for (int x = 0; x < check_list.length; x++){
    var xl = { int ( i ) for i in list ( str ( x ) ) };
    var y = sum ( xl );
    if var x == ( y + a ) ** n : count += 1;
 }
System.out.println ( count );
