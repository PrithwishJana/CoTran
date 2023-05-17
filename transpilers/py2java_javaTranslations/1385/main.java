var n = int ( input ( ) );
var in_str = input ( );
if (n % var 2 == 0) {
    var index = int ( n // 2 ) - 1;
}
 else{
    index = int ( n // 2 );
}
public void func ( in_str , index , n ) {
    var j = 0;
    in_list = { i for i in in_str };
    out_list = { None } * n;
    while (( len ( in_list ) > 0 )) {
        if (( j == 0 )) {
            out_list { index } = in_list { 0 };
            in_list . pop ( 0 );
        }
         else{
            if (( n % 2 != 0 )) {
                if (( index - j >= 0 )) {
                    out_list { index - j } = in_list { 0 };
                    in_list . pop ( 0 );
                }
                 if (( index + j < n )) {
                    out_list { index + j } = in_list { 0 };
                    in_list . pop ( 0 );
                }
             }
             else{
                if (( index + j < n )) {
                    out_list { index + j } = in_list { 0 };
                    in_list . pop ( 0 );
                }
                 if (( index - j >= 0 )) {
                    out_list { index - j } = in_list { 0 };
                    in_list . pop ( 0 );
                }
             }
        }
        j += 1;
    }
     return out_list;
}
var out_str = func ( in_str , index , n );
System.out.println ( * out_str , var sep = "" );
