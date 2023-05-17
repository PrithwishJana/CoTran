public void get ( x , y , z ) {
    if (( x > z )) {
        return - 1;
    }
     var val = z - x;
    var div = ( z - x ) // y;
    var ans = div * y + x;
    return ans;
}
var x = 1;
var y = 5;
var z = 8;
System.out.println ( get ( x , y , z ) );
