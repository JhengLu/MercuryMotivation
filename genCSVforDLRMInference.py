import re
import csv

data = """
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   1%|          | 1/88 [00:18<26:49, 18.50s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   2%|▏         | 2/88 [00:36<26:03, 18.18s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   3%|▎         | 3/88 [00:54<25:35, 18.07s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   5%|▍         | 4/88 [01:12<25:19, 18.09s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   6%|▌         | 5/88 [01:30<25:08, 18.18s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   7%|▋         | 6/88 [01:49<24:51, 18.18s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   8%|▊         | 7/88 [02:07<24:40, 18.28s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   9%|▉         | 8/88 [02:25<24:18, 18.23s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  10%|█         | 9/88 [02:44<24:03, 18.28s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  11%|█▏        | 10/88 [03:02<23:59, 18.45s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  12%|█▎        | 11/88 [03:22<24:03, 18.75s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  14%|█▎        | 12/88 [03:40<23:43, 18.73s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  15%|█▍        | 13/88 [03:59<23:23, 18.71s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  16%|█▌        | 14/88 [04:18<23:09, 18.77s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  17%|█▋        | 15/88 [04:37<22:59, 18.89s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  18%|█▊        | 16/88 [04:56<22:40, 18.89s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  19%|█▉        | 17/88 [05:16<22:43, 19.21s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  20%|██        | 18/88 [05:35<22:26, 19.24s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  22%|██▏       | 19/88 [05:55<22:09, 19.27s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  23%|██▎       | 20/88 [06:14<21:52, 19.30s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  24%|██▍       | 21/88 [06:34<21:42, 19.45s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  25%|██▌       | 22/88 [06:53<21:26, 19.50s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  26%|██▌       | 23/88 [07:13<21:06, 19.48s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  27%|██▋       | 24/88 [07:33<20:52, 19.58s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  28%|██▊       | 25/88 [07:53<20:43, 19.74s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  30%|██▉       | 26/88 [08:12<20:20, 19.69s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  31%|███       | 27/88 [08:32<20:03, 19.72s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  32%|███▏      | 28/88 [08:52<19:46, 19.78s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  33%|███▎      | 29/88 [09:12<19:29, 19.82s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  34%|███▍      | 30/88 [09:32<19:16, 19.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  35%|███▌      | 31/88 [09:53<19:01, 20.03s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  36%|███▋      | 32/88 [10:13<18:45, 20.10s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  38%|███▊      | 33/88 [10:33<18:31, 20.20s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  39%|███▊      | 34/88 [10:53<18:09, 20.17s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  40%|███▉      | 35/88 [11:14<17:55, 20.30s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  41%|████      | 36/88 [11:35<17:45, 20.49s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  42%|████▏     | 37/88 [11:55<17:22, 20.44s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  43%|████▎     | 38/88 [12:16<17:04, 20.48s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  44%|████▍     | 39/88 [12:36<16:47, 20.55s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  45%|████▌     | 40/88 [12:57<16:25, 20.53s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  47%|████▋     | 41/88 [13:18<16:10, 20.65s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  48%|████▊     | 42/88 [13:39<15:54, 20.75s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  49%|████▉     | 43/88 [14:00<15:38, 20.85s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  50%|█████     | 44/88 [14:21<15:22, 20.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  51%|█████     | 45/88 [14:42<15:03, 21.02s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  52%|█████▏    | 46/88 [15:03<14:42, 21.01s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  53%|█████▎    | 47/88 [15:24<14:23, 21.05s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  55%|█████▍    | 48/88 [15:46<14:03, 21.10s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  56%|█████▌    | 49/88 [16:07<13:48, 21.23s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  57%|█████▋    | 50/88 [16:29<13:27, 21.25s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  58%|█████▊    | 51/88 [16:50<13:11, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  59%|█████▉    | 52/88 [17:12<12:51, 21.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  60%|██████    | 53/88 [17:33<12:29, 21.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  61%|██████▏   | 54/88 [17:55<12:12, 21.55s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  62%|██████▎   | 55/88 [18:16<11:50, 21.53s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  64%|██████▎   | 56/88 [18:38<11:31, 21.62s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  65%|██████▍   | 57/88 [19:00<11:08, 21.55s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  66%|██████▌   | 58/88 [19:21<10:48, 21.61s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  67%|██████▋   | 59/88 [19:43<10:30, 21.73s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  68%|██████▊   | 60/88 [20:05<10:09, 21.77s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  69%|██████▉   | 61/88 [20:27<09:49, 21.85s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  70%|███████   | 62/88 [20:49<09:27, 21.82s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  72%|███████▏  | 63/88 [21:11<09:04, 21.78s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  73%|███████▎  | 64/88 [21:33<08:43, 21.80s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  74%|███████▍  | 65/88 [21:55<08:23, 21.88s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  75%|███████▌  | 66/88 [22:17<08:03, 22.00s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  76%|███████▌  | 67/88 [22:39<07:41, 21.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  77%|███████▋  | 68/88 [23:01<07:19, 21.99s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  78%|███████▊  | 69/88 [23:23<06:58, 22.00s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  80%|███████▉  | 70/88 [23:45<06:36, 22.05s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  81%|████████  | 71/88 [24:07<06:16, 22.13s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  82%|████████▏ | 72/88 [24:30<05:54, 22.13s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  83%|████████▎ | 73/88 [24:52<05:33, 22.26s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  84%|████████▍ | 74/88 [25:15<05:12, 22.31s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  85%|████████▌ | 75/88 [25:37<04:49, 22.23s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  86%|████████▋ | 76/88 [25:59<04:28, 22.38s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  88%|████████▊ | 77/88 [26:22<04:06, 22.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  89%|████████▊ | 78/88 [26:44<03:44, 22.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  90%|████████▉ | 79/88 [27:07<03:23, 22.62s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  91%|█████████ | 80/88 [27:30<03:00, 22.58s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  92%|█████████▏| 81/88 [27:53<02:38, 22.61s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  93%|█████████▎| 82/88 [28:15<02:15, 22.53s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  94%|█████████▍| 83/88 [28:37<01:52, 22.54s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  95%|█████████▌| 84/88 [29:00<01:29, 22.47s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  97%|█████████▋| 85/88 [29:22<01:07, 22.53s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  98%|█████████▊| 86/88 [29:45<00:45, 22.68s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  99%|█████████▉| 87/88 [30:08<00:22, 22.72s/it]dlrm_testonly_display_cpu/0 [0]:
"""

# Use regular expression to extract times in the format "12.54s/it"
times = re.findall(r'(\d+\.\d+)s/it', data)

# Convert times to float
times_in_seconds = [float(time) for time in times]

filename = 'Data/170GB.csv'
# Save times to a CSV file
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Time (s/it)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for time in times_in_seconds:
        writer.writerow({'Time (s/it)': time})

print("Times saved to " + filename)
