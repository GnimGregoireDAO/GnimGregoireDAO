
package absenceproject;

/**
 *
 * @author Daogr
 */
public class AbsenceProject {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ExceptionAbsence {
        Cours cours = new Cours("Calcul Différentiel", 3);
        cours.ajouterAbsence(6,"12" ,"Alfred",0);
        Fenetre fenetre = new Fenetre(cours);
  
    
}
}
