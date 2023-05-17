public class Main {
    static int minLettersNeeded(int n) {
        if (n % 26 == 0) return (n / 26);
        else return ((n / 26) + 1);
    }
    public static void main(String args[]) {
        int n = 52;
        System.out.println(minLettersNeeded(n));
    }
}