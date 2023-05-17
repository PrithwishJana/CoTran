public void countPairs ( arr , n ) {
    var count = 0;
    var right = 0;
    var left = 0;
    var visited = { false for i in range ( n ) };
    while (( right < n )) {
        while (( right < n and visited { arr [ right } ] == false )) {
            count += ( right - left );
            visited { arr [ right } ] = true;
            right += 1;
        }
         while (( left < right and ( right != n and visited { arr [ right } ] == true ) )) {
            visited { arr [ left } ] = false;
            left += 1;
        }
     }
     return count;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 4 , 2 , 4 , 3 , 2 };
    var n = len ( arr );
    System.out.println ( countPairs ( arr , n ) );
}
 