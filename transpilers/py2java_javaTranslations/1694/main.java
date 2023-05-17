var total = 0;
var num_cases = int ( input ( ) );
for i in range ( num_cases ) :
    var line = input ( );
    if (sum ( { int ( x ) for x in line . split ( ) } ) >= 2) {
        total += 1;
    }
 System.out.println ( total );
