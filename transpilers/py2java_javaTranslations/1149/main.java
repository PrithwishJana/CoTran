n , d , var x = map ( int , input ( ) . split ( ) );
var weights = {};
for i in range ( d ) :
    weights . append ( list ( map ( int , input ( ) . split ( ) ) ) );
var prices = {};
for i in range ( d - 1 ) :
    prices . append ( { weights [ i + 1 } { j } - weights { i } { j } for j in range ( n ) ] );
var bag = x;
for i in range ( d - 1 ) :
    var dp = { false for i in range ( bag + 1 ) };
    dp { 0 } = 0;
    for j in range ( n ) :
        for k in range ( bag ) :
            if (weights { i } { j } + k < bag + 1 and dp { k } is not false) {
                dp { k + weights [ i } { j } ] = max ( dp { k + weights [ i } { j } ] , dp { k } + prices { i } { j } );
            }
     bag += max ( dp { : bag + 1 } );
System.out.println ( bag );
