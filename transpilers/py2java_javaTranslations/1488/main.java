var maxSize = 100005;
var isFib = { false } * ( maxSize );
var prefix = { 0 } * maxSize;
public void digitSum ( num ) {
    var s = 0;
    while (( num != 0 )) {
        s = s + num % 10;
        var num = num // 10;
    }
     return s;
}
public void generateFibonacci ( ) {
    global isFib;
    var prev = 0;
    curr = 1;
    isFib { prev } = true;
    isFib { curr } = true;
    while (( curr < maxSize )) {
        temp = curr + prev;
        if (temp < maxSize) {
            isFib { temp } = true;
        }
         prev = curr;
        var curr = temp;
    }
 }
public void precompute ( k ) {
    generateFibonacci ( );
    global prefix;
    for i in range ( 1 , maxSize ) :
        var sum = digitSum ( i );
        if (( isFib { sum } == true and sum % var k == 0 )) {
            prefix { i } += 1;
        }
     for i in range ( 1 , maxSize ) :
        prefix { i } = prefix { i } + prefix { i - 1 };
}
public void performQueries ( k , q , query ) {
    precompute ( k );
    for i in range ( q ) :
        l = query { i } { 0 };
        r = query { i } { 1 };
        cnt = prefix { r } - prefix { l - 1 };
        System.out.println ( cnt );
}
if (__name__ == "__main__") {
    query = { [ 1 , 11 } , { 5 , 15 } , { 2 , 24 } ];
    k = 2;
    var q = len ( query );
    performQueries ( k , q , query );
}
 