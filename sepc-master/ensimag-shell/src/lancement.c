#include <unistd.h>


void lancement(char *prompt) {

  exec(readline(char *prompt));
  printf("%s\n", readline(char *prompt));

}
