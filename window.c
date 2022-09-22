/*  this is where the main intactible window is located,
    all configuration on it is done here. */
#ifndef MAIN_WINDOW
#define MAIN_WINDOW

#include "gui_interpreter.c"

static void activate(GtkApplication *app, gpointer user_data)
{
    GtkWidget *window;

    window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "TeaSharp");
    gtk_window_set_default_size(GTK_WINDOW(window), 640, 480);
  
    gtk_widget_show(window);
}

#endif
