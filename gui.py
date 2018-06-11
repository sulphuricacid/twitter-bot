import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ODD OR EVEN")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.get_text()
        self.entry.connect("activate", self.on_entry_activate)
        vbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button.new_with_label("Go")
        button.connect("clicked", self.on_click_me_clicked)
        vbox.pack_start(button, True, True, 0)

        self.label = Gtk.Label()
        self.label.get_text()
        vbox.pack_start(self.label, True, True, 0)

    def on_entry_activate (self, entry):
        number = entry.get_text()


# after pressing "Go", grab text from entry and run num_check() with it, then set label with the result
    def on_click_me_clicked(self, button):
        number = self.entry.get_text()
        print ('k='+number)
        print ('echo $k')
        print ('python3 webscrap.py $k')
        print ('python3 twitterbot.py')


win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
