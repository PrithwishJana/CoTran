public void strangeBDParty ( n : int , m : int , k : { int } , c : { int } ) -> int {
    k . sort ( var reverse = true );
    var cost = l = 0;
    for i in range ( n ) :
        if (l < m and c { l } < c { k [ i } - 1 ]) {
            cost += c { l };
            l += 1;
        }
         else{
            cost += c { k [ i } - 1 ];
        }
    return cost;
}
var rep = int ( input ( ) );
for _ in range ( rep ) :
    n , var m = list ( map ( int , input ( ) . split ( ) ) );
    var k = list ( map ( int , input ( ) . split ( ) ) );
    var c = list ( map ( int , input ( ) . split ( ) ) );
    System.out.println ( strangeBDParty ( n , m , k , c ) );
