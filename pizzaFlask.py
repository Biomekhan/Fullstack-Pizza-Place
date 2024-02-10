from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"

#@app.route("/about")
#def about():
#    return "About page"

#if __name__ == '__main__':
#    app.run(debug=True)
available_toppings = []

pizza_list = []
class pizza:
    def __init__(self, toppings):
        self.toppings = []
        for topping in toppings:
            if topping in available_toppings:
                self.toppings.append(topping)
            else:
                print(topping + " not available.")
    
    def add_topping(self, topping):
        
        
        if topping in self.toppings:
            print(topping + " is already on the pizza.")
        if topping in available_toppings:
            self.toppings.append(topping)
        else:
            print(topping + " not available.")

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print("Removed" + topping +".")
        else:
            print(topping + " not found on pizza.")
    def show(self):
        print("Toppings: ")
        for topping in self.toppings:
            print(topping + " ")
@app.route('/')
def index():
    return render_template('index.html', pizzas = pizza_list, toppings=available_toppings)

@app.route('/add_topping', methods=['POST'])
def add_topping():
    new_topping = request.form['new_topping']
    if new_topping not in available_toppings:
        available_toppings.append(new_topping)
    return redirect('/')

@app.route('/remove_topping/<topping>')
def remove_topping(topping):
    if topping in available_toppings:
        available_toppings.remove(topping)
    return redirect('/')

@app.route('/edit_topping/<old_topping>', methods=['POST'])
def edit_topping(old_topping):
    new_topping = request.form['edit']
    if old_topping in available_toppings and new_topping not in available_toppings:
        index = available_toppings.index(old_topping)
        available_toppings[index] = new_topping
    return redirect('/')

@app.route('/create_pizza', methods=['POST'])
def create_pizza():
    toppings = request.form.getlist('toppings')
    newPizza = pizza(toppings)
    pizza_list.append(newPizza)
    return redirect('/')

@app.route('/edit_pizza/<int:pizza_index>', methods=['POST'])
def edit_pizza(pizza_index):
    if pizza_index < len(pizza_list):
        toppings = request.form.getlist('toppings')
        pizza_list[pizza_index].toppings = toppings
    return redirect('/')

@app.route('/remove_pizza/<int:pizza_index>')
def remove_pizza(pizza_index):
    if pizza_index < len(pizza_list):
        del pizza_list[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)





