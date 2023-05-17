public void main ( ) {
    while (true) {
        var N = int ( input ( ) );
        if (N == 0) {
            exit ( );
        }
         ( W , H ) = { int ( x ) for x in input ( ) . split ( ) };
        var persimmon = { [ 0 for j in range ( 100 ) } for i in range ( 100 ) ];
        for _ in range ( N ) :
            ( x , y ) = { int ( x ) for x in input ( ) . split ( ) };
            persimmon { x } { y } = 1;
        cumsum = { [ 0 for j in range ( 100 ) } for i in range ( 100 ) ];
        for x in range ( 1 , 100 ) :
            for y in range ( 1 , 100 ) :
                cumsum { x } { y } = cumsum { x - 1 } { y } + cumsum { x } { y - 1 } - cumsum { x - 1 } { y - 1 } + persimmon { x } { y };
        ( S , T ) = { int ( x ) for x in input ( ) . split ( ) };
        max_persimmon = 0;
        for x in range ( S , W + 1 ) :
            for y in range ( T , H + 1 ) :
                max_persimmon = max ( max_persimmon , cumsum { x } { y } + cumsum { x - S } { y - T } - cumsum { x } { y - T } - cumsum { x - S } { y } );
        System.out.println ( max_persimmon );
    }
 }
if (var __name__ == '__main__') {
    main ( );
}
 