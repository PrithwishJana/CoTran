public void lis ( arr , n ) {
    i , j , var maxm = 0 , 0 , 0;
    lst = { 1 for s in range ( n ) };
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if (( arr { i } > arr { j } and lst { i } < lst { j } + 1 )) {
                lst { i } = lst { j } + 1;
            }
     for i in range ( 0 , n ) :
        if (maxm < lst { i }) {
            maxm = lst { i };
        }
     return maxm;
}
var arr = { 10 , 22 , 9 , 33 , 21 , 50 , 41 , 60 };
var n = len ( arr );
System.out.println ( "Length of lst is" , lis ( arr , n ) );
