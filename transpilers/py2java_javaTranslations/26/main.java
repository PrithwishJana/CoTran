import typing.List , Tuple , Union;
import math.ceil;
import typing.List;
public void munimum_number_of_piles ( n : int , n_values : List { int } ) -> int {
    n_values . sort ( );
    var pile = - 1;
    for idx , s in enumerate ( n_values ) :
        k = int ( ceil ( ( idx + 1 ) / ( s + 1 ) ) );
        pile = max ( pile , k );
    return pile;
}
var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
System.out.println ( munimum_number_of_piles ( n , a ) );
