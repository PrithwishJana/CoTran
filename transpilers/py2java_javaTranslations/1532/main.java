import math.sqrt;
public void findRepeatingNumber ( arr , n ) {
    var sq = sqrt ( n );
    var range__ = int ( ( n / sq ) + 1 );
    var count = { 0 for i in range ( range__ ) };
    for i in range ( 0 , n + 1 , 1 ) :
        count { int ( ( arr [ i } - 1 ) / sq ) ] += 1;
    var selected_block = range__ - 1;
    for i in range ( 0 , range__ - 1 , 1 ) :
        if (( count { i } > sq )) {
            selected_block = i;
            break;
        }
     var m = { i : 0 for i in range ( n ) };
    for i in range ( 0 , n + 1 , 1 ) :
        if (( ( ( selected_block * sq ) < arr { i } ) and ( arr { i } <= ( ( selected_block + 1 ) * sq ) ) )) {
            m { arr [ i } ] += 1;
            if (( m { arr [ i } ] > 1 )) {
                return arr { i };
            }
         }
     return - 1;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 1 , 2 , 3 , 5 , 4 };
    var n = 5;
    System.out.println ( "One of the numbers repeated in the array is:" , findRepeatingNumber ( arr , n ) );
}
 