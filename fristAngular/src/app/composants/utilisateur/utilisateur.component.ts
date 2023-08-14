import { Component } from '@angular/core';

@Component({
  selector: 'app-utilisateur',
  templateUrl: './utilisateur.component.html',
  styleUrls: ['./utilisateur.component.scss']
})
export class UtilisateurComponent {
  nom: string ; 
  age: number ;
  email: string;
  hobby: hobby;
  constructor(){
    this.nom ='Yassine';
    this.age = 19;
    this.email ="fofanayassine02@gmail.com"
    this.hobby = {
      hobbyUn:"Basket", hobbyDeux:"Lire", hobbyTrois: "Apprendre"
    }
  }

  onClick(){
    alert("Aucune information pour le moment !!")
  }
}

interface hobby{
  hobbyUn:string;
  hobbyDeux:string;
  hobbyTrois:string;
}
