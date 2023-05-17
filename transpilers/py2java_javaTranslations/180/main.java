var R = int ( input ( ) . split ( ) { - 1 } );
var best_buy = min ( map ( int , input ( ) . split ( ) ) );
var best_sell = max ( map ( int , input ( ) . split ( ) ) );
var num_buy = R // best_buy;
System.out.println ( max ( R , R + ( best_sell - best_buy ) * num_buy ) );
