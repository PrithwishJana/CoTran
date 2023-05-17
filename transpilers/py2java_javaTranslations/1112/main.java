public void expect ( m , n ) {
    var ans = 0.0;
    var i = m;
    while (( i )) {
        ans += ( pow ( i / m , n ) - pow ( ( i - 1 ) / m , n ) ) * i;
        i -= 1;
    }
     return ans;
}
if (var __name__ == "__main__") {
    m , var n = 6 , 3;
    System.out.println ( expect ( m , n ) );
}
 