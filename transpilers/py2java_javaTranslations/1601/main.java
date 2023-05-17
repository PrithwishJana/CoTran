import numpy as np;
var a = np . vectorize ( int ) ( input ( ) . split ( ) );
var cnt2 = np . vectorize ( lambda x : int ( ( np . max ( a ) - x ) / 2 ) ) ( a );
var cnt1 = np . max ( a ) - a - 2 * cnt2;
System.out.println ( sum ( cnt2 ) + { 0 , 2 , 1 } { sum ( cnt1 ) } );
