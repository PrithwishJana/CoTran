var N = 1000;
public void lastElement ( a , n ) {
    var steps = 1;
    var v = { [ } for i in range ( n ) ];
    if var n == 1 : return a { 0 };
    for i in range ( 0 , n , 2 ) :
        v { steps } . append ( a { i } | a { i + 1 } );
    while (len ( v { steps } ) > 1) {
        steps += 1;
        for i in range ( 0 , len ( v { steps - 1 } ) , 2 ) :
            if (steps & 1) {
                v { steps } . append ( v { steps - 1 } { i } | v { steps - 1 } { i + 1 } );
            }
             else{
                v { steps } . append ( v { steps - 1 } { i } ^ v { steps - 1 } { i + 1 } );
            }
    }
     return v { steps } { 0 };
}
if (__name__ == "__main__") {
    a = { 1 , 4 , 5 , 6 };
    n = len ( a );
    index , value , a { 0 } = 0 , 2 , 2;
    System.out.println ( lastElement ( a , n ) );
    index , var value = 3 , 5;
    value = 5;
    a { index } = value;
    System.out.println ( lastElement ( a , n ) );
}
 