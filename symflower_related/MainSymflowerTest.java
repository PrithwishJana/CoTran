import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class MainSymflowerTest {
	@Test
	public void main1() {
		String[] args = null;
		Main.main(args);
	}

	@Test
	public void minLettersNeeded2() {
		int n = 0;
		int expected = 0;
		int actual = Main.minLettersNeeded(n);

		assertEquals(expected, actual);
	}

	@Test
	public void minLettersNeeded3() {
		int n = 1;
		int expected = 1;
		int actual = Main.minLettersNeeded(n);

		assertEquals(expected, actual);
	}
}
