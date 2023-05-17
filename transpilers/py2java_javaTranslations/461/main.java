public void findNum ( div , rem , N ) {
    var num = rem { N - 1 };
    i = N - 2;
    while (( i >= 0 )) {
        num = num * div { i } + rem { i };
        i -= 1;
    }
     return num;
}
if (var __name__ == '__main__') {
    var div = { 8 , 3 };
    var rem = { 2 , 2 };
    var N = len ( div );
    System.out.println ( findNum ( div , rem , N ) );
}
 