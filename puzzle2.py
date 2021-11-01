
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk
import drivers

display = drivers.Lcd()


class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Display LCD")#Inicialitzem la finestra
        #Marquem el tamany de la finsestra per defecte
        self.set_default_size(130, 20) 
        #Inicialitzem la matriu on aniran els elements
        self.grid = Gtk.Grid(column_homogeneous=True,column_spacing=10,row_spacing=10)
        self.add(self.grid)
        #Inicialitzem el textview i creem els botons
        self.create_textview()
        self.create_buttons()
        #Apliquem el estil dissenyat amb CSS
        self.apply_css()
        
    def create_textview(self):
        self.textview = Gtk.TextView()
        #Activem el Wrap Mode per a que la finestra no s'extengui quan arribem al final
        self.wrap = Gtk.WrapMode(1)
        self.textview.set_wrap_mode(self.wrap)
        self.textview.set_size_request(229,110)
        #Activem el monoespaiat per a que tots els caracters ocupin el mateix
        self.textview.set_monospace(True)
        self.textbuffer = self.textview.get_buffer()
        #Afegim el textview a la matriu
        self.grid.attach(self.textview, 0, 1, 3, 1)
        

    def create_buttons(self):
        #Creem el botó de display
        display_button = Gtk.Button(label="Display")
        #L'afegim a la matriu
        self.grid.attach(display_button, 2, 2, 1, 1)
        #Si es clica al botó, s'executa la funció display_clicked
        display_button.connect("clicked",self.display_clicked)
        #Repetim els passos anteriors amb el botó de clear
        clear_button = Gtk.Button(label="Clear")
        self.grid.attach(clear_button, 0, 2, 1, 1)
        clear_button.connect("clicked",self.clear_clicked)              
                       
    def display_clicked(self,button):
        #Comencem amb un clear per a borrar la pantalla del LCD
        display.lcd_clear()
        #Creem els iteradors per a poder fer un get del text del TextView
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        self.text = self.textbuffer.get_text(start_iter, end_iter, True)
        #Usem el métode show_lines, el qual vaig crear al puzzle 1 per a mostrar el text per la pantalla del LCD
        display.show_lines(self.text,len(self.text))
    
    def clear_clicked(self,button):
        #Simplement fem un clear usant el métode de la llibreria del LCD
        display.lcd_clear()
        
    def apply_css(self):
        #En aquest métode es troba el codi necessari per a importar el codi CSS per definir els estils
        screen = Gdk.Screen.get_default()
        css_provider = Gtk.CssProvider()
        try:
            css_provider.load_from_path('styles.css')
            context = Gtk.StyleContext()
            context.add_provider_for_screen(screen, css_provider,
                                            Gtk.STYLE_PROVIDER_PRIORITY_USER)
        except GLib.Error as e:
            print("fError in theme: {e} ")
                               
        
if __name__ == "__main__":
    #Finalment definim el main on creem un onjecte de la classe TextViewWindow
    win = TextViewWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
