public void nth_term ( a , b , n ) {
    var z = 0;
    if (( n % 6 == 1 )) {
        z = a;
    }
     else if (( n % 6 == 2 )){
        z = b;
    }
    else if (( n % 6 == 3 )){
        z = b - a;
    }
    else if (( n % 6 == 4 )){
        z = - a;
    }
    else if (( n % 6 == 5 )){
        z = - b;
    }
    if (( n % 6 == 0 )) {
        z = - ( b - a );
    }
     return z;
}
if (var __name__ == '__main__') {
    var a = 10;
    var b = 17;
    var n = 3;
    System.out.println ( nth_term ( a , b , n ) );
}
 