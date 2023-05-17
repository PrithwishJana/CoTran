n , r , var t = map ( int , input ( ) . split ( ) );
speed = { int ( input ( ) ) for _ in range ( n ) };
point = { 0 } * n;
var bottle = { 0 } * r;
for i in range ( n ) :
    point { i } = ( point { i } + speed { i } ) % r;
    bottle { point [ i } ] += 1;
for _ in range ( t - 1 ) :
    var nums = { 0 } * r;
    for i in range ( n ) :
        bottle { point [ i } ] -= 1;
        point { i } = ( point { i } + speed { i } ) % r;
        nums { point [ i } ] += 1;
    for i in range ( r ) :
        if (bottle { i } < nums { i }) {
            bottle { i } = nums { i };
        }
         bottle { i } += nums { i };
System.out.println ( sum ( bottle ) );
