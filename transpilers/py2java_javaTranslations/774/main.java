N , M , var L = map ( int , input ( ) . split ( ) );
var tbl = { [ } for i in range ( 45 ) ];
for i in range ( M ) :
    d , a , k , var t = map ( int , input ( ) . split ( ) );
    tbl { d * N + a - 1 } . append ( ( k , t ) );
var dp = { [ 0 for i in range ( 45 ) } for j in range ( 45 ) ];
for da in range ( 5 * N ) :
    for i in range ( L + 1 ) :
        if (i < L) {
            for k , t in tbl { da } :
                dp { da + k } { i + 1 } = max ( dp { da + k } { i + 1 } , dp { da } { i } + t );
        }
         dp { da + 1 } { i } = max ( dp { da + 1 } { i } , dp { da } { i } );
System.out.println ( dp { 5 * N } { L } );
