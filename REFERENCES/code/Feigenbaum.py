import numpy as np
import matplotlib.pyplot as plt

def feigenbaum_noise_simulation():
    """
    Simulates a signal with noise events occurring at Feigenbaum-scaled intervals.
    """
    # Parameters
    feigenbaum_delta = 4.6692016
    n_events = 5
    base_interval = 100.0 # Starting interval
    noise_amplitude = 0.5

    # Calculate event times
    event_times = []
    current_time = 0
    interval = base_interval
    for i in range(n_events):
        current_time += interval
        event_times.append(current_time)
        interval /= feigenbaum_delta # Scale the next interval

    # Generate a baseline signal
    total_time = int(event_times[-1] + base_interval)
    time = np.arange(total_time)
    signal = np.zeros_like(time, dtype=float)

    # Add noise events at the calculated times
    for t in event_times:
        # Add a simple spike or pulse as "noise"
        start_index = int(t)
        if start_index < len(signal):
            signal[start_index] = noise_amplitude

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(time, signal, '-o', markevery=[int(t) for t in event_times])
    plt.title('Conceptual Simulation of Feigenbaum-Scaled Noise', fontsize=16)
    plt.xlabel('Time (Arbitrary Units)', fontsize=12)
    plt.ylabel('Signal Amplitude', fontsize=12)
    plt.ylim(-0.1, noise_amplitude + 0.1)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
    print(f"Noise events occurred at times: {[round(t, 2) for t in event_times]}")

# Run the function
feigenbaum_noise_simulation()