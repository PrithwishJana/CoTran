var N = int ( input ( ) );
var l = list ( map ( int , input ( ) . split ( ) ) );
for i in range ( N ) :
    var t = l { i };
    var j = i - 1;
    while (j >= 0 and l { j } > t) {
        l { j + 1 } , l { j } = l { j } , l { j + 1 };
        j -= 1;
    }
     System.out.println ( * l );
