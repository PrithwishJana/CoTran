import sched;
public void inp ( ) {
    return ( int ( input ( ) ) );
}
public void inlt ( ) {
    return ( list ( map ( int , input ( ) . split ( ) ) ) );
}
public void insr ( ) {
    var s = input ( );
    return ( list ( s { : len ( s ) - 1 } ) );
}
public void invr ( ) {
    return ( map ( int , input ( ) . split ( ) ) );
}
days , minWalks = inlt ( );
schedule = inlt ( );
additionalWalks = 0;
for i , value in enumerate ( schedule ) :
    if (i != len ( schedule ) - 1) {
        if (value + schedule { i + 1 } < minWalks) {
            missingWalks = minWalks - ( value + schedule { i + 1 } );
            additionalWalks = additionalWalks + missingWalks;
            schedule { i + 1 } = schedule { i + 1 } + missingWalks;
        }
     }
 System.out.println ( additionalWalks );
System.out.println ( * schedule );
