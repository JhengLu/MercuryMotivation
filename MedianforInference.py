import re
import statistics

data = '''

dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   1%|          | 1/88 [00:23<33:43, 23.26s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:30:53
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   2%|▏         | 2/88 [00:42<29:58, 20.91s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:31:12
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   3%|▎         | 3/88 [01:01<28:33, 20.16s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:31:31
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   5%|▍         | 4/88 [01:21<27:46, 19.84s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   6%|▌         | 5/88 [01:40<27:10, 19.64s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:31:51
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:32:10
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   7%|▋         | 6/88 [01:59<26:41, 19.53s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:32:29
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   8%|▊         | 7/88 [02:19<26:18, 19.49s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:32:49
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:   9%|▉         | 8/88 [02:38<26:00, 19.51s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:33:09
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  10%|█         | 9/88 [02:58<25:40, 19.50s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:33:28
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  11%|█▏        | 10/88 [03:17<25:22, 19.52s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:33:48
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  12%|█▎        | 11/88 [03:37<25:05, 19.55s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:34:07
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  14%|█▎        | 12/88 [03:57<24:48, 19.58s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:34:27
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  15%|█▍        | 13/88 [04:16<24:30, 19.61s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:34:47
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  16%|█▌        | 14/88 [04:36<24:12, 19.63s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:35:06
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  17%|█▋        | 15/88 [04:56<23:54, 19.66s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:35:26
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  18%|█▊        | 16/88 [05:15<23:40, 19.73s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:35:46
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  19%|█▉        | 17/88 [05:35<23:22, 19.75s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:36:06
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  20%|██        | 18/88 [05:55<23:03, 19.76s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:36:26
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  22%|██▏       | 19/88 [06:15<22:45, 19.79s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:36:46
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  23%|██▎       | 20/88 [06:35<22:27, 19.81s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:37:05
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  24%|██▍       | 21/88 [06:55<22:08, 19.83s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:37:25
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  25%|██▌       | 22/88 [07:15<21:50, 19.85s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:37:45
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  26%|██▌       | 23/88 [07:34<21:31, 19.87s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:38:05
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  27%|██▋       | 24/88 [07:54<21:13, 19.89s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:38:25
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  28%|██▊       | 25/88 [08:14<20:53, 19.89s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:38:45
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  30%|██▉       | 26/88 [08:34<20:34, 19.91s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:39:05
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  31%|███       | 27/88 [08:54<20:16, 19.95s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:39:25
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  32%|███▏      | 28/88 [09:14<19:59, 19.99s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:39:45
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  33%|███▎      | 29/88 [09:35<19:42, 20.04s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:40:06
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  34%|███▍      | 30/88 [09:55<19:25, 20.09s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:40:26
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  35%|███▌      | 31/88 [10:15<19:07, 20.12s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:40:46
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  36%|███▋      | 32/88 [10:35<18:48, 20.15s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:41:06
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  38%|███▊      | 33/88 [10:55<18:29, 20.18s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:41:26
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  39%|███▊      | 34/88 [11:16<18:10, 20.19s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:41:47
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  40%|███▉      | 35/88 [11:36<17:51, 20.21s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:42:07
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  41%|████      | 36/88 [11:56<17:32, 20.24s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:42:27
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  42%|████▏     | 37/88 [12:17<17:13, 20.27s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:42:48
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  43%|████▎     | 38/88 [12:37<16:54, 20.30s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:43:08
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  44%|████▍     | 39/88 [12:57<16:35, 20.32s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:43:29
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  45%|████▌     | 40/88 [13:18<16:18, 20.38s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:43:49
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  47%|████▋     | 41/88 [13:38<16:00, 20.43s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:44:10
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  48%|████▊     | 42/88 [13:59<15:40, 20.45s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:44:30
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  49%|████▉     | 43/88 [14:19<15:20, 20.46s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  50%|█████     | 44/88 [14:40<15:00, 20.47s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:44:51
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:45:11
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  51%|█████     | 45/88 [15:00<14:40, 20.48s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:45:32
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  52%|█████▏    | 46/88 [15:21<14:20, 20.49s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:45:52
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  53%|█████▎    | 47/88 [15:41<14:01, 20.52s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:46:13
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  55%|█████▍    | 48/88 [16:02<13:42, 20.56s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:46:34
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  56%|█████▌    | 49/88 [16:23<13:23, 20.60s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:46:54
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  57%|█████▋    | 50/88 [16:43<13:03, 20.61s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:47:15
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  58%|█████▊    | 51/88 [17:04<12:44, 20.66s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:47:36
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  59%|█████▉    | 52/88 [17:25<12:25, 20.70s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  60%|██████    | 53/88 [17:46<12:05, 20.73s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:47:57
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  61%|██████▏   | 54/88 [18:07<11:45, 20.76s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:48:17
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  62%|██████▎   | 55/88 [18:28<11:26, 20.80s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:48:38
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:48:59
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  64%|██████▎   | 56/88 [18:48<11:05, 20.81s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:49:20
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  65%|██████▍   | 57/88 [19:09<10:45, 20.84s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:49:41
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  66%|██████▌   | 58/88 [19:30<10:25, 20.86s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  67%|██████▋   | 59/88 [19:51<10:05, 20.89s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:50:02
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:50:23
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  68%|██████▊   | 60/88 [20:12<09:46, 20.96s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:50:44
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  69%|██████▉   | 61/88 [20:33<09:26, 20.99s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:51:05
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  70%|███████   | 62/88 [20:54<09:06, 21.00s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:51:26
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  72%|███████▏  | 63/88 [21:15<08:45, 21.02s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:51:47
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  73%|███████▎  | 64/88 [21:36<08:25, 21.04s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:52:08
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  74%|███████▍  | 65/88 [21:58<08:04, 21.06s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:52:30
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  75%|███████▌  | 66/88 [22:19<07:43, 21.09s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:52:51
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  76%|███████▌  | 67/88 [22:40<07:23, 21.12s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:53:12
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  77%|███████▋  | 68/88 [23:01<07:03, 21.15s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  78%|███████▊  | 69/88 [23:22<06:42, 21.16s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:53:33
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  80%|███████▉  | 70/88 [23:44<06:21, 21.17s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:53:54
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:54:16
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  81%|████████  | 71/88 [24:05<06:00, 21.21s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:54:37
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  82%|████████▏ | 72/88 [24:26<05:39, 21.23s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:54:58
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  83%|████████▎ | 73/88 [24:47<05:18, 21.26s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  84%|████████▍ | 74/88 [25:09<04:58, 21.31s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:55:20
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:55:41
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  85%|████████▌ | 75/88 [25:30<04:37, 21.37s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:56:03
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  86%|████████▋ | 76/88 [25:52<04:16, 21.40s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:56:24
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  88%|████████▊ | 77/88 [26:13<03:55, 21.42s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:56:46
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  89%|████████▊ | 78/88 [26:35<03:34, 21.45s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:57:07
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  90%|████████▉ | 79/88 [26:56<03:13, 21.48s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  91%|█████████ | 80/88 [27:18<02:52, 21.51s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:57:29
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  92%|█████████▏| 81/88 [27:40<02:30, 21.55s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:57:50
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  93%|█████████▎| 82/88 [28:01<02:09, 21.59s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:58:12
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  94%|█████████▍| 83/88 [28:23<01:47, 21.60s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:58:34
dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:58:55
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  95%|█████████▌| 84/88 [28:45<01:26, 21.63s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:59:17
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  97%|█████████▋| 85/88 [29:06<01:04, 21.66s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 20:59:39
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  98%|█████████▊| 86/88 [29:28<00:43, 21.68s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 21:00:01
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set:  99%|█████████▉| 87/88 [29:50<00:21, 21.68s/it]dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set: 100%|██████████| 88/88 [29:58<00:00, 17.78s/it]dlrm_testonly_display_cpu/0 [0]:Current Time: 2024-01-08 21:00:09
dlrm_testonly_display_cpu/0 [0]:
dlrm_testonly_display_cpu/0 [0]:Evaluating test set: 100%|██████████| 88/88 [30:02<00:00, 20.48s/it]
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