#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#ifdef __linux
#include <unistd.h>
#else
#include <windows.h>
#endif

#include "window.c"

/*  this is the start of the teasharp interpretor.
    It uses gtk for gui capability and is writen in C.
    feel free to add whatever   */ 
int main(int argc, char **argv)
{
    GtkApplication *app;
    int status = 0;

    app = gtk_application_new("org.ts.interpreter", G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
    status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);
    
    return(status);
}
