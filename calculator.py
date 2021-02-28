import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.final_nums = []

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton("Enter", clicked = lambda: self.func_result())
        btn_clear = qtw.QPushButton("Clear", clicked = lambda: self.clear_calc())
        btn_9 = qtw.QPushButton("9", clicked = lambda: self.num_press("9"))
        btn_8 = qtw.QPushButton("8", clicked = lambda: self.num_press("8"))
        btn_7 = qtw.QPushButton("7", clicked = lambda: self.num_press("7"))
        btn_6 = qtw.QPushButton("6", clicked = lambda: self.num_press("6"))
        btn_5 = qtw.QPushButton("5", clicked = lambda: self.num_press("5"))
        btn_4 = qtw.QPushButton("4", clicked = lambda: self.num_press("4"))
        btn_3 = qtw.QPushButton("3", clicked = lambda: self.num_press("3"))
        btn_2 = qtw.QPushButton("2", clicked = lambda: self.num_press("2"))
        btn_1 = qtw.QPushButton("1", clicked = lambda: self.num_press("1"))
        btn_0 = qtw.QPushButton("0", clicked = lambda: self.num_press("0"))
        btn_plus = qtw.QPushButton("+", clicked = lambda: self.func_press("+"))
        btn_minus = qtw.QPushButton("-", clicked = lambda: self.func_press("-"))
        btn_mult = qtw.QPushButton("x", clicked = lambda: self.func_press("*"))
        btn_div = qtw.QPushButton("/", clicked = lambda: self.func_press("/"))

        # Add buttons to GridLayout
        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)

        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)

        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)

        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)

        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_div, 5, 3)
        self.layout().addWidget(container)

    # Add number
    def num_press(self, number):
        self.temp_nums.append(number)
        temp_string = "".join(self.temp_nums)
        if self.final_nums:
            self.result_field.setText("".join(self.final_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    # Add function operator
    def func_press(self, operator):
        temp_string = "".join(self.temp_nums)
        self.final_nums.append(temp_string)
        self.final_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText("".join(self.final_nums))

    # Calculate and display result
    def func_result(self):
        if len(self.final_nums) > 0:
            fin_string = "".join(self.final_nums) + "".join(self.temp_nums)
            result_string = eval(fin_string)
            fin_string += "="
            fin_string += str(result_string)
            self.result_field.setText(fin_string)
            print(fin_string)

    # Empty lists and result_field
    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.final_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
app.exec_()
