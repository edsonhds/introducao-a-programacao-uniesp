public class lig_prg_ted5 {
    public static void main(String[] args) {        
    }
    static {
        int i = 1;
        while (i <= 20) {
            System.out.print(i);
            if (i % 5 == 0)
                System.out.println();
            else
                System.out.print('\t');
            ++i;
        }
    }
}