import operator.itemgetter;
var m_inf = float ( "-inf" );
var n = int ( input ( ) );
var phrase = { 0 } * ( 394 );
for s , l , p in ( map ( int , input ( ) . split ( ) ) for _ in { 0 } * n ) :
    for i , _p in enumerate ( phrase { s : l + 1 } , var start = s ) :
        phrase { i } = _p if _p > p else p;
var dp = { 0 } + { m_inf } * 393;
for length , p in filter ( itemgetter ( 1 ) , enumerate ( phrase ) ) :
    for from_p , to_p , to in zip ( dp , dp { length : } , range ( length , 395 ) ) :
        dp { to } = to_p if to_p >= from_p + p else from_p + p;
var result = { dp [ int ( input ( ) ) } for _ in { 0 } * int ( input ( ) ) ];
System.out.println ( * ( result if m_inf not in result else { - 1 } ) , var sep = "\n" );
