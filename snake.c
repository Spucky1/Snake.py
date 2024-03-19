#include <stdio.h>
#include <stdlib.h>
int i,j,height=20, width=20,gameover,score;
int x,y,fruitx,fruity,flag;

void draw()
{
    for ( i = 0; i < height; i++){
        for (j = 0; j < width; j++){
            if ( i== 0 || i == width -1 || j == 0 || j == height -1){
                printf("#");
            }
            else {
                printf("");
            }

        }
        printf("\n");
    }
}

void player()
{
    printf("o");
}

int main()
{
    draw();
    player();
    return 0;
}
