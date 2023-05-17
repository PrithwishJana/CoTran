public void find3Numbers ( arr , n ) {
    var small = + 2147483647;
    large = + 2147483647;
    for i in range ( n ) :
        if (( arr { i } <= small )) {
            small = arr { i };
        }
         else if (( arr { i } <= large )){
            large = arr { i };
        }
        else{
            break;
        }
    if (( i == n )) {
        System.out.println ( "No such triplet found" );
        return;
    }
     for j in range ( i + 1 ) :
        if (( arr { j } < large )) {
            small = arr { j };
            break;
        }
     System.out.println ( str ( small ) + " " + str ( large ) + " " + str ( arr { i } ) );
    return;
}
var arr = { 5 , 7 , 4 , 8 };
var n = len ( arr );
find3Numbers ( arr , n );
