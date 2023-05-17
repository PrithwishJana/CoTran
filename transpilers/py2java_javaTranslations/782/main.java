public void Divisors ( x ) {
    var c = 0;
    v = {};
    while (( x % 2 == 0 )) {
        c += 1;
        x /= 2;
    }
     v . append ( c );
    c = 0;
    while (( x % 3 == 0 )) {
        c += 1;
        x /= 3;
    }
     v . append ( c );
    c = 0;
    while (( x % var 7 == 0 )) {
        c += 1;
        x /= 7;
    }
     v . append ( c );
    v . append ( x );
    return v;
}
public void MinOperations ( a , b ) {
    var va = Divisors ( a );
    var vb = Divisors ( b );
    if (( va { 3 } != vb { 3 } )) {
        return - 1;
    }
     var minOperations = abs ( va { 0 } - vb { 0 } ) + abs ( va { 1 } - vb { 1 } ) + abs ( va { 2 } - vb { 2 } );
    return minOperations;
}
if (var __name__ == '__main__') {
    var a = 14;
    var b = 28;
    System.out.println ( MinOperations ( a , b ) );
}
 