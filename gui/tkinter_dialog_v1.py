import tkinter
import cadwork
import element_controller as ec
import attribute_controller as ac


def create_node() -> int:
    return ec.create_node(cadwork.point_3d(100, 0, 1000))


def create_text_object(text: str) -> int:
    return ec.create_text_object(text, cadwork.point_3d(100, 0, 1000),
                                 cadwork.point_3d(1, 0, 0), cadwork.point_3d(0, 1, 0),
                                 100)


def set_element_name(node_id: int, name: str):
    ac.set_name([node_id], name)


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.rev = None
        self.ok = None
        self.cancel = None
        self.name = None
        self.nameEntry = None
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack()

        self.name = tkinter.StringVar()
        self.name.set("name...")
        self.nameEntry["textvariable"] = self.name

        self.ok = tkinter.Button(self)
        self.ok["text"] = "Create"
        self.ok["command"] = self.onOk
        self.ok.pack(side="right")

        self.cancel = tkinter.Button(self)
        self.cancel["text"] = "Cancel"
        self.cancel["command"] = self.master.destroy
        self.cancel.pack(side="right")

        self.rev = tkinter.Button(self)
        self.rev["text"] = "Reverse name"
        self.rev["command"] = self.onReverse
        self.rev.pack(side="right")

    def onReverse(self):
        self.name.set(self.name.get()[::-1])

    def onOk(self):
        text_object_id = create_text_object(self.name.get())
        set_element_name(text_object_id, self.name.get())


if __name__ == "__main__":
    dialog = MyApp()
    dialog.mainloop()
