import re
import statistics

data = '''
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   1%|          | 1/88 [00:12<18:32, 12.79s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   2%|▏         | 2/88 [00:25<18:09, 12.67s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   3%|▎         | 3/88 [00:37<17:52, 12.61s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   5%|▍         | 4/88 [00:50<17:40, 12.63s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   6%|▌         | 5/88 [01:03<17:30, 12.65s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   7%|▋         | 6/88 [01:15<17:17, 12.66s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   8%|▊         | 7/88 [01:28<17:09, 12.71s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   9%|▉         | 8/88 [01:41<16:57, 12.72s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  10%|█         | 9/88 [01:54<16:50, 12.80s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  11%|█▏        | 10/88 [02:07<16:38, 12.80s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  12%|█▎        | 11/88 [02:20<16:26, 12.81s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  14%|█▎        | 12/88 [02:33<16:17, 12.86s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  15%|█▍        | 13/88 [02:45<16:03, 12.85s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  16%|█▌        | 14/88 [02:58<15:53, 12.89s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  17%|█▋        | 15/88 [03:11<15:39, 12.87s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  18%|█▊        | 16/88 [03:24<15:28, 12.89s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  19%|█▉        | 17/88 [03:37<15:16, 12.91s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  20%|██        | 18/88 [03:50<15:04, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  22%|██▏       | 19/88 [04:03<14:51, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  23%|██▎       | 20/88 [04:16<14:38, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  24%|██▍       | 21/88 [04:29<14:26, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  25%|██▌       | 22/88 [04:42<14:14, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  26%|██▌       | 23/88 [04:55<14:02, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  27%|██▋       | 24/88 [05:08<13:47, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  28%|██▊       | 25/88 [05:21<13:36, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  30%|██▉       | 26/88 [05:34<13:23, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  31%|███       | 27/88 [05:47<13:10, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  32%|███▏      | 28/88 [06:00<12:57, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  33%|███▎      | 29/88 [06:12<12:43, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  34%|███▍      | 30/88 [06:25<12:31, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  35%|███▌      | 31/88 [06:38<12:17, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  36%|███▋      | 32/88 [06:51<12:05, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  38%|███▊      | 33/88 [07:04<11:51, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  39%|███▊      | 34/88 [07:17<11:39, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  40%|███▉      | 35/88 [07:30<11:26, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  41%|████      | 36/88 [07:43<11:12, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  42%|████▏     | 37/88 [07:56<11:01, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  43%|████▎     | 38/88 [08:09<10:47, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  44%|████▍     | 39/88 [08:22<10:36, 12.99s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  45%|████▌     | 40/88 [08:35<10:23, 12.98s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  47%|████▋     | 41/88 [08:48<10:09, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  48%|████▊     | 42/88 [09:01<09:57, 12.99s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  49%|████▉     | 43/88 [09:14<09:43, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  50%|█████     | 44/88 [09:27<09:29, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  51%|█████     | 45/88 [09:40<09:16, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  52%|█████▏    | 46/88 [09:53<09:03, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  53%|█████▎    | 47/88 [10:06<08:50, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  55%|█████▍    | 48/88 [10:19<08:38, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  56%|█████▌    | 49/88 [10:32<08:25, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  57%|█████▋    | 50/88 [10:45<08:13, 12.98s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  58%|█████▊    | 51/88 [10:58<08:00, 12.99s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  59%|█████▉    | 52/88 [11:11<07:46, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  60%|██████    | 53/88 [11:24<07:35, 13.01s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  61%|██████▏   | 54/88 [11:37<07:20, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  62%|██████▎   | 55/88 [11:49<07:07, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  64%|██████▎   | 56/88 [12:02<06:53, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  65%|██████▍   | 57/88 [12:15<06:40, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  66%|██████▌   | 58/88 [12:28<06:28, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  67%|██████▋   | 59/88 [12:41<06:15, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  68%|██████▊   | 60/88 [12:54<06:02, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  69%|██████▉   | 61/88 [13:07<05:49, 12.96s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  70%|███████   | 62/88 [13:20<05:36, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  72%|███████▏  | 63/88 [13:33<05:23, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  73%|███████▎  | 64/88 [13:46<05:10, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  74%|███████▍  | 65/88 [13:59<04:57, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  75%|███████▌  | 66/88 [14:12<04:44, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  76%|███████▌  | 67/88 [14:25<04:31, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  77%|███████▋  | 68/88 [14:38<04:18, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  78%|███████▊  | 69/88 [14:51<04:05, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  80%|███████▉  | 70/88 [15:04<03:52, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  81%|████████  | 71/88 [15:17<03:40, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  82%|████████▏ | 72/88 [15:29<03:27, 12.94s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  83%|████████▎ | 73/88 [15:42<03:13, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  84%|████████▍ | 74/88 [15:55<03:01, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  85%|████████▌ | 75/88 [16:08<02:47, 12.91s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  86%|████████▋ | 76/88 [16:21<02:35, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  88%|████████▊ | 77/88 [16:34<02:22, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  89%|████████▊ | 78/88 [16:47<02:09, 12.92s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  90%|████████▉ | 79/88 [17:00<01:56, 12.91s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  91%|█████████ | 80/88 [17:13<01:43, 12.91s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  92%|█████████▏| 81/88 [17:26<01:30, 12.95s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  93%|█████████▎| 82/88 [17:39<01:17, 12.93s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  94%|█████████▍| 83/88 [17:52<01:04, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  95%|█████████▌| 84/88 [18:05<00:51, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  97%|█████████▋| 85/88 [18:18<00:38, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  98%|█████████▊| 86/88 [18:31<00:25, 12.97s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  99%|█████████▉| 87/88 [18:44<00:12, 12.95s/it]d

'''

# Use regular expression to extract times in the format "12.54s/it"
times = re.findall(r'(\d+\.\d+)s/it', data)

# Convert times to float
times_in_seconds = [float(time) for time in times]

# Calculate the median
median_time = statistics.median(times_in_seconds)
print(f"Median time per iteration: {median_time} seconds/it")

# Calculate the average
average_time = sum(times_in_seconds) / len(times_in_seconds)
print(f"Average time per iteration: {average_time} seconds/it")