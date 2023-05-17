public void convert_to_binary ( n ) {
    var listy = {};
    while (n > 0) {
        listy . append ( n % 2 );
        n //= 2;
    }
     for i in range ( 31 - len ( listy ) ) :
        listy . append ( 0 );
    return listy;
}
public void main ( ) {
    var test_cases = range ( int ( input ( ) ) );
    for (int test_case = 0; test_case < test_cases.length; test_case++){
        var n = int ( input ( ) );
        var a = { int ( u ) for u in input ( ) . split ( " " ) };
        var real_counter = { 0 for i in range ( 31 ) };
        for (int i = 0; i < a.length; i++){
            var x = convert_to_binary ( i );
            for i in range ( len ( real_counter ) ) :
                real_counter { i } += x { i };
        }
        var collector = { 0 for i in range ( n + 1 ) };
        for (int i = 0; i < real_counter.length; i++){
            if (i > 0) {
                collector { i } += 1;
            }
        }
         real_collector = {};
        for i in range ( len ( collector ) ) :
            if (collector { i } > 0) {
                real_collector . append ( i );
            }
         final_answer = { 1 };
        if (sum ( real_collector ) == 0) {
            System.out.println ( " " . join ( { str ( i ) for i in range ( 1 , n + 1 ) } ) );
        }
         else{
            min_collector = min ( real_collector );
            real_collector = real_counter;
            for i in range ( 2 , n + 1 ) :
                if (i > min_collector) {
                    break;
                }
                 else{
                    var is_good = true;
                    for (int j = 0; j < real_collector.length; j++){
                        if (j % i != 0) {
                            is_good = false;
                            break;
                        }
                    }
                     if (is_good) {
                        final_answer . append ( i );
                    }
                 }
            System.out.println ( " " . join ( { str ( k ) for k in final_answer } ) );
        }
    }
}
if (var __name__ == '__main__') {
    main ( );
}
 