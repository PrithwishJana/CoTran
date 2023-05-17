import bisect;
var n = int ( input ( ) );
var seq = { int ( input ( ) ) for _ in range ( n ) };
var dp = { seq [ 0 } ];
for (int num = 0; num < seq.length; num++){
    if (num > dp { - 1 }) {
        dp . append ( num );
    }
     else{
        dp { bisect . bisect_left ( dp , num ) } = num;
    }
}
System.out.println ( len ( dp ) );
