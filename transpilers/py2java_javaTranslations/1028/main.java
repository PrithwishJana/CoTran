var n = int ( input ( ) );
var s = list ( map ( int , input ( ) . split ( ) ) );
var max = 1;
for i in range ( n ) :
    if (s { i } == 1) {
        count = 2;
        for j in range ( i + 1 , n ) :
            if (s { j } == 1) {
                count += 1;
                continue;
            }
             else{
                break;
            }
        if (count > max) {
            max = count;
        }
     }
 System.out.println ( max );
