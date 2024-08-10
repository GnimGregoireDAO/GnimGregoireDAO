
package absenceproject;

public class Absence {
    private int semaine;
    private String jour;
    private String nomEtudiant;
    int nbHeures;
    
//Définition du construu
    public Absence(int semaine, String jour, String nomEtudiant, int nbHeures) throws ExceptionAbsence{
        this.semaine = semaine;
    // Gestion de l'exception sur la semaine 
        if ((semaine < 1) || (semaine > 15)){
            throw new ExceptionAbsence("Semaine doit etre entre 1 et 15");
        }
        this.jour = jour;
        this.nomEtudiant = nomEtudiant;
        this.nbHeures = nbHeures;
        
    }
       
}
