public void smallest ( x , y , z ) {
    var c = 0;
    while (( x and y and z )) {
        x = x - 1;
        y = y - 1;
        z = z - 1;
        c = c + 1;
    }
     return c;
}
var x = 12;
var y = 15;
var z = 5;
System.out.println ( "Minimum of 3 numbers is" , smallest ( x , y , z ) );
