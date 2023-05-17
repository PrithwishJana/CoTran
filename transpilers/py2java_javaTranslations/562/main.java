public void findElement ( arr , ranges , rotations , index ) {
    for i in range ( rotations - 1 , - 1 , - 1 ) :
        var left = ranges { i } { 0 };
        var right = ranges { i } { 1 };
        if (( left <= index and right >= index )) {
            if (( var index == left )) {
                index = right;
            }
             else{
                index = index - 1;
            }
        }
     return arr { index };
}
arr = { 1 , 2 , 3 , 4 , 5 };
rotations = 2;
ranges = { [ 0 , 2 } , { 0 , 3 } ];
index = 1;
System.out.println ( findElement ( arr , ranges , rotations , index ) );
