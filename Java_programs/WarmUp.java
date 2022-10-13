import java.util.*;

public class WarmUp {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// leitura da primeira linha (valor de n) + conversão
		int n = Integer.parseInt(sc.nextLine());
		
		// leitura da sequencia de inteiros + separação
		String[] numeros = sc.nextLine().split(" "); 
		String saida = "";
		
		for (int i = 0; i < numeros.length; i++) {
			int numero = Integer.parseInt(numeros[i]);
			saida += (numero * n) + " ";
		}
		
		System.out.println(saida.trim());
		sc.close();
	}
}
