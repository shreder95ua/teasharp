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

#include "arg_processing.h"

/*  this is where the main intactible window is located,
    all configuration on it is done here. */
static void activate(GtkApplication *app, gpointer user_data)
{
    GtkWidget *window;

    window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "TeaSharp");
    gtk_window_set_default_size(GTK_WINDOW(window), 640, 480);
  
    gtk_widget_show(window);
}


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
