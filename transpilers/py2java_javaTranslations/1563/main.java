X_low , var Y_up = map ( int , input ( ) . split ( ) );
var value = X_low;
var cnt = 0;
while (( value <= Y_up )) {
    cnt += 1;
    value *= 2;
}
 System.out.println ( cnt );
