const world = document.querySelector('#gameBoard');
const c = world.getContext('2d');

world.width = world.clientWidth;
world.height = world.clientHeight;

let frames=0;  

const keys = {
    ArrowLeft: {    pressed:false   },
    ArrowRight: {   pressed:false   }
}

class Player{
    constructor(){
        this.width=32; 
        this.height=32;
        
        this.velocity={
            x:0,
            y:0
        }
    
        const image= new Image();
        image.src = './space.png';
        image.onload =()=>{
            this.image = image;
            this.width=48;
            this.height=48;
            this.position={
                x:world.width/2 - this.width/2,
                y:world.height - this.height -10
            }
        }
    }

    draw(){
        
        c.drawImage(this.image,
            this.position.x,
            this.position.y,
            this.width,
            this.height,
        );
    }
    update(){
        //A chaque frame on redessine le joueur
        this.position.x += this.velocity.x;
        this.draw();
    }
}


const player = new Player();

//Boucle d'animation
const animationLoop= ()=>{
    requestAnimationFrame(animationLoop);
    frames++;
}
animationLoop();