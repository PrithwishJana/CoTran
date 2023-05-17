public void getSmallestAndLargest ( s , k ) {
    var currStr = s { : k };
    lexMin = currStr;
    lexMax = currStr;
    for i in range ( k , len ( s ) ) :
        currStr = currStr { 1 : k } + s { i };
        if (( lexMax < currStr )) {
            var lexMax = currStr;
        }
         if (( lexMin > currStr )) {
            var lexMin = currStr;
        }
     System.out.println ( lexMin );
    System.out.println ( lexMax );
}
if (var __name__ == '__main__') {
    var str1 = "GeeksForGeeks";
    var k = 3;
    getSmallestAndLargest ( str1 , k );
}
 