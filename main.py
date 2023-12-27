import re
if __name__ == '__main__':


    text = """
process [2659]: latency = 794.537 ns
process [2659]: latency = 798.126 ns
process [2659]: latency = 792.917 ns
process [2659]: latency = 798.299 ns
process [2659]: latency = 798.811 ns
process [2659]: latency = 800.871 ns
process [2659]: latency = 798.566 ns
process [2659]: latency = 799.207 ns
process [2659]: latency = 800.61 ns
process [2659]: latency = 797.944 ns
process [2659]: latency = 801.957 ns
process [2659]: latency = 798.618 ns
process [2659]: latency = 802.433 ns
process [2659]: latency = 799.808 ns
process [2659]: latency = 797.877 ns
process [2659]: latency = 801.24 ns
process [2659]: latency = 799.21 ns
process [2659]: latency = 800.726 ns
process [2659]: latency = 800.019 ns
process [2659]: latency = 800.044 ns
process [2659]: latency = 799.789 ns
process [2659]: latency = 799.612 ns
process [2659]: latency = 800.336 ns
process [2659]: latency = 798.931 ns
process [2659]: latency = 799.848 ns
process [2659]: latency = 799.432 ns
process [2659]: latency = 791.656 ns
process [2659]: latency = 799.222 ns
process [2659]: latency = 797.269 ns
process [2659]: latency = 790.641 ns
process [2659]: latency = 796.2 ns
process [2659]: latency = 798.264 ns
process [2659]: latency = 798.346 ns
process [2659]: latency = 799.273 ns
process [2659]: latency = 798.063 ns
process [2659]: latency = 797.998 ns
process [2659]: latency = 796.502 ns
process [2659]: latency = 798.61 ns
process [2659]: latency = 797.883 ns
process [2659]: latency = 796.079 ns
process [2659]: latency = 798.352 ns
process [2659]: latency = 796.596 ns
process [2659]: latency = 795.736 ns
process [2659]: latency = 796.69 ns
process [2659]: latency = 798.023 ns
process [2659]: latency = 795.526 ns
process [2659]: latency = 795.876 ns
process [2659]: latency = 797.81 ns
process [2659]: latency = 795.838 ns
process [2659]: latency = 796.305 ns
process [2659]: latency = 799.196 ns
process [2659]: latency = 810.751 ns
process [2659]: latency = 807.312 ns
process [2659]: latency = 810.966 ns
process [2659]: latency = 806.781 ns
process [2659]: latency = 810.792 ns
process [2659]: latency = 808.813 ns
process [2659]: latency = 809.091 ns
process [2659]: latency = 811.769 ns
process [2659]: latency = 813.765 ns
process [2659]: latency = 801.746 ns
process [2659]: latency = 796.158 ns
process [2659]: latency = 792.786 ns
process [2659]: latency = 792.257 ns
process [2659]: latency = 795.477 ns
process [2659]: latency = 792.277 ns
process [2659]: latency = 796.034 ns
process [2659]: latency = 796.483 ns
process [2659]: latency = 797.521 ns
process [2659]: latency = 795.491 ns
process [2659]: latency = 799.08 ns
process [2659]: latency = 796.823 ns
process [2659]: latency = 798.507 ns
process [2659]: latency = 800.971 ns
process [2659]: latency = 797.474 ns

    """

    # Define a regular expression pattern to match latency values
    latency_pattern = r'latency = (\d+\.\d+) ns'

    # Use re.findall to find all matching latency values in the text
    latency_values = re.findall(latency_pattern, text)

    # Convert the extracted values to floating-point numbers
    latencies = [float(value) for value in latency_values]

    # Calculate and print the average latency
    average_latency = sum(latencies) / len(latencies)
    print(f"Average Latency: {average_latency:.3f} ns")


