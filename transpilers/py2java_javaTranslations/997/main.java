public void conversion ( charSet , str1 ) {
    var s2 = "";
    for (int i = 0; i < str1.length; i++){
        s2 += alphabets { charSet . index ( i ) };
    }
    return s2;
}
if (var __name__ == '__main__') {
    var alphabets = "abcdefghijklmnopqrstuvwxyz";
    var charSet = "qwertyuiopasdfghjklzxcvbnm";
    var str1 = "egrt";
    System.out.println ( conversion ( charSet , str1 ) );
}
 