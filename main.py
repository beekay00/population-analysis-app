import csv
import tkinter as tk
from max_population import find_country_with_max_population

data_dict = {}

def summarize_data(countries, populations):
    global data_dict
    for i in range(len(countries)):
        country = countries[i]
        population = populations[i]

        if country in data_dict:
            data_dict[country] += population
        else:
            data_dict[country] = population

    return data_dict


def format_population(population):
    return "{:,.0f}".format(population)

def save_data_to_file():
    filename = "population_data.txt"
    with open(filename, mode='w', encoding='utf-8') as file:
        for country, population in data_dict.items():
            population_formatted = format_population(population)
            file.write(f"{country}: {population_formatted} million\n")
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Data saved to {filename}")

def handle_sort_data():
    sorted_data = sorted(data_dict.items(), key=lambda x: x[1])
    text_output.delete("1.0", tk.END)
    for country, population in sorted_data:
        population_formatted = format_population(population)
        text_output.insert(tk.END, f"{country}: {population_formatted} million\n")


def visualize_data(data_dict):
    text_output.delete("1.0", tk.END)
    for country, population in data_dict.items():
        population_formatted = format_population(population)
        text_output.insert(tk.END, f"{country}: {population_formatted} million\n")

def handle_search():
    country = search_entry.get().strip()
    if country:
        population = data_dict.get(country)
        if population:
            population_formatted = format_population(population)
            population_label.config(text=f"Population of {country}: {population_formatted} million")
        else:
            population_label.config(text=f"Population data not available for {country}")
    else:
        population_label.config(text="Please enter a country")

def handle_button_click():
    global text_output

    filename = "info.csv"

    countries = []
    populations = []

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            country = row[0]
            population = row[1].replace(" mln", "").replace(" ", "").replace(",", "")

            countries.append(country)
            populations.append(float(population))

    country_with_max_population = find_country_with_max_population(countries, populations)
    result_label.config(text="Country with the highest population: " + country_with_max_population)

    filename2 = "info2.csv"

    with open(filename2, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            country = row[0]
            population = row[1].replace(" mln", "").replace(" ", "").replace(",", "")

            countries.append(country)
            populations.append(float(population))

    global data_dict
    data_dict = summarize_data(countries, populations)

    visualize_data(data_dict)

window = tk.Tk()
window.title("Population Analysis")
window.geometry("400x450")

bg_color = "#F2F2F2"  
button_color = "#4CAF50"  
button_text_color = "white"  
label_text_color = "#333333"  
text_output_bg_color = "white" 

window.configure(bg=bg_color)
button_style = {"background": button_color, "foreground": button_text_color}
label_style = {"fg": label_text_color}
text_output_style = {"background": text_output_bg_color}

button = tk.Button(window, text="Find Max Population", command=handle_button_click, **button_style)
button.pack(pady=10)

result_label = tk.Label(window, text="Result", font=("Arial", 12, "bold"), **label_style)
result_label.pack(pady=10)

text_output = tk.Text(window, height=10, width=30, **text_output_style)
text_output.pack()

search_frame = tk.Frame(window, bg=bg_color)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search Country:", **label_style)
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=20)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", command=handle_search, **button_style)
search_button.pack(side=tk.LEFT)

population_label = tk.Label(window, text="", **label_style)
population_label.pack(pady=10)

sort_data_button = tk.Button(window, text="Sort Data", command=handle_sort_data, **button_style)
sort_data_button.pack(pady=10)

save_data_button = tk.Button(window, text="Save Data", command=save_data_to_file, **button_style)
save_data_button.pack(pady=10)

window.mainloop()


