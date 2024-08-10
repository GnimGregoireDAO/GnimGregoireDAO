package absenceproject;
import java.util.ArrayList;


public class Cours {
    private String titre;
    private int groupe;
    private ArrayList<Absence> absence = new ArrayList<Absence>();
    private int nbHeures;
    
    public Cours(String titre, int groupe){
        this.titre = titre;
        this.groupe = groupe;
    }
    // Definition des accesseurs
    public String getTitre(){
        return titre;
    }
    public int getGroupe() {
        return groupe;
    }
    public void ajouterAbsence(int semaine, String jour, String nomEtudiant, int nbHeures) throws ExceptionAbsence{
            absence.add(new Absence(6,"12",nomEtudiant, nbHeures));
        
    }
    public int totalAbsence(){
        return absence.size()-1;
    }
    
    public int totalHeuresAbsence() {
    int totalHeuresAbsence = 0;
    for (int i = 0; i < absence.size(); i++) {
        if (absence.get(i).nbHeures != 0) {
            totalHeuresAbsence += absence.get(i).nbHeures;
        }
    }
    return totalHeuresAbsence;
}

        
    }
    

