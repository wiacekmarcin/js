pins = []

t1 = """
    @QtCore.pyqtSlot()
    def clicked_pb_217_%d(self):
        self.inReg.setZ217_%d(True)
        self.sendInput()
        self.inReg.setZ217_%d(False)
        self.sendInput()


    @QtCore.pyqtSlot()
    def clicked_pb_217_%d(self):
        self.inReg.setZ217_%d(True)
        self.sendInput()
        self.inReg.setZ217_%d(False)
        self.sendInput()

    @QtCore.pyqtSlot()
    def clicked_pb_217_%dx%d(self):
        self.inReg.setZ217_%d(True)
        self.inReg.setZ217_%d(True)
        self.sendInput()
        self.inReg.setZ217_%d(False)
        self.inReg.setZ217_%d(False)
        self.sendInput()
"""
print(t1 % (2, 2, 2, 3, 3, 3, 2, 3, 2, 3, 2, 3))

