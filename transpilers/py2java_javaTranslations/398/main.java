public void countTriplets ( A , B , C ) {
    var ans = 0;
    for i in range ( 1 , A + 1 ) :
        for j in range ( 1 , B + 1 ) :
            for k in range ( 1 , C + 1 ) :
                if (( i * k > j * j )) {
                    ans += 1;
                }
     return ans;
}
var A = 3;
var B = 2;
var C = 2;
System.out.println ( countTriplets ( A , B , C ) );
