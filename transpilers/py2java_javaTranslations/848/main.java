var N = int ( input ( ) );
var ABs = { tuple ( map ( int , input ( ) . split ( ) ) ) for _ in range ( N ) };
var bsum = 0;
for A , B in ABs :
    bsum += B;
var dp = { [ - 1 } * ( bsum + 1 ) for _ in range ( N + 1 ) ];
dp { 0 } { 0 } = 0;
for i , ( A , B ) in enumerate ( ABs ) :
    for j in reversed ( range ( i + 1 ) ) :
        for k in range ( bsum + 1 ) :
            if (dp { j } { k } == - 1) {
                continue;
            }
             var nk = min ( bsum , k + 2 * A - B );
            dp { j + 1 } { nk } = max ( dp { j + 1 } { nk } , dp { j } { k } + B );
var answer = { 0 } * ( N );
for j in range ( 1 , N + 1 ) :
    for k in range ( bsum + 1 ) :
        if (dp { j } { k } == - 1) {
            continue;
        }
         answer { j - 1 } = max ( answer { j - 1 } , dp { j } { k } + k );
System.out.println ( * { a / 2 for a in answer } );
