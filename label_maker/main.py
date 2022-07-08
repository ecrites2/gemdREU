import matplotlib.pyplot as plt
from experimenter_identity import Identity
from chemical_identity import Chemicals
from space_and_time import SpaceTime
from reaction_coordinate_plot import ReactionDiagram

def HideSomeSpines(ax):
    """ This is just a function to hide the top and right spines on a plt diagram because I do it so often """
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return

def HideAllSpines(ax):
    """ This is just a function to hide the top and right spines on a plt diagram because I do it so often """
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    return

def main3():
    """ Main function in 3 dimensions """
    # Figure instance
    fig, ax = plt.subplots(nrows=2, ncols=1, gridspec_kw={"height_ratios": [1, 4]})

    #### Reaction Diagram ####
    dwell = ReactionDiagram(12, 72, 48, 55, 1200, 25)
    times = dwell.GetTimeIntervals()
    function_times = dwell.function_times
    temps = dwell.temperatures

    # Portions of the reaction diagram
    start = dwell.StartEndVector(temps[0], 0)
    heating = dwell.HeatingCoolingDwellingVector(function_times[0], function_times[1], temps[0], temps[1])
    hot = dwell.HeatingCoolingDwellingVector(function_times[1], function_times[2], temps[1], temps[1])
    cooling = dwell.HeatingCoolingDwellingVector(function_times[2], function_times[3], temps[1], temps[2])
    end = dwell.StartEndVector(temps[2], 1)
    # Temperatures of each portion in the reaction diagram
    temps = dwell.GetTemperatures()
    times = dwell.GetFunctionalTimes()
    steps = dwell.CreateStepVectors3(temps, times)
    ##
    new = dwell.PlotStepVectors3(ax[1], steps, temps)
    old = dwell.AnnotateTemperatures3(ax[1], steps)
    mid = dwell.AnnotateTimes3(ax[1], steps)
    ##
    dwell.AnnotateRates3(ax[1], steps)

    dwell = ReactionDiagram(12, 72, 48, 55, 1200, 25)

    #### Experimenter Identity ####
    sam = Identity("Name", "JHED")
    sam.NotebookNumber("Page Number")
    sam.AnnotateName(ax[0])
    sam.AnnotateJHED(ax[0])
    sam.AnnotateEmail(ax[0])
    sam.AnnotateNotebookNumber(ax[0])

    #### Date, Location, Time, etc. ####
    spacetime = SpaceTime(20221218, 245, 20221219, 1355)
    spacetime.AnnotateStart(ax[0])
    spacetime.AnnotateEnd(ax[0])

    #### Chemicals and Such ####
    chemical = Chemicals("Ba2O3", "I2")
    chemical.AnnotateCompound(ax[0])
    chemical.AnnotateTransportAgent(ax[0])

    ## Plotting shenanigans ## ADD TICK MARKS AT MAJOR TEMPERATURES
    plt.xticks([])  # comment this out?
    plt.yticks([])  # comment this out?
    plt.xlabel("Time")
    plt.ylabel("Temperature")

    HideSpines(ax[0])
    HideSpines(ax[1])

    # More plotting shenanigans
    ax = ax[0]
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    plt.savefig("Demo.png")
    return

def master(times, temps):
    """ Main function in N dimensions """
    # Figure instance
    fig, ax = plt.subplots(nrows=2, ncols=1, gridspec_kw={"height_ratios": [1, 4]})

    #### Reaction Diagram ####
    dwell = ReactionDiagram(times=times, temps=temps)

    # Portions of the reaction diagram
    vector_array = dwell.CreateVectors()
    dwell.PlotVectors(ax[1], vector_array)

    #### Experimenter Identity ####
    sam = Identity("Name", "JHED")
    sam.NotebookNumber("Page Number")
    sam.AnnotateName(ax[0])
    sam.AnnotateJHED(ax[0])
    sam.AnnotateEmail(ax[0])
    sam.AnnotateNotebookNumber(ax[0])

    #### Date, Location, Time, etc. ####
    spacetime = SpaceTime(20221218, 245, 20221219, 1355)
    spacetime.AnnotateStart(ax[0])
    spacetime.AnnotateEnd(ax[0])

    #### Chemicals and Such ####
    chemical = Chemicals("Superconductor", "I2")
    chemical.AnnotateCompound(ax[0])
    chemical.AnnotateTransportAgent(ax[0])

    # Beautification
    # Top subplot
    HideAllSpines(ax[0])
    ax[0].set_xticks([])
    ax[0].set_yticks([])

    # Bottom subplot
    HideSomeSpines(ax[1])
    ax[1].set_xticks([])
    ax[1].set_yticks([])

    plt.suptitle("I am a God")
    plt.savefig("Trial.pdf")
    return

if __name__ == "__main__":
    time_array = [5, 48, 4, 36, 5, 66, 10, 25, 1]
    temp_array = [25, 1200, 800, 1100, 400, 25]
    master(times=time_array, temps=temp_array)
