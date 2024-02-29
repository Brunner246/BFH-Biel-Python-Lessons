import tkinter
import cadwork
import element_controller as ec
import attribute_controller as ac


class MyController:
    def __init__(self):
        self.position = cadwork.point_3d(100, 0, 1000)
        self.text_font_size = 100

    def create_node(self) -> int:
        return ec.create_node(self.position)

    def create_text_object(self, text: str) -> int:
        return ec.create_text_object(text, self.position,
                                     cadwork.point_3d(1, 0, 0), cadwork.point_3d(0, 1, 0),
                                     self.text_font_size)

    def set_element_name(self, node_id: int, name: str):
        ac.set_name([node_id], name)


class MyApp(tkinter.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
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
        text_object_id = self.controller.create_text_object(self.name.get())
        self.controller.set_element_name(text_object_id, self.name.get())


if __name__ == "__main__":
    controller = MyController()
    dialog = MyApp(controller)
    dialog.mainloop()
