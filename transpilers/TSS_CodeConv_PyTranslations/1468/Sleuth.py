class Sleuth:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        question = scanner.nextLine().trim()
        originalQ = question[0:len(question) - 1].trim()
        ch = originalQ[len(originalQ) - 1:]
        vowels = ["A", "E", "I", "O", "U", "Y"]
        b = java.util.Arrays.stream(vowels).anyMatch(lambda e : e.equalsIgnoreCase(ch) or e.toLowerCase(java.util.Locale.US).equalsIgnoreCase(ch))
        print("YES" if b else "NO")
