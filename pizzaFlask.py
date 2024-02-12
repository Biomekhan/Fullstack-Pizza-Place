from flask import Flask, render_template, request, redirect
app = Flask(__name__)


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
    #Pass the list of pizzas and toppings to the html
    return render_template('index.html', pizzas = pizza_list, toppings=available_toppings)


@app.route('/add_topping', methods=['POST'])
def add_topping():
    #Add new topping, check if field is left blank
    new_topping = request.form['new_topping']
    if (new_topping == ""):
        new_topping = "Error: input left empty"
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
    #Edit an existing topping
    new_topping = request.form['new_topping']
    if (new_topping == ""):
        new_topping = "Error: input left empty"
    #Change the topping if its found in the list
    if old_topping in available_toppings and new_topping not in available_toppings: 
        index = available_toppings.index(old_topping)
        available_toppings[index] = new_topping
    return redirect('/')

@app.route('/create_pizza', methods=['POST'])
def create_pizza():
    toppings = request.form.getlist('toppings')
    newPizza = pizza(toppings)
    dupeFlag = 0
    #Creates a pizza after checking to see if another like it exists
    for i in pizza_list:
        if newPizza.toppings == i.toppings:
            dupeFlag = 1
    #With no duplicates, its good to be added into the list
    if dupeFlag == 0:
        pizza_list.append(newPizza)
    return redirect('/')

@app.route('/edit_pizza/<int:pizza_index>', methods=['POST'])
def edit_pizza(pizza_index):
    #Allows changing the pizzas once they're in the list
    if pizza_index-1 < len(pizza_list):
        toppings = request.form.getlist('toppings')
        pizza_list[pizza_index-1].toppings = toppings
    return redirect('/')

@app.route('/remove_pizza/<int:pizza_index>')
def remove_pizza(pizza_index):
    #This simply removes a pizza.
    print(pizza_index)
    if pizza_index-1 < len(pizza_list):
        del pizza_list[pizza_index-1]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)





