public void multiply ( array , n ) {
    var pro = 1;
    for i in range ( n ) :
        pro = pro * array { i };
    return pro;
}
var array = { 1 , 2 , 3 , 4 , 5 , 6 };
var n = len ( array );
System.out.println ( multiply ( array , n ) );
