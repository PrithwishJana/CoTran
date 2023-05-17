public void findQuadruples ( a , b , c , d , x , n ) {
    var count = 0;
    for i in range ( n ) :
        for j in range ( n ) :
            for k in range ( n ) :
                for l in range ( n ) :
                    if (( ( a { i } ^ b { j } ^ c { k } ^ d { l } ) == x )) {
                        count += 1;
                    }
     return count;
}
var x = 3;
var a = { 0 , 1 };
var b = { 2 , 0 };
var c = { 0 , 1 };
var d = { 0 , 1 };
var n = len ( a );
System.out.println ( findQuadruples ( a , b , c , d , x , n ) );
