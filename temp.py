import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TireTemp:
    def __init__(self, temperatures):
        """
        Initialize the TireTemp class with temperatures.

        :param temperatures: List of four temperature values in Celsius.
        """
        self.temperatures = temperatures
        self.labels = ['Front Left Tire', 'Front Right Tire', 'Back Left Tire', 'Back Right Tire']
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.rects = []
        self.texts = []

        # Define positions for the rectangles
        self.positions = [(0, 2), (2, 2), (0, 0), (2, 0)]

        self.create_plot()

    def get_color(self, temperature):
        """
        Determine the color based on the temperature.

        :param temperature: Temperature value in Celsius.
        :return: Color as a string.
        """
        if temperature < 10:
            return 'green'
        elif 10 <= temperature < 20:
            return 'yellow'
        elif 20 <= temperature < 30:
            return 'orange'
        else:
            return 'red'

    def create_plot(self):
        """
        Create the initial plot with rectangles and text.
        """
        for i, temp in enumerate(self.temperatures):
            color = self.get_color(temp)
            rect = patches.Rectangle(self.positions[i], 2, 2, linewidth=1, edgecolor='black', facecolor=color)
            self.rects.append(rect)
            self.ax.add_patch(rect)
            text = self.ax.text(self.positions[i][0] + 1, self.positions[i][1] + 1, f'{temp}°C\n{self.labels[i]}', fontsize=12, ha='center', va='center', color='black')
            self.texts.append(text)

        # Set the limits and hide the axes
        self.ax.set_xlim(0, 4)
        self.ax.set_ylim(0, 4)
        self.ax.axis('off')

    def update_temperatures(self, new_temperatures):
        """
        Update the temperatures and the plot.

        :param new_temperatures: List of new temperature values in Celsius.
        """
        if len(new_temperatures) != 4:
            raise ValueError("You must provide exactly four temperature values.")

        self.temperatures = new_temperatures

        for i, temp in enumerate(self.temperatures):
            color = self.get_color(temp)
            self.rects[i].set_facecolor(color)
            self.texts[i].set_text(f'{temp}°C\n{self.labels[i]}')

        plt.draw()

# Example usage
temperatures = [5, 15, 25, 35]  # Initial temperatures
tire_temp = TireTemp(temperatures)
plt.show(block=False)

# Update temperatures
new_temperatures = [7, 18, 22, 33]  # New temperature values
tire_temp.update_temperatures(new_temperatures)
plt.pause(2)  # Pause to allow the plot to update

# Update temperatures again
new_temperatures = [10, 20, 30, 40]  # Another set of new temperature values
tire_temp.update_temperatures(new_temperatures)
plt.pause(2)  # Pause to allow the plot to update
