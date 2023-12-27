import re
import statistics

data = """

dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   1%|          | 1/88 [00:25<36:20, 25.07s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   2%|▏         | 2/88 [00:46<32:55, 22.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   3%|▎         | 3/88 [01:08<31:41, 22.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   5%|▍         | 4/88 [01:29<30:46, 21.98s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   6%|▌         | 5/88 [01:51<30:08, 21.79s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   7%|▋         | 6/88 [02:12<29:36, 21.66s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   8%|▊         | 7/88 [02:33<29:08, 21.59s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   9%|▉         | 8/88 [02:55<28:45, 21.57s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  10%|█         | 9/88 [03:16<28:21, 21.53s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  11%|█▏        | 10/88 [03:38<28:00, 21.54s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  12%|█▎        | 11/88 [03:59<27:36, 21.51s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  14%|█▎        | 12/88 [04:20<27:04, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  15%|█▍        | 13/88 [04:42<26:49, 21.46s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  16%|█▌        | 14/88 [05:04<26:30, 21.49s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  17%|█▋        | 15/88 [05:25<26:09, 21.50s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  18%|█▊        | 16/88 [05:47<25:47, 21.49s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  19%|█▉        | 17/88 [06:08<25:21, 21.44s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  20%|██        | 18/88 [06:29<24:57, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  22%|██▏       | 19/88 [06:51<24:37, 21.41s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  23%|██▎       | 20/88 [07:12<24:18, 21.45s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  24%|██▍       | 21/88 [07:33<23:52, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  25%|██▌       | 22/88 [07:55<23:27, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  26%|██▌       | 23/88 [08:16<23:04, 21.30s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  27%|██▋       | 24/88 [08:37<22:48, 21.38s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  28%|██▊       | 25/88 [08:59<22:25, 21.35s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  30%|██▉       | 26/88 [09:20<22:06, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  31%|███       | 27/88 [09:42<21:42, 21.36s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  32%|███▏      | 28/88 [10:03<21:19, 21.32s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  33%|███▎      | 29/88 [10:24<20:57, 21.32s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  34%|███▍      | 30/88 [10:45<20:37, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  35%|███▌      | 31/88 [11:07<20:12, 21.27s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  36%|███▋      | 32/88 [11:28<19:49, 21.24s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  38%|███▊      | 33/88 [11:49<19:30, 21.27s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  39%|███▊      | 34/88 [12:10<19:09, 21.29s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  40%|███▉      | 35/88 [12:32<18:51, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  41%|████      | 36/88 [12:53<18:31, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  42%|████▏     | 37/88 [13:15<18:10, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  43%|████▎     | 38/88 [13:36<17:47, 21.35s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  44%|████▍     | 39/88 [13:57<17:23, 21.30s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  45%|████▌     | 40/88 [14:18<17:01, 21.28s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  47%|████▋     | 41/88 [14:40<16:41, 21.30s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  48%|████▊     | 42/88 [15:01<16:17, 21.25s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  49%|████▉     | 43/88 [15:22<15:54, 21.21s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  50%|█████     | 44/88 [15:43<15:29, 21.13s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  51%|█████     | 45/88 [16:04<15:12, 21.23s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  52%|█████▏    | 46/88 [16:25<14:49, 21.18s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  53%|█████▎    | 47/88 [16:47<14:26, 21.13s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  55%|█████▍    | 48/88 [17:08<14:08, 21.22s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  56%|█████▌    | 49/88 [17:29<13:46, 21.20s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  57%|█████▋    | 50/88 [17:51<13:28, 21.27s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  58%|█████▊    | 51/88 [18:12<13:07, 21.29s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  59%|█████▉    | 52/88 [18:33<12:44, 21.23s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  60%|██████    | 53/88 [18:55<12:26, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  61%|██████▏   | 54/88 [19:16<12:05, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  62%|██████▎   | 55/88 [19:37<11:41, 21.26s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  64%|██████▎   | 56/88 [19:58<11:21, 21.28s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  65%|██████▍   | 57/88 [20:20<11:02, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  66%|██████▌   | 58/88 [20:41<10:41, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  67%|██████▋   | 59/88 [21:03<10:18, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  68%|██████▊   | 60/88 [21:24<10:00, 21.43s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  69%|██████▉   | 61/88 [21:46<09:39, 21.47s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  70%|███████   | 62/88 [22:07<09:15, 21.36s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  72%|███████▏  | 63/88 [22:28<08:54, 21.38s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  73%|███████▎  | 64/88 [22:49<08:31, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  74%|███████▍  | 65/88 [23:11<08:11, 21.36s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  75%|███████▌  | 66/88 [23:32<07:50, 21.38s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  76%|███████▌  | 67/88 [23:54<07:30, 21.47s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  77%|███████▋  | 68/88 [24:15<07:07, 21.40s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  78%|███████▊  | 69/88 [24:36<06:45, 21.36s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  80%|███████▉  | 70/88 [24:58<06:25, 21.41s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  81%|████████  | 71/88 [25:19<06:03, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  82%|████████▏ | 72/88 [25:41<05:41, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  83%|████████▎ | 73/88 [26:02<05:19, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  84%|████████▍ | 74/88 [26:23<04:59, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  85%|████████▌ | 75/88 [26:45<04:38, 21.39s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  86%|████████▋ | 76/88 [27:06<04:16, 21.40s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  88%|████████▊ | 77/88 [27:28<03:55, 21.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  89%|████████▊ | 78/88 [27:49<03:34, 21.44s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  90%|████████▉ | 79/88 [28:11<03:12, 21.44s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  91%|█████████ | 80/88 [28:32<02:51, 21.38s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  92%|█████████▏| 81/88 [28:53<02:29, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  93%|█████████▎| 82/88 [29:14<02:07, 21.29s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  94%|█████████▍| 83/88 [29:36<01:46, 21.28s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  95%|█████████▌| 84/88 [29:57<01:25, 21.31s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  97%|█████████▋| 85/88 [30:19<01:04, 21.42s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  98%|█████████▊| 86/88 [30:40<00:42, 21.34s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  99%|█████████▉| 87/88 [31:01<00:21, 21.33s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set: 100%|██████████| 88/88 [31:10<00:00, 17.73s/it]dlrm_testonly_display_cpu/0 [0]:AUROC over test set: 0.5893608331680298.
dlrm_testonly_display_cpu/0 [0]:Number of test samples: 22920308
dlrm_testonly_display_cpu/0 [0]:




"""

# Use regular expression to extract times in the format "12.54s/it"
times = re.findall(r'(\d+\.\d+)s/it', data)

# Convert times to float
times_in_seconds = [float(time) for time in times]

# Calculate the median
median_time = statistics.median(times_in_seconds)
print(f"Median time per iteration: {median_time} seconds/it")
