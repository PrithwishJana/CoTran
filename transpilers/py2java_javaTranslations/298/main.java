import sys;
public void main ( lines ) {
    w , m , var k = list ( map ( int , lines { 0 } . split ( ) ) );
    var max_length = 0;
    var available_digits = int ( w / k );
    while (available_digits > 0) {
        current_cost_per_n = len ( str ( m ) );
        same_cost_until = 10 ** ( current_cost_per_n );
        usable_numbers = same_cost_until - m;
        use_digits = usable_numbers * current_cost_per_n;
        m = same_cost_until;
        if (available_digits >= use_digits) {
            max_length += usable_numbers;
            available_digits -= use_digits;
        }
         else{
            max_length += int ( available_digits / current_cost_per_n );
            available_digits = 0;
        }
    }
     System.out.println ( max_length );
}
if (var __name__ == "__main__") {
    main ( sys . stdin . readlines ( ) );
}
 