
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk
import drivers

display = drivers.Lcd()


class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Display LCD")
        self.set_default_size(130, 20)
        self.grid = Gtk.Grid(column_homogeneous=True,column_spacing=10,row_spacing=10)
        self.add(self.grid)
        self.create_textview()
        self.create_buttons()
        self.apply_css()
        
  

    def create_textview(self):

        self.textview = Gtk.TextView()
        self.wrap = Gtk.WrapMode(1)
        self.textview.set_wrap_mode(self.wrap)
        self.textview.set_size_request(229,110)
        self.textview.set_monospace(True)
        self.textbuffer = self.textview.get_buffer()
        self.grid.attach(self.textview, 0, 1, 3, 1)
        

    def create_buttons(self):
        display_button = Gtk.Button(label="Display")
        self.grid.attach(display_button, 2, 2, 1, 1)
        display_button.connect("clicked",self.display_clicked)
        clear_button = Gtk.Button(label="Clear")
        self.grid.attach(clear_button, 0, 2, 1, 1)
        clear_button.connect("clicked",self.clear_clicked)
        
                       
                       
    def display_clicked(self,button):
        display.lcd_clear()
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        self.text = self.textbuffer.get_text(start_iter, end_iter, True)
        print(self.text)
            
        display.show_lines(self.text,len(self.text))
    
    def clear_clicked(self,button):
        display.lcd_clear()
        
    def apply_css(self):
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
    win = TextViewWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
