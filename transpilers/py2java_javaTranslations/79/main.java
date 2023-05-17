public void maximumArea ( l , b , x , y ) {
    left , right , above , var below = 0 , 0 , 0 , 0;
    left = x * b;
    right = ( l - x - 1 ) * b;
    above = l * y;
    below = ( b - y - 1 ) * l;
    System.out.println ( max ( max ( left , right ) , max ( above , below ) ) );
}
var l = 8;
var b = 8;
var x = 0;
var y = 0;
maximumArea ( l , b , x , y );
